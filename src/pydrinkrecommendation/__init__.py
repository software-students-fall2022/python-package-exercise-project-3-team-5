from os.path import dirname, join
import sys
import os


sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from drinks import Taste, Mood, Price
import default_path
import recommendation

def setDefaultPath(path):
    default_path.setDefaultPath(path)
    
def get_recommendation(mood: Mood, taste: Taste, price: Price):
    return recommendation.get_recommendation(mood, taste, price)
    