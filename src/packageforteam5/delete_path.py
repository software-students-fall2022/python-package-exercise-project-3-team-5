import json
import os
from os.path import dirname, join
import default_path as path

def delete(key, default_value=None, path=path.DEFAULT_PATH_READ):
    """_summary_

    Args:
        key (string): the key in the json file to delete 
        default_value (object, optional): The default value to return if the key or the file does not exist. Defaults to None.
        path (string, optional): the path of the saved Json file to load. Defaults to DEFAULT_PATH.

    Returns:
        object: the value of the key in the json file, or the default value if the key or the file does not exist
    """
    if not os.path.exists(path):
        print("There is no such path")
        return default_value
    with open(path) as f:
        data = json.load(f)
        data.pop(key)
        print("Successfully delete: ",key)
        with open(path,'w') as file:
            file.write(json.dumps(data, indent=4))
        return data
    if(value == None):
        return default_value


    