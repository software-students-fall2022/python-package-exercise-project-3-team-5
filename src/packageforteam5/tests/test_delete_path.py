import json
import os
from os.path import dirname, join
import sys



sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import delete_path
import default_path as path

def delete_nonexisting_data():
    path.setDefaultPath("r", join(dirname(dirname(dirname(__file__))), 'data', 'save.json'))
    print(delete_path.delete("test"))

def delete_existing_data1():
    path.setDefaultPath("r", join(dirname(dirname(dirname(__file__))), 'data', 'save_test.json'))
    return delete_path.delete("quiz")

def delete_existing_data2():
    path.setDefaultPath("r", join(dirname(dirname(dirname(__file__))), 'data', 'save_test.json'))
    return delete_path.delete("test")

def delete_nonexisting_data2():
    path.setDefaultPath("r", join(dirname(dirname(dirname(__file__))), 'data', 'save_test_2.json'))
    return delete_path.delete("test")

def delete_existing_data3():
    path.setDefaultPath("r", join(dirname(dirname(dirname(__file__))), 'data', 'save_test_2.json'))
    return delete_path.delete("glossary")

def test_delete_nonexisting_data():
    assert delete_nonexisting_data() == None

def test_delete_existing_data1():
    assert delete_existing_data1() == {"test" : 5}

def test_delete_existing_data2():
    assert delete_existing_data2() == {}  

def test_delete_nonexisting_data2():
    assert delete_nonexisting_data2() == None 

def test_delete_existing_data3():
    assert delete_existing_data3() == {}  