import os
import urllib.request as request
from src.datascience import logger
import zipfile
from src.datascience.entity.config_entity import (DataIngestionConfig)


## Data Ingestion component responsible for handling data downloading and extraction
class DataIngestion:
    
    ## Initializes the DataIngestion instance with a given configuration
    def __init__(self, config: DataIngestionConfig):
        
        # Sets the configuration for data ingestion, provided by a DataIngestionConfig object
        self.config = config

    ## Downloads the file from a URL if it does not already exist locally
    def download_file(self):
        
        # Checks if the file does not already exist at the specified path
        if not os.path.exists(self.config.local_data_file):
            
            # Downloads the file from the source URL to the local file path
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,  ## URL to download the file from
                filename=self.config.local_data_file  ## Local file path to save the downloaded file
            )
            
            # Logs the download details with filename and headers
            logger.info(f"{filename} downloaded with the following info: \n{headers}")
        
        # If the file exists, logs a message that it already exists
        else:
            logger.info(f"File already exists")

    ## Extracts the downloaded zip file into the specified directory
    def extract_zip_file(self):
        """
        Extracts the zip file contents into the directory specified in the configuration
        Function returns None
        """
        
        # Sets the path to unzip files to, as specified in the configuration
        unzip_path = self.config.unzip_dir
        
        # Ensures the target directory for unzipping exists; if not, creates it
        os.makedirs(unzip_path, exist_ok=True)
        
        # Opens the downloaded zip file in read mode to extract its contents
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            
            # Extracts all files in the zip to the specified directory
            zip_ref.extractall(unzip_path)
