import json
import random
from datetime import datetime
from Data_layer import *
from Table import Table



class Order:
    def __init__(self, order_id, customer_name, order_time, total_price, items, table_number=None):
        self.order_id = order_id
        self.customer_name = customer_name
        self.order_time = order_time
        self.total_price = total_price
        self.items = items
        self.table_number = table_number

        
    def __str__(self):
        return f"Order ID: {self.order_id}, Customer Name: {self.customer_name}, Order Time: {self.order_time}, Total Price: ${self.total_price}"
    
    def take_order(self, customer_name, table_number, menu_items):
        self.table_number = table_number
        Table.reserve_table(table_number)

        print("Menu:")
        for item in menu_items:
            print(f"{item['name']}: ${item['price']}")

        self.customer_name = customer_name
        self.order_time = str(datetime.now())
        self.order_id = str(random.randint(1000, 9999))

        while True:
            item_name = input(
                "Please enter the name of the dish you want to order (type 'done' to finish): ")
            if item_name == "done":
                break
            else:
                item_amount = int(input("Please enter the amount: "))
                item = next(
                    (x for x in menu_items if x["name"] == item_name), None)
                if item:
                    # Check ingredient availability
                    stock = Data_Stock.get_ingredients()
                    insufficient_ingredients = False
                    for ingredient in item["ingredients"]:
                        stock_ingredient = next(
                            (x for x in stock["ingredients"] if x["name"] == ingredient["name"]), None)
                        if stock_ingredient:
                            if stock_ingredient["amount"] < ingredient["amount"] * item_amount:
                                insufficient_ingredients = True
                                break
                        else:
                            insufficient_ingredients = True
                            break

                    if insufficient_ingredients:
                        print(f"Not enough ingredients to prepare  {item_amount} {item_name}'s. Please choose another dish.")
                        continue

                    self.items.append(
                        {"name": item_name, "amount": item_amount})
                    self.total_price += item["price"] * item_amount

                    # Reduce ingredient stock
                    for ingredient in item["ingredients"]:
                        stock_ingredient = next(
                            (x for x in stock["ingredients"] if x["name"] == ingredient["name"]), None)
                        if stock_ingredient:
                            stock_ingredient["amount"] -= ingredient["amount"] * item_amount

                    Data_Stock.save_ingredients(stock)
                else:
                    print(f"{item_name} is not in the menu.")

        order_history = Data_OrderHistory.get_order_history()
        order_history["orders"].append(self.__dict__)
        Data_OrderHistory.save_order_history(order_history)
        print("Order added to the order history!")
        print("Order created successfully!")
    print("Order saved to order history")
    
    @staticmethod
    def view_orders():
        order_history = Data_OrderHistory.get_order_history()
        orders = order_history["orders"]
        for order in orders:
            print(f"Order ID: {order['order_id']}")
            print(f"Customer Name: {order['customer_name']}")
            print(f"Order Time: {order['order_time']}")
            print(f"Total Price: ${order['total_price']}")
            print(f"Items:")
            for item in order["items"]:
                print(f"{item['name']} X {item['amount']}")
            print("*" * 15)

    @staticmethod
    def delete_order(order_id):
        order_history = Data_OrderHistory.get_order_history()
        orders = order_history["orders"]

        updated_orders = [
            order for order in orders if order['order_id'] != order_id]

        if len(updated_orders) == len(orders):
            print(f"No order found with ID {order_id}.") 
            return

        order_history["orders"] = updated_orders
        Data_OrderHistory.save_order_history(order_history)

        print(f"Order {order_id} has been deleted from the order history.")

    @staticmethod
    def view_order_history():
        order_history = Data_OrderHistory.get_order_history()

        for order in order_history["orders"]:
            print(f"Order ID: {order['order_id']}")
            print(f"Customer Name: {order['customer_name']}")
            print(f"Order Time: {order['order_time']}")
            print(f"Total Price: ${order['total_price']:.2f}")
            print("Items:")
            for item in order['items']:
                print(f" - {item['name']} ({item['amount']})")
            print()

    def edit_order_history(self, order_id, choice, new_value=None):
        order_history = Data_OrderHistory.get_order_history()
        order_to_edit = None
        for order in order_history['orders']:
            if order['order_id'] == order_id:
                order_to_edit = order
                break
        if order_to_edit:
            if choice == 1:
                order_to_edit['customer_name'] = new_value
            elif choice == 2:
                order_to_edit['total_price'] = new_value
            elif choice == 3:
                order_to_edit['items'] = new_value
            elif choice == 4:
                order_to_edit['table_number'] = new_value
            else:
                print("Invalid choice.")
                return
            Data_OrderHistory.save_order_history(order_history)
        else:
            print(f"No order found with ID {order_id}.")
            return
