import json
import os
from os.path import dirname, join
import sys



sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import delete_path
import default_path as path

def delete_existing_data():
    path.setDefaultPath("w", join(dirname(dirname(dirname(__file__))), 'data', 'save_test.json'))
    print(delete_path.delete("test"))


def test_load_existing_data():
    assert delete_existing_data() == None