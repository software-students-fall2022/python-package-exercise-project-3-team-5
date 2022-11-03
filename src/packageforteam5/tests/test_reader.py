import json
import os
from os.path import dirname, join
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from types import SimpleNamespace
import loader
import default_path as path
def delete_file(path):
    if os.path.exists(path):
         os.remove(path)
         
def test_init():
    p = join(dirname(dirname(dirname(__file__))), 'data', "subfolder" ,'non-save_test.json')
    delete_file(p)

def load_existing_data():
    test_init()
    path.setDefaultPath(join(dirname(dirname(dirname(__file__))), 'data', 'save_test.json'))
    quiz = loader.load("quiz")
    return quiz.sport.q1.options[0]

def load_existing_data2():
    test_init()
    path.setDefaultPath(join(dirname(dirname(dirname(__file__))), 'data', 'save_test.json'))
    value = loader.load("test")
    return value

def load_existing_data_with_overridden_file():
    test_init()
    value = loader.load("glossary", None, join(dirname(dirname(dirname(__file__))), 'data', 'save_test_2.json'))
    return value.GlossDiv.GlossList.GlossEntry.GlossDef.GlossSeeAlso[0]

def load_non_existing_data_from_existing_file():
    test_init()
    path.setDefaultPath(join(dirname(dirname(dirname(__file__))), 'data', 'save_test.json'))
    quiz = loader.load("non-exist")
    return quiz
    
def load_default_value_from_non_existing_data():
    test_init()
    path.setDefaultPath(join(dirname(dirname(dirname(__file__))), 'data', "subfolder" ,'non-save_test.json'))
    quiz = loader.load("non-exist-2", 100)
    return quiz

def load_existing_data_from_non_existing_file():
    test_init()
    quiz = loader.load("quiz", None, join(dirname(dirname(__file__)), 'data', "subfolder", 'non-save_test.json'))
    return quiz



def test_load_existing_data():
    assert load_existing_data() == "New York Bulls"
    
def test_load_existing_data2():
    assert load_existing_data2() == 5

def test_load_existing_data_with_overridden_file():
    assert load_existing_data_with_overridden_file() == "GML"
    
def test_load_non_existing_data_from_existing_file():
    assert load_non_existing_data_from_existing_file() == None
    
def test_load_default_value_from_non_existing_data():
    assert load_default_value_from_non_existing_data() == 100
    
def test_load_existing_data_from_non_existing_file():
    assert load_existing_data_from_non_existing_file() == None