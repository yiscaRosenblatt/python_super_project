from Super import Super
from UI import Employee_UI , Customer_UI

class SuperMain_UI:
    def __init__(self, Super: Super):
        self.Super = Super
    def show (self):
        print("who are you?\n1. employee\n2. customer")
        someone = int(input())
        if (someone == 1):
            employee_ui = Employee_UI.Employee_UI()
            employee_ui.show()
        else:
            Customer_UI.Customer_UI().show()

