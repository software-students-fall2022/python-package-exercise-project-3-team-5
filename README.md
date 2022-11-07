![Python build & test](https://github.com/software-students-fall2022/python-package-exercise-project-3-team-5/actions/workflows/main.yml/badge.svg)

[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=9088608&assignment_repo_type=AssignmentRepo)
# Python Package Exercise

A little exercise to create a Python package, build it, test it, distribute it, and use it. See [instructions](./instructions.md) for details.

# pydrinkrecommendation - Recommend daily drink


## Functions
`pydrinkrecommendation` has 4 functions to help users get their daily drink recommendation: 

### **Set Default Path for the Stored File**
By default, all information about drinks is saved on ../data/save.json. But you can change the saved file's path:
```python
import pydrinkrecommendation as rec

rec.setDefaultPath(path: str)
```
If `path` doesn't exist, it will create corresponding directories and files.\
For example:
```python
import os
from os.path import dirname, join
import sys
import pydrinkrecommendation as rec

p =join(dirname(dirname(__file__)), 'data', 'file.json')
rec.setDefaultPath(p)
```
This will create a Json file named "file.json" in "data" folder located in the parent directory of the current .py file.
<br>\
<br>

### **Store and Update a Drink**
```python
import pydrinkrecommendation as rec
from pydrinkrecommendation.drinks import Mood, Taste, Price, Drink

rec.write_drink(drink: Drink)
```
This will store a drink (an object of type `Drink`) to the default file path.\
If the dafault file already contains a drink of the same name, then this will update that drink to the input properties.

\
For example:
```python
import pydrinkrecommendation as rec
from pydrinkrecommendation.drinks import Mood, Taste, Price, Drink


rec.write_drink(Drink(name="New Drink", mood = Mood.Happy, taste = Taste.Sweet, price = Price.Low))
```
This will write a new drink names "New Drink" with corresponding properties to the default Json file.

<br>
<br>

### **Delete a drink**
```python
import pydrinkrecommendation as rec

rec.delete_drink(drink_name: str)
```
This will delete the corresponding drink from the default Json file, and return the `Drink` object. If the drink doesn't exist, this will return `None`

For example:
```python
import pydrinkrecommendation as rec

rec.delete_drink("Cappuccino")
```
This will delete and return a `Drink` object whose name is "Cappuccino".

<br>
<br>

### **Get a Random Drink Recommendation**
```python
import pydrinkrecommendation as rec
from pydrinkrecommendation.drinks import Mood, Taste, Price, Drink

rec.get_recommendation(mood: Mood, taste: Taste, price: Price)
```
This will return a random `Drink` object that matches `Mood`, `Taste`, and `Price`. 
- If any of the parameters is `None`, that property will not be considered (For example, if `Mood` is `None`, then only `Taste` and `Price` will become the filters).
- If all of the parameters are `None`, then the returned `Drink` object will be randomly chosen from all drinks in the Json file
- If none of the drinks matches the filters, then this will return a random `Drink` object that matches either `Mood`, `Taste`, or `Price`.

For example:
```python
import pydrinkrecommendation as rec
from pydrinkrecommendation.drinks import Mood, Taste, Price, Drink

rec.get_recommendation(Mood.Happy, Taste.Sweet, None)
```
This will return a random `Drink` object whose `Mood` is `Happy` **and** `Taste` is `Sweet`.

<br>
<br>


## Installation & Use the package as a Module

<br>
<br>

## Example Project
An example project using this package can be found [here](https://github.com/cty288/pydrinkrecommendation-example). Please follow the instructions in the project's `README.md` file to run this project.
<br>
<br>


## How to build and test this package
1. Install [pipenv](https://packaging.python.org/en/latest/tutorials/managing-dependencies/#managing-dependencies) and [build](https://packaging.python.org/en/latest/tutorials/packaging-projects/#generating-distribution-archives) if not already installed.
2. Navigate to the root folder of this project (where `pyproject.toml` is located).
3. Install `pytest` in a virtual environment
4. Run the tests from the root directory. Tests files are located in `src/pydrinkrecommendation/tests` directory. Test Json files are located in `src/data` directory.
   ```
   python3 -m pytest
   ```
5. To build this project, run the following command from the root directory
   ```
   python -m build
   ```

# Contributors
[Iris Qian](https://github.com/okkiris)\
[Tim Chen](https://github.com/cty288)\
[Ziyang Liao](https://github.com/ian-Liaozy)\
Shannon Huang


