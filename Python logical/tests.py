import unittest
from unittest.mock import patch
from datetime import datetime
from Dish import *
from Employee import *
from Hostess import *
from Ingredient import *
from Manager import *
from Menu import *
from Order_history import *
from Order import *
from Stock import *
from Table  import *



class TestEmployee(unittest.TestCase):
    @patch('Employee.Data_Employee.get_employees', return_value={"employees": []})
    @patch('Employee.Data_Employee.save_employees')
    def test_add_employee(self, mock_save, mock_get_employees):
        employee = Employee("001", "John Doe", "1234567890", "john@example.com", "Manager")
        employee.add_employee()
        mock_get_employees.assert_called_once()
        mock_save.assert_called_once()

    @patch('Employee.Data_Employee.get_employees', return_value={"employees": [{"employee_id": "001"}]})
    @patch('Employee.Data_Employee.save_employees')
    def test_delete_employee(self, mock_save, mock_get_employees):
        Employee.delete_employee("001")
        mock_get_employees.assert_called_once()
        mock_save.assert_called_once()

    @patch('Employee.Data_Employee.get_employees', return_value={"employees": [{"employee_id": "001", "name": "John Doe"}]})
    def test_view_employees(self, mock_get_employees):
        with patch('builtins.print') as mock_print:
            Employee.view_employees()
            mock_get_employees.assert_called_once()
            mock_print.assert_called()

    @patch('Employee.Data_Employee.get_employees', return_value={"employees": [{"employee_id": "001", "name": "John Doe"}]})
    def test_get_employees(self, mock_get_employees):
        employees = Employee.get_employees()
        mock_get_employees.assert_called_once()
        self.assertEqual(len(employees), 1)
        self.assertEqual(employees[0]["employee_id"], "001")
        self.assertEqual(employees[0]["name"], "John Doe")


class TestOrder(unittest.TestCase):
    @patch('Menu.Data_Menu.display_menu',
           return_value={"menu_items": [
               {"name": "Dish 1", "price": 10.0, "ingredients": []},
               {"name": "Dish 2", "price": 15.0, "ingredients": []},
               {"name": "Dish 3", "price": 12.5, "ingredients": []}
           ]})
    @patch('Stock.Data_Stock.get_ingredients',
           return_value={"ingredients": []})
    @patch('Stock.Data_Stock.save_ingredients')
    @patch('Order_history.Data_OrderHistory.get_order_history',
           return_value={"orders": []})
    @patch('Order_history.Data_OrderHistory.save_order_history')
    def test_take_order(self, mock_save_order_history, mock_get_order_history,
                        mock_save_ingredients, mock_get_ingredients, mock_display_menu):
        with patch('builtins.input', side_effect=["Dish 1", "2", "done"]):
            order = Order(None, None, None, 0, [])
            order.take_order("John Doe")

        mock_display_menu.assert_called_once()
        mock_get_order_history.assert_called_once()
        mock_save_order_history.assert_called_once()
        mock_get_ingredients.assert_called_once()
        mock_save_ingredients.assert_called_once()

    @patch('Order_history.Data_OrderHistory.get_order_history',
           return_value={"orders": [
               {"order_id": "1234", "customer_name": "John Doe", "order_time": "2023-05-17 12:00:00",
                "total_price": 25.0, "items": [{"name": "Dish 1", "amount": 2}, {"name": "Dish 2", "amount": 1}]}
           ]})
    def test_view_orders(self, mock_get_order_history):
        with patch('builtins.print') as mock_print:
            Order.view_orders()

            mock_get_order_history.assert_called_once()
            mock_print.assert_called()

    @patch('Order_history.Data_OrderHistory.get_order_history',
           return_value={"orders": [
               {"order_id": "1234", "customer_name": "John Doe", "order_time": "2023-05-17 12:00:00",
                "total_price": 25.0, "items": [{"name": "Dish 1", "amount": 2}, {"name": "Dish 2", "amount": 1}]}
           ]})
    @patch('Order_history.Data_OrderHistory.save_order_history')
    def test_delete_order(self, mock_save_order_history, mock_get_order_history):
        with patch('builtins.input', return_value="1234") as mock_input:
            Order.delete_order()

            mock_get_order_history.assert_called_once()
            mock_save_order_history.assert_called_once()
            mock_input.assert_called_with("Enter the ID of the order you would like to delete: ")

    @patch('Order_history.Data_OrderHistory.get_order_history',
           return_value={"orders": [
               {"order_id": "1234", "customer_name": "John Doe", "order_time": "2023-05-17 12:00:00",
                "total_price": 25.0, "items": [{"name": "Dish 1", "amount": 2}, {"name": "Dish 2", "amount": 1}]}
           ]})
    def test_view_order_history(self, mock_get_order_history):
        with patch('builtins.print') as mock_print:
            Order.view_order_history()

            mock_get_order_history.assert_called_once()
            mock_print.assert_called()

    def test_edit_order_history(self):
        order_id = "1234"
        choice = 1
        new_value = "Jane Doe"
        order_history = {
            "orders": [
                {
                    "order_id": order_id,
                    "customer_name": "John Doe",
                    "order_time": "2023-05-17 12:00:00",
                    "total_price": 25.0,
                    "items": [{"name": "Dish 1", "amount": 2}, {"name": "Dish 2", "amount": 1}]
                }
            ]
        }
        expected_order_history = {
            "orders": [
                {
                    "order_id": order_id,
                    "customer_name": new_value,
                    "order_time": "2023-05-17 12:00:00",
                    "total_price": 25.0,
                    "items": [{"name": "Dish 1", "amount": 2}, {"name": "Dish 2", "amount": 1}]
                }
            ]
        }

        with patch('Order_history.Data_OrderHistory.get_order_history', return_value=order_history) as mock_get_order_history:
            with patch('Order_history.Data_OrderHistory.save_order_history') as mock_save_order_history:
                order = Order(None, None, None, 0, [])
                order.edit_order_history(order_id, choice, new_value)

                mock_get_order_history.assert_called_once()
                mock_save_order_history.assert_called_with(expected_order_history)


