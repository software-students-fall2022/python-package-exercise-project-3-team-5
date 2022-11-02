from genericpath import samefile
import json
import os
from os.path import dirname, join
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import loader
import default_path

    

def set_default_path_read():
    set_path = default_path.setDefaultPath(join(dirname(dirname(dirname(__file__))), 'data', 'test_path_read.json'), "r")
    path = default_path.DEFAULT_PATH_READ
    set_back = default_path.setDefaultPath(join(dirname(dirname(dirname(__file__))), 'data', 'save.json'), "r")
    return set_path, path, set_back

def set_default_path_write():
    set_path = default_path.setDefaultPath(join(dirname(dirname(dirname(__file__))), 'data', 'test_path_save.json'), "w")
    path = default_path.DEFAULT_PATH_SAVE
    set_back = default_path.setDefaultPath(join(dirname(dirname(dirname(__file__))), 'data', 'save.json'), "w")
    return set_path, path, set_back

def set_default_path_both():
    set_path = default_path.setDefaultPath(join(dirname(dirname(dirname(__file__))), 'data', 'test_path_save_read.json'), "wr")
    path_save = default_path.DEFAULT_PATH_SAVE
    path_read = default_path.DEFAULT_PATH_READ
    set_back = default_path.setDefaultPath(join(dirname(dirname(dirname(__file__))), 'data', 'save.json'), "wr")
    return set_path, path_save, path_read, set_back

def set_default_path_no_operation():
    set_path = default_path.setDefaultPath(join(dirname(dirname(dirname(__file__))), 'data', 'test_path_no_operation.json'))
    path_save = default_path.DEFAULT_PATH_SAVE
    path_read = default_path.DEFAULT_PATH_READ
    set_back = default_path.setDefaultPath(join(dirname(dirname(dirname(__file__))), 'data', 'save.json'), "wr")
    return set_path, path_save, path_read, set_back


def test_set_default_path_read():
    value1, value2, value3 = set_default_path_read()
    areSame = samefile(value2, join(dirname(dirname(dirname(__file__))), 'data', 'test_path_read.json'))
    assert value1 == 'Update Read File Path Successfully' and areSame == True and value3 == 'Update Read File Path Successfully'

def test_set_default_path_write():
    value1, value2, value3 = set_default_path_write()
    areSame = samefile(value2, join(dirname(dirname(dirname(__file__))), 'data', 'test_path_save.json'))
    assert value1 == 'Update Write File Path Successfully' and areSame == True and value3 == 'Update Write File Path Successfully'

def test_set_default_path_both():
    value1, value2, value3, value4 = set_default_path_both()
    save_areSame = samefile(value2, join(dirname(dirname(dirname(__file__))), 'data', 'test_path_save_read.json'))
    read_areSame = samefile(value3, join(dirname(dirname(dirname(__file__))), 'data', 'test_path_save_read.json'))

    assert value1 == 'Update Read and Write File Path Successfully' and save_areSame == True and read_areSame == True and value4 == 'Update Read and Write File Path Successfully'

def test_set_default_path_no_operation():
    value1, value2, value3, value4 = set_default_path_no_operation()
    save_areSame = samefile(value2, join(dirname(dirname(dirname(__file__))), 'data', 'test_path_no_operation.json'))
    read_areSame = samefile(value3, join(dirname(dirname(dirname(__file__))), 'data', 'test_path_no_operation.json'))

    assert value1 == 'Update Read and Write File Path Successfully' and save_areSame == True and read_areSame == True and value4 == 'Update Read and Write File Path Successfully'

