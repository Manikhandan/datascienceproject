# datascienceproject

# End to End Data Science Project

### Workflows--ML Pipeline

1. Data Ingestion - Collects data from various sources, storing it locally for further processing and use in the pipeline.
2. Data Validation -if we recive any new dataset to predcit the resultsthen that data should be in the correct data type with the same data strcture. Ensures data quality and integrity by checking for missing values, data types, and anomalies to confirm that data is ready for use.
3. Data Transformation-- Feature Engineering,Data Preprocessing - Applies transformations, such as scaling, encoding, or feature engineering, to prepare data for optimal model performance.
4. Model Trainer - Trains machine learning models on prepared data, tuning parameters to achieve the best results.
5. Model Evaluation- MLFLOW,Dagshub - Assesses model performance using various metrics, and logs results in tracking tools like MLFLOW or Dagshub.

## Workflows

1. Update config.yaml ->ex-  if i need to get data from api/database to fetch & update it right, so those kind of information will be updated in config.yaml . Configures the pipeline with key settings, paths, and parameters to customize behavior across stages.

2. Update schema.yaml -> we need to chcek & update the schema of the input that w are getting, whenever new test data cmes then that schema of that data needs to be validated  Defines data structure and schema requirements, enforcing rules on data format and constraints.

3. Update params.yaml -> we are gong to update the parameters & for the first three workflows we are gign to work on upto all 5 pipelines Stores hyperparameters and other tunable parameters to facilitate model adjustments without altering code.

4. Update the entity - Defines data objects or entities used in the pipeline, allowing structured data handling.

5. Update the configuration manager in src config - Manages and accesses configuration files and settings used throughout the pipeline.

6. Update the components - Modifies or adds pipeline components, each responsible for a specific task within the ML workflow.

7. Update the pipeline - Integrates all components into an end-to-end pipeline, allowing automated execution from ingestion to evaluation.validate training pipeline & batch prediction pipeline

8. Update the main.py- Orchestrates and runs the complete workflow by calling each pipeline component sequentially within a main script.