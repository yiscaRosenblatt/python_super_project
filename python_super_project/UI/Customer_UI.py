from python_super_project.DataModels.Customer import Customer
from python_super_project.DataModels.Employee.Cashier import Cashier
from python_super_project.UI.Cashier_UI import Cashier_UI


class Customer_UI:
    def __init__(self, Super):
        self.Super = Super

    def show(self):
        print("Hello and welcome to the Super\nwhat is your name?")
        name = input()
        print(f"Hello {name}\nA cashier will contact you in a second")
        newCustomer = Customer(name)
        Customer.addCustomer(newCustomer, self.Super.cashiers)
        response = Cashier.CashierAvailable(self.Super.cashiers)
        if response["status"]:
            Cashier_UI.showForCustomer(self, response["cashier"], newCustomer)

