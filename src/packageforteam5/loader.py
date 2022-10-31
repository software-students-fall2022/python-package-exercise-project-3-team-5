import json
import os
from os.path import dirname, join
import default_path as path
from types import SimpleNamespace
#reference: https://stackoverflow.com/questions/16279212/how-to-use-dot-notation-for-dict-in-python
class NestedNamespace(SimpleNamespace):
    def __init__(self, dictionary, **kwargs):
        super().__init__(**kwargs)
        
        for key, value in dictionary.items():
            if isinstance(value, dict):
                self.__setattr__(key, NestedNamespace(value))
            else:
                self.__setattr__(key, value)


#@staticmethod
def load(key, default_value=None, path=path.DEFAULT_PATH_READ):
    """_summary_

    Args:
        key (string): the key in the json file to load
        default_value (object, optional): The default value to return if the key or the file does not exist. Defaults to None.
        path (string, optional): the path of the saved Json file to load. Defaults to DEFAULT_PATH.

    Returns:
        object: the value of the key in the json file, or the default value if the key or the file does not exist. Use dot notation "." to access nested values.
    """
    if not os.path.exists(path):
        return default_value
    with open(path) as f:
        data = json.load(f)
    value = data.get(key, default_value)
    if(value == None):
        return default_value
    if(not isinstance(value, dict)):
            return value
    return NestedNamespace(value)