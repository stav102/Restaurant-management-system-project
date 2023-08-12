import json
import random
from datetime import datetime
from Data_layer import *



class Stock:
    def __init__(self, name, amount, unit):
        self.name = name
        self.amount = amount
        self.unit = unit
    
    def __str__(self):
        return f"Ingredient Name: {self.name}, Amount: {self.amount}, Unit: {self.unit}"
    
    
    @staticmethod
    def print_stock():
        ingredients_data = Data_Stock.get_ingredients()
        ingredients = ingredients_data["ingredients"]
        print("{:<15} {:<10} {}".format("Ingredient", "Amount", "Unit"))
        for ingredient in ingredients:
            print("{:<15} {:<10} {}".format(ingredient['name'], ingredient['amount'], ingredient['unit']))

    @staticmethod
    def add_ingredient(name, amount, unit):
        ingredient = Stock(name=name, amount=amount, unit=unit)
        ingredients_data = Data_Stock.get_ingredients()
        ingredients = ingredients_data["ingredients"]
        ingredients.append(ingredient.__dict__)
        Data_Stock.save_ingredients(ingredients_data)
        print("Ingredient added successfully!")