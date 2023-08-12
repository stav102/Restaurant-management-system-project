from Employee import *
from Dish import Dish
from Ingredient import Ingredient


class PrototypeEmployee(Employee):
    def __init__(self, employee_id, name, phone, email, role):
        super().__init__(employee_id, name, phone, email, role)

    def clone(self):
        clone = PrototypeEmployee(
            employee_id=self.get_employee_id(),
            name=self.get_name(),
            phone=self.get_phone(),
            email=self.get_email(),
            role=self.role
        )
        return clone

    def get_employee_details_from_input(self):
        while True:
            employee_id = input("Enter employee ID: ")
            if employee_id.strip():
                try:
                    self._Employee__employee_id = int(employee_id)
                    break
                except ValueError:
                    print("Invalid input type. Please enter an integer for employee ID.")
            else:
                print("Input cannot be blank. Please try again.")

        self._Employee__name = input("Enter employee name: ")

        while True:
            phone = input("Enter employee phone number: ")
            if phone.isdigit() and len(phone) == 10:
                break
            print("Invalid input. Please enter a valid 10-digit phone number (numeric value).")

        self._Employee__phone = phone

        while True:
            email = input("Enter employee email: ")
            if "@" in email and "." in email:
                break
            print("Invalid input. Please enter a valid email address.")

        self._Employee__email = email

        self.role = input("Enter employee role: ")

    def get_employee_id_from_input(self):
        while True:
            employee_id = input("Enter employee ID to delete: ")
            if employee_id.strip():
                try:
                    self._Employee__employee_id = int(employee_id)
                    break
                except ValueError:
                    print("Invalid input type. Please enter an integer for employee ID.")
            else:
                print("Input cannot be blank. Please try again.")

    def delete_employee(self):
        Employee.delete_employee(self.get_employee_id())






class DishPrototype(Dish):
    def __init__(self, name=None, price=None, ingredients=None):
        super().__init__(name, price, ingredients or [])

    def clone(self):
        clone = DishPrototype(self.name, self.price, self.ingredients.copy())
        return clone

    def get_dish_details_from_input(self):
        while True:
            name = input("Enter the name of the dish: ")
            if name.strip():
                self.name = name
                break
            print("Input cannot be blank. Please enter a valid dish name.")

        while True:
            price_str = input("Enter the price of the dish: ")
            if price_str.strip():
                try:
                    price = float(price_str)
                    self.price = price
                    break
                except ValueError:
                    print("Invalid input type. Please enter a valid numeric value for the dish price.")
            else:
                print("Input cannot be blank. Please enter a valid dish price.")

        self.ingredients = []
        while True:
            ingredient_name = input("Enter an ingredient name or 'done' to finish: ")
            if ingredient_name == 'done':
                break

            while True:
                ingredient_amount_str = input("Enter the amount of the ingredient: ")
                if ingredient_amount_str.strip():
                    try:
                        ingredient_amount = float(ingredient_amount_str)
                        break
                    except ValueError:
                        print("Invalid input type. Please enter a valid numeric value for the ingredient amount.")
                else:
                    print("Input cannot be blank. Please enter a valid ingredient amount.")

            while True:
                ingredient_unit = input("Enter the unit of measurement for the ingredient: ")
                if ingredient_unit.strip():
                    break
                print("Input cannot be blank. Please enter a valid unit of measurement.")

            ingredient = {'name': ingredient_name, 'amount': ingredient_amount, 'unit': ingredient_unit}
            self.ingredients.append(ingredient)




class IngredientPrototype(Ingredient):
    def clone(self):
        clone = IngredientPrototype(self.name, self.amount, self.unit)
        return clone

    def get_ingredient_details_from_input(self):
        self.name = input("Enter ingredient name: ")

        while True:
            amount_str = input("Enter the amount of the ingredient: ")
            if amount_str.strip():
                try:
                    amount = float(amount_str)
                    self.amount = amount
                    break
                except ValueError:
                    print("Invalid input type. Please enter a valid numeric value for the ingredient amount.")
            else:
                print("Input cannot be blank. Please enter a valid ingredient amount.")

        while True:
            unit = input("Enter the unit of measurement for the ingredient: ")
            if unit.strip():
                self.unit = unit
                break
            print("Input cannot be blank. Please enter a valid unit of measurement.")


