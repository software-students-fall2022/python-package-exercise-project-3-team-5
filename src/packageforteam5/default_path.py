from distutils.log import error
import json
import os
from os.path import dirname, join

DEFAULT_PATH_SAVE = join(dirname(dirname(__file__)), 'data', 'save.json')
DEFAULT_DIR_READ = join(dirname(dirname(__file__)), 'data', 'save.json')


@staticmethod
def setDefaultPath(operation, path):
    """_summary_

    Args:
        key (string): the key in the json file to load
        default_value (object, optional): The default value to return if the key or the file does not exist. Defaults to None.
        path (string, optional): the path of the saved Json file to load. Defaults to DEFAULT_PATH.

    Returns:
        object: the value of the key in the json file, or the default value if the key or the file does not exist
    """
    global DEFAULT_PATH_SAVE, DEFAULT_DIR_READ
    if not os.path.exists(path):
        return error
    elif operation == "r":
        DEFAULT_DIR_READ = path
    elif operation == "w":
        DEFAULT_PATH_SAVE = path
    else:
        return error