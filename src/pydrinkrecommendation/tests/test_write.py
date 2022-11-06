import json
import os
from os.path import dirname, join
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import write
import loader
from loader import NestedNamespace
import default_path as path
import delete_path

def delete_file(path):
    if os.path.exists(path):
         os.remove(path)
    
def init_test():
    t3 = join(dirname(dirname(dirname(__file__))), 'data', 'write_test_3.json')
    delete_file(t3)
    t4 = join(dirname(dirname(dirname(__file__))), 'data', 'write_test_4.json')
    delete_file(t4)
    t2 = join(dirname(dirname(dirname(__file__))), 'data', 'write_test_2.json')
    delete_path.delete("new value")
    t1 = join(dirname(dirname(dirname(__file__))), 'data', 'write_test.json')
    write.write("new value", 1, t1)
    write.write("quiz", {"sport":{"q1":{"question":"What is the capital of France?","options":["Paris","London","Berlin","Madrid"],"answer":"Paris"}}}, t1)
    
def write_valid_data():
    init_test()
    path.setDefaultPath(join(dirname(dirname(dirname(__file__))), 'data', 'write_test.json'))
    write.write("new value", 15)
    newKey = loader.load("new value")
    return newKey

def write_valid_data_with_existing_overridden_file():
    init_test()
    p = join(dirname(dirname(dirname(__file__))), 'data', 'write_test_2.json')
    write.write("new value", 10, p)
    newKey = loader.load("new value", None, p)
    return newKey

def write_nested_namespace():
    init_test()
    path.setDefaultPath(join(dirname(dirname(dirname(__file__))), 'data', 'write_test.json'))
    value = loader.load("quiz")
    value.sport.q1.question = "New Question"
    write.write("quiz", value)
    return loader.load("quiz").sport.q1.question
    
def write_valid_data_with_nonexisting_default_file():
    init_test()
    path.setDefaultPath(join(dirname(dirname(dirname(__file__))), 'data', 'write_test_3.json'))
    write.write("new value", 10)
    newKey = loader.load("new value")
    return newKey

def write_valid_data_with_nonexisting_overridden_file():
    init_test()
    p = join(dirname(dirname(dirname(__file__))), 'data', 'write_test_4.json')
    write.write("new value", 10, p)
    newKey = loader.load("new value", None, p)
    return newKey



'''  
def load_default_value_from_non_existing_data():
   
    path.setDefaultPath("r", join(dirname(dirname(__file__)), 'data', 'non-save_test.json'))
    quiz = loader.load("non-exist-2", 100)
    return quiz

def load_existing_data_from_non_existing_file():
    quiz = loader.load("quiz", None, join(dirname(dirname(__file__)), 'data', 'non-save_test.json'))
    return quiz
'''


def test_write_valid_data():
    assert write_valid_data() == 15
    
def test_write_valid_data_with_existing_overridden_file():
    assert write_valid_data_with_existing_overridden_file() == 10

def test_write_nested_namespace():
    assert write_nested_namespace() == "New Question"
  
def test_write_valid_data_with_nonexisting_default_file():
    assert write_valid_data_with_nonexisting_default_file() == 10
    
def test_write_valid_data_with_nonexisting_overridden_file():
    assert write_valid_data_with_nonexisting_overridden_file() == 10
'''    
def test_load_non_existing_data_from_existing_file():
    assert load_non_existing_data_from_existing_file() == None
    
def test_load_default_value_from_non_existing_data():
    assert load_default_value_from_non_existing_data() == 100
    
def test_load_existing_data_from_non_existing_file():
    assert load_existing_data_from_non_existing_file() == None
'''