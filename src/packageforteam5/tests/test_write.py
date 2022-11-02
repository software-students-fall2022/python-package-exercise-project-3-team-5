import json
import os
from os.path import dirname, join
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from types import SimpleNamespace
import write
import loader
import default_path as path
    

def write_valid_data():
    path.setDefaultPath("w", join(dirname(dirname(dirname(__file__))), 'data', 'write_test.json'))
    write.write("new value", 10)
    newKey = loader.load("new value")
    print(newKey)
    return newKey

def write_valid_data_with_existing_overridden_file():
    write.write("new value", 10, None, join(dirname(dirname(dirname(__file__))), 'data', 'write_test_2.json'))
    newKey = loader.load("new value")
    return newKey

def write_valid_data_with_nonexisting_default_file():
    path.setDefaultPath("w", join(dirname(dirname(dirname(__file__))), 'data', 'write_test_3.json'))
    write.write("new value", 10)
    newKey = loader.load("new value")
    return newKey

def write_valid_data_with_nonexisting_overridden_file():
    write.write("new value", 10, None, join(dirname(dirname(dirname(__file__))), 'data', 'write_test_4.json'))
    newKey = loader.load("new value")
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
    assert write_valid_data() == 10
    
def test_write_valid_data_with_existing_overridden_file():
    assert write_valid_data_with_existing_overridden_file() == 10

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