import json
import os
from os.path import dirname, join
import default_path as path
from distutils.log import error

def write(key, value, overridden_path=None):
    """_summary_
    Args:
        key (string): the key to add to json file 
        value (string, number): the value associated with given key to write to given json file
        path (string, optional): the path of the saved Json file to use. Defaults to DEFAULT_PATH.
    Returns:
        object: 0 if unsuccessful, 1 if successful
    """
    
    if(overridden_path == None or overridden_path == ""):
        overridden_path = path.DEFAULT_PATH_SAVE
    
    dir = '\\'.join(overridden_path.split('\\')[0:-1])
    if not os.path.exists(dir):
        try:
            os.makedirs(dir)
            fp = open(overridden_path, 'w')
            fp.write('{}')
            fp.close()
        except:
            return error
    
    if not os.path.exists(overridden_path):
        try:
            fp = open(overridden_path, 'w')
            fp.write('{}')
            fp.close()
        except:
            return error
    
    with open(overridden_path) as f:
        data = json.load(f)
        data.update({key: value})
    with open(overridden_path, "w") as outputFile:
        json.dump(data, outputFile, indent=4)
        print("Key value pair added!")
        return 1