from distutils.log import error
import json
import os
from os.path import dirname, join

DEFAULT_PATH_SAVE = join(dirname(dirname(__file__)), 'data', 'save.json')
DEFAULT_PATH_READ = join(dirname(dirname(__file__)), 'data', 'save.json')


# @staticmethod
def setDefaultPath(operation, path):
    """_summary_

    Args:
        operation (string): Indicates which path to update (write/read) 
        path (string): the new path to save/write, will be the new value of DEFAULT_PATH_SAVE/DEFAULT_PATH_READ

    Returns:
        string: indicates if the modification process success or not
    """
    global DEFAULT_PATH_SAVE, DEFAULT_PATH_READ
    if not os.path.exists(path):
        return "Unable to Update, Path Does Not Exist"
    elif operation == "r":
        DEFAULT_PATH_READ = path
        return "Update Read File Path Successfully"
    elif operation == "w":
        DEFAULT_PATH_SAVE = path
        return "Update Write File Path Successfully"
    else:
        return "Unable to Update, Wrong Operation"