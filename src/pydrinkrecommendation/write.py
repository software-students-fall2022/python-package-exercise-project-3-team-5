import json
import os
from os.path import dirname, join
import default_path as path
from distutils.log import error
from loader import NestedNamespace

def write(key, value):
    """_summary_
    Args:
        key (string): the key to add to json file 
        value (string, number): the value associated with given key to write to given json file
        path (string, optional): the path of the saved Json file to use. Defaults to DEFAULT_PATH.
    Returns:
        object: 0 if unsuccessful, 1 if successful
    """
    op_path = path.DEFAULT_PATH
    if not os.path.exists(op_path):
        try:
            dir = dirname(op_path)
            print("dir=", dir)
            os.makedirs(dir, exist_ok=True)
            fp = open(op_path, 'w')
            fp.write('{}')
            fp.close()
        except:
            return error
    if(isinstance(value, NestedNamespace)):
        value = value.to_dictionary()
        
    with open(op_path) as f:
        data = json.load(f)
        data.update({key: value})
    with open(op_path, "w") as outputFile:
        json.dump(data, outputFile, indent=4)
        print("Key value pair added!")
        return 1