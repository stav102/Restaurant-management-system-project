import json
import random
from datetime import datetime
from Data_layer import *

class Dish:
    def __init__(self, name, price, ingredients):
        """
        Initialize a Dish object.
        """
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def __repr__(self):
        return f"{self.name} - ${self.price:.2f}"
    
     