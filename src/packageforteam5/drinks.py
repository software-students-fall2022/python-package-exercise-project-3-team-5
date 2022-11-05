from enum import IntEnum

class Mood(IntEnum):
    Tired = 0,
    Happy = 1

class Taste(IntEnum):
    Bitter = 0,
    Sweet = 1
    
class Price(IntEnum):
    Low = 0,
    Medium = 1,
    High = 2
    
class Drink():
    def __init__(self, name, mood: Mood, taste: Taste, price: Price):
        self.name = name
        self.mood = mood
        self.taste = taste
        self.price = price