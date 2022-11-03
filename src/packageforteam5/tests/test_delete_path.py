import json
import os
from os.path import dirname, join
import sys



sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import delete_path
import default_path as path

data1 = {
    "quiz": {
        "sport": {
            "q1": {
                "question": "Which one is correct team name in NBA?",
                "options": [
                    "New York Bulls",
                    "Los Angeles Kings",
                    "Golden State Warriros",
                    "Huston Rocket"
                ],
                "answer": "Huston Rocket"
            }
        },
        "maths": {
            "q1": {
                "question": "5 + 7 = ?",
                "options": [
                    "10",
                    "11",
                    "12",
                    "13"
                ],
                "answer": "12"
            },
            "q2": {
                "question": "12 - 8 = ?",
                "options": [
                    "1",
                    "2",
                    "3",
                    "4"
                ],
                "answer": "4"
            }
        }
    },
	"test" : 5
}

data2 = {
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}

def add_file1(path):
    if os.path.exists(path):
         with open(path,'w') as file:
            file.write(json.dumps(data1, indent=4))

def add_file2(path):
    if os.path.exists(path):
         with open(path,'w') as file:
            file.write(json.dumps(data2, indent=4))
    
def init_test():
    t3 = join(dirname(dirname(dirname(__file__))), 'data', 'save_test_3.json')
    add_file1(t3)
    t4 = join(dirname(dirname(dirname(__file__))), 'data', 'save_test_4.json')
    add_file2(t4)


def delete_nonexisting_data():
    path.setDefaultPath(join(dirname(dirname(dirname(__file__))), 'data', 'save.json'),"r")
    print(delete_path.delete("test"))

def delete_existing_data1():
    init_test()
    path.setDefaultPath(join(dirname(dirname(dirname(__file__))), 'data', 'save_test_3.json'),"r")
    return delete_path.delete("quiz")

def delete_existing_data2():
    init_test()
    path.setDefaultPath(join(dirname(dirname(dirname(__file__))), 'data', 'save_test_3.json'),"r")
    return delete_path.delete("test")

def delete_nonexisting_data2():
    path.setDefaultPath(join(dirname(dirname(dirname(__file__))), 'data', 'save_test_4.json'),"r")
    return delete_path.delete("test")

def delete_existing_data3():
    init_test()
    path.setDefaultPath(join(dirname(dirname(dirname(__file__))), 'data', 'save_test_4.json'),"r")
    return delete_path.delete("glossary")

def test_delete_nonexisting_data():
    assert delete_nonexisting_data() == None

def test_delete_existing_data1():
    assert delete_existing_data1() ==  {"sport": {
            "q1": {
                "question": "Which one is correct team name in NBA?",
                "options": [
                    "New York Bulls",
                    "Los Angeles Kings",
                    "Golden State Warriros",
                    "Huston Rocket"
                ],
                "answer": "Huston Rocket"
            }
        },
        "maths": {
            "q1": {
                "question": "5 + 7 = ?",
                "options": [
                    "10",
                    "11",
                    "12",
                    "13"
                ],
                "answer": "12"
            },
            "q2": {
                "question": "12 - 8 = ?",
                "options": [
                    "1",
                    "2",
                    "3",
                    "4"
                ],
                "answer": "4"
            }
        }
    }
def test_delete_existing_data2():
    assert delete_existing_data2() == 5  

def test_delete_nonexisting_data2():
    assert delete_nonexisting_data2() == None 

def test_delete_existing_data3():
    assert delete_existing_data3() == {"title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }