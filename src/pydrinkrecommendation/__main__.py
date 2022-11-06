import loader
import default_path
import delete_path
import os
from os.path import dirname, join


def main():
  default_path.setDefaultPath(join(dirname(dirname(__file__)), 'data', 'save.json'))
  
  return 0
  
if __name__ == '__main__':
    main()
