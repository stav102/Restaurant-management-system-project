from Data_layer import Data_Menu
from Dish import *

class Menu:
    def __init__(self):
        self.menu_items = []
        self.menu_dict = Data_Menu.display_menu()
        
    def display_menu(self):
        print("Menu:")
        for dish in self.menu_dict['menu_items']:
            print(f"{dish['name']}: ${dish['price']}")
            print("Ingredients:")
            for ingredient in dish['ingredients']:
                print(f"- {ingredient['name']}: {ingredient['amount']} {ingredient['unit']}")
            print()
    
    def add_dish(self, dish):
        self.menu_dict['menu_items'].append(dish.__dict__)
        Data_Menu.save_to_menu(self.menu_dict)  
    
    def edit_dish(self, dish_name, new_dish):
        for i, dish in enumerate(self.menu_dict['menu_items']):
            if dish['name'] == dish_name:
                updated_dish = Dish(new_dish['name'], new_dish['price'], new_dish['ingredients'])
                self.menu_dict['menu_items'][i] = updated_dish.__dict__
                Data_Menu.save_to_menu(self.menu_dict)  # Save menu data
                print(f"{dish_name} was updated in the menu.")
                break
        else:
            print(f"{dish_name} was not found in the menu.")

    def remove_dish(self, dish_name):
        for i, dish in enumerate(self.menu_dict['menu_items']):
            if dish['name'] == dish_name:
                del self.menu_dict['menu_items'][i]
                Data_Menu.save_to_menu(self.menu_dict)  
                print(f"{dish_name} was removed from the menu.")
                break
        else:
            print(f"{dish_name} was not found in the menu.")


menu = Menu()

