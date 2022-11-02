from distutils.log import error
import json
import os
from os.path import dirname, join

DEFAULT_PATH_SAVE = join(dirname(dirname(__file__)), 'data', 'save.json')
DEFAULT_PATH_READ = join(dirname(dirname(__file__)), 'data', 'save.json')


# @staticmethod
def setDefaultPath(path, operation="wr"):
    """_summary_

    Args:
        operation (string): Indicates which path to update (write/read) 
        path (string): the new path to save/write, will be the new value of DEFAULT_PATH_SAVE/DEFAULT_PATH_READ

    Returns:
        string: indicates if the modification process success or not
    """
    global DEFAULT_PATH_SAVE, DEFAULT_PATH_READ
    if not os.path.exists(path):
        try:
            dir = dirname(path)
            print("dir=", dir)
            os.makedirs(dir, exist_ok=True)
            fp = open(path, 'w')
            fp.write('{}')
            fp.close()
        except:
            return error

    if operation == "r":
        DEFAULT_PATH_READ = path
        return "Update Read File Path Successfully"
    elif operation == "w":
        DEFAULT_PATH_SAVE = path
        return "Update Write File Path Successfully"
    elif operation == "wr":
        DEFAULT_PATH_READ= path
        DEFAULT_PATH_SAVE = path
        return "Update Read and Write File Path Successfully"
    else:
        return "Unable to Update, Wrong Operation"