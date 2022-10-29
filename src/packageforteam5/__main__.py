import wisdom
import loader
import os

def main():
  line = wisdom.get()
  print(line)
  print(loader.DEFAULT_PATH)
  if not os.path.exists(os.path.dirname(loader.DEFAULT_PATH)):
      os.makedirs(os.path.dirname(loader.DEFAULT_PATH))

  print(loader.load("quiz")["sport"]["q1"]["options"][0])
  print(loader.load("test"))
  print(loader.load("notexist", "default"))
if __name__ == '__main__':
    main()

