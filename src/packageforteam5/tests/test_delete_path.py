import json
import os
from os.path import dirname, join
import sys


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import delete_path
import default_path as path

data1 = {
    "Dragonfruit": {
        "mood": "happy",
        "taste": "sweet",
        "price": "moderate"    
    },

    "Black Tea": {
        "mood": "tired",
        "taste": "bitter",
        "price": "low"    
    }
}

data2 = {
    "Irish Cold Brew": {
        "mood": "tired",
        "taste": "bitter",
        "price": "low"    
    },
 
    "Caramel Frappuccino": {
     "mood": "happy",
     "taste": "sweet",
     "price": "high"    
    },
 
    "Pink Drink": {
     "mood": "happy",
     "taste": "sour",
     "price": "moderate"    
    },
 
    "Iced Espresso": {
     "mood": "tired",
     "taste": "bitter",
     "price": "low"    
    },

    "Iced Caramel Macchiato": {
        "mood": "tired",
        "taste": "sweet",
        "price": "high"    
    }
 
 
 }

def add_file1(path):
    if os.path.exists(path):
         with open(path,'w') as file:
            file.write(json.dumps(data1, indent=4))

def add_file2(path):
    if os.path.exists(path):
         with open(path,'w') as file:
            file.write(json.dumps(data2, indent=4))
    
def init_test():
    t3 = join(dirname(dirname(dirname(__file__))), 'data', 'save_test_3.json')
    add_file1(t3)
    t4 = join(dirname(dirname(dirname(__file__))), 'data', 'save_test_4.json')
    add_file2(t4)


def delete_nonexisting_data():
    path.setDefaultPath(join(dirname(dirname(dirname(__file__))), 'data', 'save.json'),"r")
    print(delete_path.delete("test"))

def delete_existing_data1():
    init_test()
    path.setDefaultPath(join(dirname(dirname(dirname(__file__))), 'data', 'save_test_3.json'),"r")
    return delete_path.delete("Dragonfruit")

def delete_existing_data2():
    init_test()
    path.setDefaultPath(join(dirname(dirname(dirname(__file__))), 'data', 'save_test_3.json'),"r")
    return delete_path.delete("Black Tea")

def delete_nonexisting_data2():
    path.setDefaultPath(join(dirname(dirname(dirname(__file__))), 'data', 'save_test_4.json'),"r")
    return delete_path.delete("test")

def delete_existing_data3():
    init_test()
    path.setDefaultPath(join(dirname(dirname(dirname(__file__))), 'data', 'save_test_4.json'),"r")
    return delete_path.delete("Pink Drink")

def test_delete_nonexisting_data():
    assert delete_nonexisting_data() == None

def test_delete_existing_data1():
    assert delete_existing_data1().mood == "happy"
def test_delete_exting_isting_data2():
    assert delete_existing_data2().taste == "bitter"  

def test_delete_nonexisting_data2():
    assert delete_nonexisting_data2() == None 

def test_delete_existing_data3():
    ret = delete_existing_data3() 

    assert ret.price == "moderate"
    
