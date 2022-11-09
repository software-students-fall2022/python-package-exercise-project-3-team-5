import json
import os
from os.path import dirname, join
import sys


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import delete_path
import default_path as path
from  drinks import Mood, Taste, Price, Drink
data1 = {
    "Irish Cold Brew": {
        "mood": 0,
        "taste": 0,
        "price": 0
    },
    "Caramel Frappuccino": {
        "mood": 1,
        "taste": 1,
        "price": 2
    },
    "Iced Espresso": {
        "mood": 0,
        "taste": 0,
        "price": 1
    },
    "Iced Caramel Macchiato": {
        "mood": 1,
        "taste": 1,
        "price": 1
    }
}

data2 = {
    "Irish Cold Brew": {
        "mood": 0,
        "taste": 0,
        "price": 0
    },
    "Caramel Frappuccino": {
        "mood": 1,
        "taste": 1,
        "price": 2
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
    path.setDefaultPath(join(dirname(dirname(dirname(__file__))), 'data', 'save.json'))
    print(delete_path.delete("test"))

def delete_existing_data1():
    init_test()
    path.setDefaultPath(join(dirname(dirname(dirname(__file__))), 'data', 'save_test_3.json'))
    return delete_path.delete("Irish Cold Brew")

def delete_existing_data2():
    init_test()
    path.setDefaultPath(join(dirname(dirname(dirname(__file__))), 'data', 'save_test_3.json'))
    return delete_path.delete("Iced Caramel Macchiato")

def delete_nonexisting_data2():
    path.setDefaultPath(join(dirname(dirname(dirname(__file__))), 'data', 'save_test_4.json'))
    return delete_path.delete("test")

def delete_existing_data3():
    init_test()
    path.setDefaultPath(join(dirname(dirname(dirname(__file__))), 'data', 'save_test_4.json'))
    return delete_path.delete("Caramel Frappuccino")

def test_delete_nonexisting_data():
    assert delete_nonexisting_data() == None

def test_delete_existing_data1():
    assert delete_existing_data1().mood == Mood.Tired
def test_delete_exting_isting_data2():
    assert delete_existing_data2().taste == Taste.Sweet

def test_delete_nonexisting_data2():
    assert delete_nonexisting_data2() == None 

def test_delete_existing_data3():
    ret = delete_existing_data3() 

    assert ret.price == Price.High
    
