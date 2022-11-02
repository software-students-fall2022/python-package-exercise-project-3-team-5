import wisdom
import loader
import default_path
import delete_path
import os
from os.path import dirname, join


def main():
  line = wisdom.get()
  print(line)
  print(default_path.DEFAULT_PATH_READ, default_path.DEFAULT_PATH_SAVE)
  if not os.path.exists(os.path.dirname(default_path.DEFAULT_PATH_READ)):
      os.makedirs(os.path.dirname(default_path.DEFAULT_PATH_READ))

  print(loader.load("quiz").sport.q1.options[0])
  print(loader.load("test"))
  print(loader.load("notexist", "default"))

  print(default_path.setDefaultPath(join(dirname(dirname(__file__)), 'data', 'test.json'), "r"))
  print(default_path.setDefaultPath(join(dirname(dirname(__file__)), 'data', 'test.json'), "w"))
  print(default_path.setDefaultPath(join(dirname(dirname(__file__)), 'data', 'test1.json'), "r"))
  print(default_path.setDefaultPath(join(dirname(dirname(__file__)), 'data', 'test1.json'), "w"))
  print(default_path.setDefaultPath(join(dirname(dirname(__file__)), 'data', 'test.json'), "r"))
  
  print(delete_path.delete("test"))
  print(delete_path.delete("quiz"))
  print(delete_path.delete("hello"))

  #print(default_path.DEFAULT_PATH_READ, default_path.DEFAULT_PATH_SAVE)
  
  print(default_path.setDefaultPath(join(dirname(dirname(__file__)), 'data', 'save_test.json'), "r"))
  print("Default path read: ", default_path.DEFAULT_PATH_READ)
  quiz = loader.load("quiz")
  print("Quiz Option: ", quiz.sport.q1.options[0])
  
if __name__ == '__main__':
    main()

