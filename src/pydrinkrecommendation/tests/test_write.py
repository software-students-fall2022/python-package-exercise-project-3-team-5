import os
from os.path import dirname, join
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import write
import loader
import default_path as path

def delete_file(path):
    if os.path.exists(path):
         os.remove(path)
    
def init_test():
    t1 = join(dirname(dirname(dirname(__file__))), 'data', 'write_test_1.json')
    delete_file(t1)
    t2 = join(dirname(dirname(dirname(__file__))), 'data', 'write_test_2.json')
    delete_file(t2)
    # delete_path.delete("new value")
    # test_file_path = join(dirname(dirname(dirname(__file__))), 'data', 'write_test.json')
    
    # write.write("test drink", {"mood": 1, "taste": 1, "price": 1})

def write_non_exist_data():
    init_test()
    path.setDefaultPath(join(dirname(dirname(dirname(__file__))), 'data', 'write_test_1.json'))
    write.write("test drink 2", {"mood": 1, "taste": 1, "price": 1})
    newKey = loader.load("test drink 2")
    return newKey

def write_nested_namespace():
    init_test()
    path.setDefaultPath(join(dirname(dirname(dirname(__file__))), 'data', 'write_test_2.json'))
    write.write("test drink", {"mood": 1, "taste": 1, "price": 1})
    value = loader.load("test drink")
    value.mood = 0
    write.write("test drink", value)
    return loader.load("test drink").mood
    



'''  
def load_default_value_from_non_existing_data():
   
    path.setDefaultPath("r", join(dirname(dirname(__file__)), 'data', 'non-save_test.json'))
    quiz = loader.load("non-exist-2", 100)
    return quiz

def load_existing_data_from_non_existing_file():
    quiz = loader.load("quiz", None, join(dirname(dirname(__file__)), 'data', 'non-save_test.json'))
    return quiz
'''


def test_write_non_exist_data():
    dict_test = write_non_exist_data().to_dictionary()
    mood, taste, price = dict_test['mood'], dict_test['taste'], dict_test['price']
    assert mood == 1 and taste == 1 and price == 1
test_write_non_exist_data()
def test_write_nested_namespace():
    assert write_nested_namespace() == 0
  
'''    
def test_load_non_existing_data_from_existing_file():
    assert load_non_existing_data_from_existing_file() == None
    
def test_load_default_value_from_non_existing_data():
    assert load_default_value_from_non_existing_data() == 100
    
def test_load_existing_data_from_non_existing_file():
    assert load_existing_data_from_non_existing_file() == None
'''