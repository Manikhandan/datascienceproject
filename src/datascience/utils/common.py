## Importing necessary modules
import os                          # Imports the 'os' module to interact with the operating system for tasks like file and directory handling.
import yaml                        # Imports 'yaml' for reading and writing YAML configuration files.
from src.datascience import logger # Imports 'logger' from 'src.datascience' for logging messages.
import json                        # Imports 'json' to handle JSON file reading and writing.
import joblib                      #create & save a model as joblib format in harddislk Imports 'joblib' to save and load binary files (efficient for large data).
from ensure import ensure_annotations # Imports 'ensure_annotations' to enforce function annotations for type checking.
from box import ConfigBox          # Imports 'ConfigBox' from 'box' to convert dictionaries to object attributes.
from pathlib import Path           # Imports 'Path' to handle file paths as objects.
from typing import Any             # Imports 'Any' from typing, allowing for flexible type annotations.
from box.exceptions import BoxValueError # Imports 'BoxValueError' to handle specific errors from ConfigBox operations.

# Define a function with enforced type annotations to read YAML files and return them as ConfigBox objects.
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input
    Raises:
        ValueError: if yaml file is empty
        e: empty file
    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        # Opens the YAML file in read mode.
        with open(path_to_yaml) as yaml_file:
            # Reads content from YAML and parses it into a dictionary.
            content = yaml.safe_load(yaml_file)
            # Logs success message upon loading.
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            # Converts dictionary to ConfigBox (allows attribute access) and returns it.
            return ConfigBox(content)
    except BoxValueError:
        # Raises a ValueError if the YAML file is empty.
        raise ValueError("yaml file is empty")
    except Exception as e:
        # Catches and re-raises any other exception.
        raise e


# Define a function with enforced annotations to create directories from a list of paths.
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    # Iterates over each directory path in the list.
    for path in path_to_directories:
        # Creates directory, ensuring no error if it already exists.
        os.makedirs(path, exist_ok=True)
        if verbose:
            # Logs a message if verbose mode is True.
            logger.info(f"created directory at: {path}")


# Define a function with annotations to save data as a JSON file.
@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    # Opens the file in write mode, creating it if it doesn't exist.
    with open(path, "w") as f:
        # Writes data to the JSON file with indentation for readability.
        json.dump(data, f, indent=4)
    # Logs that the JSON file was successfully saved.
    logger.info(f"json file saved at: {path}")


# Define a function with enforced annotations to load JSON files as ConfigBox objects.
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file
    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    # Opens the JSON file in read mode.
    with open(path) as f:
        # Reads and parses JSON data into a dictionary.
        content = json.load(f)
    # Logs success message after loading.
    logger.info(f"json file loaded succesfully from: {path}")
    # Converts dictionary to ConfigBox and returns it.
    return ConfigBox(content)


# Define a function with annotations to save data as a binary file using joblib.
@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    # Uses joblib to save data as a binary file at the specified path.
    joblib.dump(value=data, filename=path)
    # Logs success message after saving the file.
    logger.info(f"binary file saved at: {path}")


# Define a function with annotations to load binary data using joblib.
@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file
    Returns:
        Any: object stored in the file
    """
    # Uses joblib to load data from the binary file at the specified path.
    data = joblib.load(path)
    # Logs success message after loading the file.
    logger.info(f"binary file loaded from: {path}")
    # Returns the loaded data.
    return data
