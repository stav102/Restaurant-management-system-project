from datetime import datetime
from Data_layer import *


class Employee:
    def __init__(self, employee_id, name, phone, email, role):
        """
        Initialize an Employee object.
        """
        self.__employee_id = employee_id
        self.__name = name
        self.__phone = phone
        self.__email = email
        self.role = role

    def get_employee_id(self):
        return self.__employee_id

    def get_name(self):
        return self.__name

    def get_phone(self):
        return self.__phone

    def get_email(self):
        return self.__email

    def add_employee(self):
        """
        Add an employee to the database.
        """
        employees_data = Data_Employee.get_employees()
        employees = employees_data["employees"]
        employees.append({
            "employee_id": self.__employee_id,
            "name": self.__name,
            "phone": self.__phone,
            "email": self.__email,
            "role": self.role
        })
        Data_Employee.save_employees(employees_data)

    @staticmethod
    def delete_employee(employee_id):
        """
        Delete an employee from the database.
        """
        employees_data = Data_Employee.get_employees()
        employees = employees_data["employees"]
        for i, employee in enumerate(employees):
            if employee["employee_id"] == employee_id:
                del employees[i]
                break
        Data_Employee.save_employees(employees_data)
    
    
    @staticmethod
    def view_employees():
        """
        View all employees in the database.
        """
        employees_data = Data_Employee.get_employees()
        if employees_data is None or "employees" not in employees_data:
            print("No employee data found.")
            return

        employees = employees_data["employees"]
        print("{:<15} {:<20} {:<15} {:<25} {:<15}".format("employee_id", "name", "phone", "email", "role"))
        for employee in employees:
            employee_id = employee.get("employee_id") or ""
            name = employee.get("name") or ""
            phone = employee.get("phone") or ""
            email = employee.get("email") or ""
            role = employee.get("role") or ""
            print("{:<15} {:<20} {:<15} {:<25} {:<15}".format(employee_id, name, phone, email, role))

    @staticmethod
    def get_employees():
        """
        Get a list of all employees in the database.
        """
        employees_data = Data_Employee.get_employees()
        employees = employees_data["employees"]
        return employees

    @staticmethod
    def edit_employee(employee_id, field, new_value):
        """
        Edit an employee's information in the database.
        """
        employees_data = Data_Employee.get_employees()
        employees = employees_data["employees"]
        for employee in employees:
            if employee["employee_id"] == employee_id:
                employee[field] = new_value
                Data_Employee.save_employees(employees_data)
                return True

        return False
