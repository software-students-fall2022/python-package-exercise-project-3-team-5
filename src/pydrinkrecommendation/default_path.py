from distutils.log import error
import os
from os.path import dirname, join

DEFAULT_PATH = join(dirname(dirname(__file__)), 'data', 'save.json')


def setDefaultPath(path):
    """_summary_

    Args:
        path (string): the new path to save/write, will be the new value of DEFAULT_PATH_SAVE/DEFAULT_PATH_READ

    Returns:
        string/error: indicates if the modification process success or not
    """
    global DEFAULT_PATH
    if not os.path.exists(path):
        try:
            dir = dirname(path)
            os.makedirs(dir, exist_ok=True)
            fp = open(path, 'w')
            fp.write('{}')
            fp.close()
        except:
            return error

    DEFAULT_PATH = path
    return "Update Read and Write File Path Successfully"