class TestOrderHistory(unittest.TestCase):


    @patch('Order_history.Data_OrderHistory.get_order_history')
    @patch('Order_history.Data_OrderHistory.save_order_history')
    @patch('builtins.print')
    def test_edit_order_history(self, mock_print, mock_save_order_history, mock_get_order_history):
        order_history = {
            'orders': [
                {
                    'order_id': 1,
                    'customer_name': 'John Doe',
                    'total_price': 25.99,
                    'order_time': '2023-05-15 15:30:00'
                }
            ]
        }
        mock_get_order_history.return_value = order_history

        order_history = OrderHistory()
        order_history.edit_order_history(1, 1, 'Jane Smith')

        expected_order_history = {
            'orders': [
                {
                    'order_id': 1,
                    'customer_name': 'Jane Smith',
                    'total_price': 25.99,
                    'order_time': '2023-05-15 15:30:00'
                }
            ]
        }
        mock_save_order_history.assert_called_with(expected_order_history)
        mock_print.assert_called_with("Order history updated.")


class TestTable(unittest.TestCase):
    @patch('Table.Data_Table.get_tables')
    @patch('Table.Data_Table.save_tables')
    @patch('builtins.print')
    def test_reserve_table_success(self, mock_print, mock_save_tables, mock_get_tables):
        tables_data = {
            'tables': [
                {'table_number': 1, 'status': 'free for reservation'},
                {'table_number': 2, 'status': 'occupied'}
            ]
        }
        mock_get_tables.return_value = tables_data

        table = Table(1, 'free for reservation')
        Table.reserve_table(table)

        expected_output = 'Table 1 reserved successfully.'
        mock_print.assert_called_with(expected_output)
        mock_save_tables.assert_called_with(tables_data)

    @patch('Table.Data_Table.get_tables')
    @patch('Table.Data_Table.save_tables')
    @patch('builtins.print')
    def test_reserve_table_not_available(self, mock_print, mock_save_tables, mock_get_tables):
        tables_data = {
            'tables': [
                {'table_number': 1, 'status': 'occupied'},
                {'table_number': 2, 'status': 'free for reservation'}
            ]
        }
        mock_get_tables.return_value = tables_data

        table = Table(1, 'free for reservation')
        Table.reserve_table(table)

        expected_output = 'Table 1 is not available for reservation.'
        mock_print.assert_called_with(expected_output)
        mock_save_tables.assert_not_called()



if __name__ == '__main__':
    unittest.main()
