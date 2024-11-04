## template.py- bcuz i need to have a generic project struture

## Importing necessary modules
import os                   # Provides functions to interact with the operating system (e.g., creating directories).
from pathlib import Path    # Simplifies working with file paths in a cross-platform way.
import logging              # For tracking events and debugging information.

## Setting up basic logging configuration
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')
# Configures logging to display informational messages with a timestamp, which helps in tracking the program’s progress.

## Defining the main project name
project_name = "datascience"
# Variable to store the root folder name for the project, which is used to create file paths dynamically.

## Defining the list of files and folders to create in the project structure
list_of_files = [
    ".github/workflows/.gitkeep",                 # Placeholder file for GitHub workflows (used in GitHub Actions).
    f"src/{project_name}/__init__.py",            # Initializes the main project package.
    f"src/{project_name}/components/__init__.py", # Initializes a 'components' subpackage. init.py -> it will create that folder as package & we can use it in anywhere in this whole package - components- > we can write data injestin, data transformation, training, experiments
    f"src/{project_name}/utils/__init__.py",      # Initializes a 'utils' subpackage. utils- generic functionalites to mention 
    f"src/{project_name}/utils/common.py",        # Placeholder for common utility functions.
    f"src/{project_name}/config/__init__.py",     # Initializes a 'config' subpackage.
    f"src/{project_name}/config/configuration.py",# Placeholder for configuration-related code.
    f"src/{project_name}/pipeline/__init__.py",   # Initializes a 'pipeline' subpackage. pipeline- we need to create training & prediction pipeline
    f"src/{project_name}/entity/__init__.py",     # Initializes an 'entity' subpackage.
    f"src/{project_name}/entity/config_entity.py",# Placeholder for configuration entity definitions.
    f"src/{project_name}/constants/__init__.py",  # Initializes a 'constants' subpackage.
    "config/config.yaml",                         # Placeholder for main configuration file in YAML format.
    "params.yaml",                                # Placeholder for hyperparameters/settings in YAML format.
    "schema.yaml",                                # Placeholder for a data schema in YAML format.
    "main.py",                                    # Placeholder for the main Python script.
    "Dockerfile",                                 # Placeholder for Docker configuration file.
    "setup.py",                                   # Placeholder for setup configuration file for packaging.
    "research/research.ipynb",                    # Placeholder for research notebook.
    "templates/index.html",                       # Placeholder for HTML template.
    "app.py"                                      # Placeholder for the application’s entry point.
]

## Creating each directory and file as per the list_of_files structure
for filepath in list_of_files:
    filepath = Path(filepath)          # Convert each path string to a Path object, making it easier to work with.
    filedir, filename = os.path.split(filepath) # Split the path into directory and file name.

    ## Check if the directory for the file needs to be created
    if filedir != "":                  # If the file has a directory path (not in root).
        os.makedirs(filedir, exist_ok=True)    # Create directory if it doesn't exist.
        logging.info(f"Creating directory {filedir} for the file: {filename}")

    ## Check if the file already exists or is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        # If the file doesn't exist or is empty, create it as an empty file.
        with open(filepath, "w") as f: # Open the file in write mode to create it.
            pass                       # Pass statement to create the empty file without adding content.
        logging.info(f"Creating empty file: {filepath}") # Log the creation of the file.
    else:
        logging.info(f"{filename} already exists") # If file exists and has content, log that it’s already created.
