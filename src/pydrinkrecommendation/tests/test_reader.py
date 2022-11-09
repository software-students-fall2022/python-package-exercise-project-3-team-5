import json
import os
from os.path import dirname, join
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from types import SimpleNamespace

import recommendation
import default_path as path
from drinks import Mood, Taste, Price

def delete_file(path):
    if os.path.exists(path):
         os.remove(path)
         
def test_init():
    p = join(dirname(dirname(dirname(__file__))), 'data', "subfolder" ,'non-save_test.json')
    delete_file(p)

def load_existing_data():
    test_init()
    path.setDefaultPath(join(dirname(dirname(dirname(__file__))), 'data', 'save_test.json'))
    drink = recommendation.get_recommendation(Mood.Happy, Taste.Sweet, Price.High)
    return drink

def load_existing_data2():
    test_init()
    path.setDefaultPath(join(dirname(dirname(dirname(__file__))), 'data', 'save_test.json'))
    drink = recommendation.get_recommendation(Mood.Happy, Taste.Sweet, Price.Medium)
    return drink

def load_data_with_None():
    test_init()
    path.setDefaultPath(join(dirname(dirname(dirname(__file__))), 'data', 'save_test.json'))
    drink = recommendation.get_recommendation(None, None, None)
    return drink

def load_non_existing_drink():
    test_init()
    path.setDefaultPath(join(dirname(dirname(dirname(__file__))), 'data', 'save_test_2.json'))
    drink = recommendation.get_recommendation(Mood.Tired, Taste.Sweet, Price.Medium)
    return drink

def load_empty_json():
    test_init()
    path.setDefaultPath(join(dirname(dirname(dirname(__file__))), 'data', 'empty_json.json'))
    drink = recommendation.get_recommendation(Mood.Tired, Taste.Sweet, Price.Medium)
    return drink


def test_load_existing_data():
    assert load_existing_data().price == Price.High
    
def test_load_non_existing_drink():
    d = load_non_existing_drink()
    assert d!=None

def test_load_existing_data2():
    assert load_existing_data2().name == "Iced Caramel Macchiato"

def test_load_data_with_none():
    assert load_data_with_None() != None
    
def test_load_empty_json():
    assert load_empty_json() == None