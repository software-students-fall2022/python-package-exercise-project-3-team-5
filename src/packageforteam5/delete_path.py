import json
import os
from os.path import dirname, join
import default_path as path
import warnings
from loader import NestedNamespace


               
def delete(key, overridden_path=None):
    """_summary_

    Args:
        key (string): the key in the json file to delete 
       
        path (string, optional): the path of the saved Json file to load. Defaults to DEFAULT_PATH.

    Returns:
        object: the value of the key in the json file, or none if the key or the file does not exist
    """
    if (overridden_path == None or overridden_path == ""):
        overridden_path = path.DEFAULT_PATH_READ
    print("Default", overridden_path)
    print("Default2", path.DEFAULT_PATH_READ)
    if not os.path.exists(overridden_path):
        return None
    with open(overridden_path) as f:
        try:
            data = json.load(f)
        except:
            return None
        keylist = data.keys()
        value = data.get(key, None)
        for k in keylist:
            if key == k:
                data.pop(key)
                print("Successfully delete: ",key)
                with open(overridden_path,'w') as file:
                    file.write(json.dumps(data, indent=4))
                    
                if(value == None):
                     return None
                if(not isinstance(value, dict)):
                        return value
                return NestedNamespace(value)
        warnings.warn("Error! No such key exists.")
        return None
    


    