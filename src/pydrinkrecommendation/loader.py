import json
import os
from os.path import dirname, join
import default_path as path
from types import SimpleNamespace
import warnings
#reference: https://stackoverflow.com/questions/16279212/how-to-use-dot-notation-for-dict-in-python
class NestedNamespace(SimpleNamespace):
    def __init__(self, dictionary, **kwargs):
        super().__init__(**kwargs)
        
        for key, value in dictionary.items():
            if isinstance(value, dict):
                self.__setattr__(key, NestedNamespace(value))
            else:
                self.__setattr__(key, value)
    
    def to_dictionary(self):
        # self.__dict__.items() can be either NestedNamespace or other types. 
        return {key: value.to_dictionary() if isinstance(value, NestedNamespace) else value for key, value in self.__dict__.items()}

    

#@staticmethod
def load(key, default_value=None, overridden_path=None):
    """_summary_

    Args:
        key (string): the key in the json file to load
        default_value (object, optional): The default value to return if the key or the file does not exist. Defaults to None.
        path (string, optional): the path of the saved Json file to load. Defaults to DEFAULT_PATH.

    Returns:
        object: the value of the key in the json file, or the default value if the key or the file does not exist. Use dot notation "." to access nested values.
    """
    if(overridden_path == None or overridden_path == ""):
        overridden_path = path.DEFAULT_PATH_READ
    
    if not os.path.exists(overridden_path):
        warnings.warn('I got lost in the woods and could not find the file! I will fallback to the default value!')
        return default_value
    with open(overridden_path) as f:
        try:
            data = json.load(f)
        except:
            return default_value
    value = data.get(key, default_value)
    if(value == None):
        warnings.warn('Where is the key? I will fallback to the default value!')
        return default_value
    if(not isinstance(value, dict)):
            return value
    return NestedNamespace(value)