import json
import os #operation system


class DataFactory:

    @staticmethod
    def get_data(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data

    @staticmethod
    def save_data(file_path, data):
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)


class Data_Employee:
    @staticmethod
    def get_employees():
        data_path = os.path.join("Databases", "employees.json")
        return DataFactory.get_data(data_path)

    @staticmethod
    def save_employees(employees):
        data_path = os.path.join("Databases", "employees.json")
        DataFactory.save_data(data_path, employees)


class Data_Stock:
    @staticmethod
    def get_ingredients():
        data_path = os.path.join("Databases", "Stock.json")
        return DataFactory.get_data(data_path)

    @staticmethod
    def save_ingredients(ingredients):
        data_path = os.path.join("Databases", "Stock.json")
        DataFactory.save_data(data_path, ingredients)


class Data_Menu:
    @staticmethod
    def display_menu():
        data_path = os.path.join("Databases", "menu.json")
        return DataFactory.get_data(data_path)

    @staticmethod
    def save_to_menu(menu_data):
        data_path = os.path.join("Databases", "menu.json")
        existing_data = DataFactory.get_data(data_path)
        existing_data['menu_items'] = menu_data['menu_items']
        DataFactory.save_data(data_path, existing_data)


class Data_Table:
    @staticmethod
    def get_tables():
        data_path = os.path.join("Databases", "tables.json")
        return DataFactory.get_data(data_path)

    @staticmethod
    def save_tables(tables):
        data_path = os.path.join("Databases", "tables.json")
        DataFactory.save_data(data_path, tables)


class Data_OrderHistory:
    @staticmethod
    def get_order_history():
        data_path = os.path.join("Databases", "order_history.json")
        return DataFactory.get_data(data_path)

    @staticmethod
    def save_order_history(order_history):
        data_path = os.path.join("Databases", "order_history.json")
        DataFactory.save_data(data_path, order_history)
