import os
from os.path import dirname, join
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import write
import loader
import default_path as path
from drinks import Drink
import delete_path

def delete_file(path):
    if os.path.exists(path):
         os.remove(path)
    
def init_test():
    t1 = join(dirname(dirname(dirname(__file__))), 'data', 'write_test_1.json')
    delete_file(t1)
    t2 = join(dirname(dirname(dirname(__file__))), 'data', 'write_test_2.json')
    path.setDefaultPath(t2)
    delete_path.delete("test drink 2")

def write_drink_to_non_existing_file():
    init_test()
    path.setDefaultPath(join(dirname(dirname(dirname(__file__))), 'data', 'write_test_1.json'))
    testDrink1 = Drink("test drink 1", 0, 1, 2)
    write.write(testDrink1)
    testDrink1Properties = loader.load("test drink 1")
    return testDrink1Properties

def write_new_drink_to_existing_file():
    init_test()
    path.setDefaultPath(join(dirname(dirname(dirname(__file__))), 'data', 'write_test_2.json'))
    testDrink2 = Drink("test drink 2", 1, 0, 1)
    write.write(testDrink2)
    testDrink2Properties = loader.load("test drink 2")
    return testDrink2Properties

def write_existing_drink_to_existing_file():
    path.setDefaultPath(join(dirname(dirname(dirname(__file__))), 'data', 'write_test_3.json'))
    testDrink3 = Drink("test drink 3", 1, 1, 1)
    write.write(testDrink3)
    updatedTestDrink3 = Drink("test drink 3", 1, 0, 1)
    write.write(updatedTestDrink3)
    testDrink3Properties = loader.load("test drink 3")
    return testDrink3Properties

def test_write_drink_to_non_existing_file():
    dict_test1 = write_drink_to_non_existing_file()
    
    #mood, taste, price = dict_test1['mood'], dict_test1['taste'], dict_test1['price']
    assert dict_test1.mood == 0 and dict_test1.taste == 1 and dict_test1.price == 2

def test_write_new_drink_to_existing_file():
    dict_test2 = write_new_drink_to_existing_file().to_dictionary()
    mood, taste, price = dict_test2['mood'], dict_test2['taste'], dict_test2['price']
    assert mood == 1 and taste == 0 and price == 1

def test_existing_new_drink_to_existing_file():
    dict_test3 = write_existing_drink_to_existing_file().to_dictionary()
    mood, taste, price = dict_test3['mood'], dict_test3['taste'], dict_test3['price']
    assert mood == 1 and taste == 0 and price == 1