import json
import random
from datetime import datetime
from Data_layer import *



class Ingredient:
    def __init__(self, name, amount, unit):
        self.name = name
        self.amount = amount
        self.unit = unit
        
    def __str__(self):
        return f"{self.amount} {self.unit} of {self.name}"