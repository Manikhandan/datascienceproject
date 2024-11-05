from src.datascience.constants import *
from src.datascience.utils.common import read_yaml, create_directories
from src.datascience.entity.config_entity import (DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelEvaluationConfig, ModelTrainerConfig)

## whenver this configurationmanager calls then whaterver mwntioned in config, schema, params file needs to be call here
## so using config_filepath we are getting all info in those 3 files totally

## This class manages configurations for various stages of the ML pipeline
class ConfigurationManager: 

    ## Initializes the ConfigurationManager instance, loading configurations from specified files
    def __init__(self,
                 config_filepath=CONFIG_FILE_PATH,  ## Path to main config file (default defined by CONFIG_FILE_PATH)
                 params_filepath=PARAMS_FILE_PATH,  ## Path to parameters file for model parameters (default defined by PARAMS_FILE_PATH)
                 schema_filepath=SCHEMA_FILE_PATH): ## Path to schema file for data validation (default defined by SCHEMA_FILE_PATH)

        # Reads YAML content from the provided config file path
        self.config = read_yaml(config_filepath)  
        
        # Reads YAML content from the parameters file for model hyperparameters
        self.params = read_yaml(params_filepath)
        
        # Reads YAML content from the schema file for data validation schema
        self.schema = read_yaml(schema_filepath)

        ## Creates an artifacts folder (or any other specified root directory) to store all generated files
        create_directories([self.config.artifacts_root]) 

    ## we ned to intiate data injection so we need all config info here, thats y creatingthis function get data injection config
    ## Method to retrieve data ingestion configurations; called whenever we need settings for the data ingestion step
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        
        # Extracts the 'data_ingestion' section from the main configuration file
        config = self.config.data_ingestion

        # Ensures the root directory for data ingestion is created and ready to store ingested data
        create_directories([config.root_dir])

        # Initializes and returns a DataIngestionConfig object with specific configurations for data ingestion
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,  ## Directory to store ingested data files
            source_URL=config.source_URL,  ## URL for downloading data
            local_data_file=config.local_data_file,  ## Local path to save the downloaded data file
            unzip_dir=config.unzip_dir  ## Directory to extract the downloaded file

        )
        return data_ingestion_config  ##this data injecton config will parse to my data injection pipeline Returns the configured DataIngestionConfig instance

    # Method to retrieve the data validation configuration as a DataValidationConfig object
    def get_data_validation_config(self) -> DataValidationConfig:

        # Accesses the data_validation section from the main config file, which contains specific settings for data validation
        config = self.config.data_validation

        # Accesses column schema information from the schema file, specifying the expected structure of the data
        schema = self.schema.COLUMNS

        # Ensures the root directory for data validation exists, creating it if necessary
        create_directories([config.root_dir])

        # Creates an instance of DataValidationConfig with settings required for data validation
        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,            # Sets the root directory for data validation
            STATUS_FILE=config.STATUS_FILE,      # Path to a status file for tracking validation status
            unzip_data_dir=config.unzip_data_dir, # Directory where unzipped data will be stored
            all_schema=schema                    # Schema information to validate data columns
        )

        # Returns the data validation configuration object, which contains all required settings for validation tasks
        return data_validation_config



    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
        )

        return data_transformation_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.ElasticNet
        schema =  self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data_path = config.train_data_path,
            test_data_path = config.test_data_path,
            model_name = config.model_name,
            alpha = params.alpha,
            l1_ratio = params.l1_ratio,
            target_column = schema.name
            
        )

        return model_trainer_config
    
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config=self.config.model_evaluation
        params=self.params.ElasticNet
        schema=self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_evaluation_config=ModelEvaluationConfig(
            root_dir=config.root_dir,
            test_data_path=config.test_data_path,
            model_path = config.model_path,
            all_params=params,
            metric_file_name = config.metric_file_name,
            target_column = schema.name,
            mlflow_uri="https://dagshub.com/manikhandan1997/datascienceproject.mlflow"


        )
        return model_evaluation_config