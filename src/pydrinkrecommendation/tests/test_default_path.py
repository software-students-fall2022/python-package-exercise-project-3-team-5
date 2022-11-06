from genericpath import samefile
import os
from os.path import dirname, join
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import default_path


def delete_file(path):
    if os.path.exists(path):
            os.remove(path)
            
def init_test():
    p1 = join(dirname(dirname(dirname(__file__))), 'data', 'test_set_path.json')
    delete_file(p1)

def set_default_path():
    init_test()
    set_path = default_path.setDefaultPath(join(dirname(dirname(dirname(__file__))), 'data', 'test_set_path.json'))
    path = default_path.DEFAULT_PATH
    set_back = default_path.setDefaultPath(join(dirname(dirname(dirname(__file__))), 'data', 'save.json'))
    return set_path, path, set_back

def test_set_default_path():
    value1, value2, value3 = set_default_path()
    areSame = samefile(value2, join(dirname(dirname(dirname(__file__))), 'data', 'test_set_path.json'))
    assert value1 == 'Update Read and Write File Path Successfully' and areSame == True and value3 == 'Update Read and Write File Path Successfully'

