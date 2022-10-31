import json
import os
from os.path import dirname, join
import default_path as path

def write(key, value, default_value = None, path=path.DEFAULT_PATH_READ):
    """_summary_
    Args:
        key (string): the key to add to json file 
        value (string, number): the value associated with given key to write to given json file
        path (string, optional): the path of the saved Json file to use. Defaults to DEFAULT_PATH.
    Returns:
        object: 0 if unsuccessful, 1 if successful
    """
    if not os.path.exists(path):
        print("There is no such path")
        return 0
    with open(path) as f:
        data = json.load(f)
        data.update({key: value})
    with open(path, "w") as outputFile:
        json.dump(data, outputFile)
        print("Key value pair added!")
        return 1