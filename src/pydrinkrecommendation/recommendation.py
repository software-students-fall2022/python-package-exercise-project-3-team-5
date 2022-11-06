import json
import os
from os.path import dirname, join
import default_path as path
from types import SimpleNamespace
import warnings
import logging
from  drinks import Mood, Taste, Price, Drink
import random

def get_recommendation(mood: Mood, taste: Taste, price: Price):
    overridden_path = path.DEFAULT_PATH_READ
    if not os.path.exists(overridden_path):
        return logging.exception("The file for drinks does not exist!")
   
    with open(overridden_path) as f:
        try:
            data = json.load(f)
        except:
            return logging.exception("Failed to load the file for drinks!")
    
    #get all drinks that match the mood
    mood_filter = {k: v for k, v in data.items() if (mood == None or v["mood"] == mood)}
    taste_filter = {k: v for k, v in data.items() if (taste == None or v["taste"] == taste)}
    price_filter = {k: v for k, v in data.items() if (price == None or v["price"] == price)}
    
    #get the intersection of all drinks that match mood_filter, taste_filter, and price_filter
    intersection = set(mood_filter.keys()).intersection(set(taste_filter.keys())).intersection(set(price_filter.keys()))
    
    result_dict ={}
    if len(intersection) != 0:
        result_dict = {k: v for k, v in data.items() if k in intersection}
    else:
        if (len(mood_filter) == 0 and len(taste_filter) == 0 and len(price_filter) == 0):
            return None
            
        #if there is no intersection, get a random drink dict from mood_filter, taste_filter, and price_filter
        result_dict = random.choice([mood_filter, taste_filter, price_filter])
        while len(result_dict) == 0:
            result_dict = random.choice([mood_filter, taste_filter, price_filter])
    
    #return a random drink from the result_dict
    return Drink(random.choice(list(result_dict.keys())), result_dict[random.choice(list(result_dict.keys()))]["mood"], result_dict[random.choice(list(result_dict.keys()))]["taste"], result_dict[random.choice(list(result_dict.keys()))]["price"])
