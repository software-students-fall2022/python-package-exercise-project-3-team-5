import json
import os
from os.path import dirname, join
import default_path as path

def delete(key, default_value=None, overridden_path=None):
    """_summary_

    Args:
        key (string): the key in the json file to delete 
        default_value (object, optional): The default value to return if the key or the file does not exist. Defaults to None.
        path (string, optional): the path of the saved Json file to load. Defaults to DEFAULT_PATH.

    Returns:
        object: the value of the key in the json file, or the default value if the key or the file does not exist
    """
    if (overridden_path == None or overridden_path == ""):
        overridden_path = path.DEFAULT_PATH_READ
    print("Default", overridden_path)
    print("Default2", path.DEFAULT_PATH_READ)
    if not os.path.exists(overridden_path):
        return default_value
    with open(overridden_path) as f:
        data = json.load(f)
        keylist = data.keys()

        for k in keylist:
            if key == k:
                data.pop(key)
                print("Successfully delete: ",key)
                with open(overridden_path,'w') as file:
                    file.write(json.dumps(data, indent=4))
                    print(data)
                    return data
        print("Error! No such key exists.")
        return default_value
    


    