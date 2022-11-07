import json
import os
from os.path import dirname, join
import default_path as path
from distutils.log import error
from loader import NestedNamespace
from  drinks import Drink

def write(drink: Drink):
    """_summary_
    Args:
        drink: a Drink object that contains a drink name, as well as the drink's properties (mood, taste, price)
    Returns:
        None
    """
    op_path = path.DEFAULT_PATH
    if not os.path.exists(op_path):
        try:
            dir = dirname(op_path)
            #print("dir=", dir)
            os.makedirs(dir, exist_ok=True)
            fp = open(op_path, 'w')
            fp.write('{}')
            fp.close()
        except:
            return error
        
    with open(op_path) as f:
        data = json.load(f)
        data.update({drink.name: {"mood": drink.mood, "taste": drink.taste, "price": drink.price}})
        print(data)
    with open(op_path, "w") as outputFile:
        json.dump(data, outputFile, indent=4)
        print("Key value pair added!")