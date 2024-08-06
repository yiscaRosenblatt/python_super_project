from python_super_project.DataModels.Employee.Cashier import Cashier
from python_super_project.DataModels.Employee.Usher import Usher
from python_super_project.UI import Employee_UI, Customer_UI


class SuperMain_UI:
    def __init__(self, Super):
        self.Super = Super
    def show (self):
        Usher.loadUsher(self.Super)
        Cashier.loadUsher(self.Super)
        isFine = False
        while isFine == False:
            try:
                print("who are you?\n1. employee\n2. customer")
                someone = int(input())
                if someone == 1:
                    Employee_UI.Employee_UI(self.Super).show()
                    isFine = True
                elif someone == 2:
                    Customer_UI.Customer_UI().show()
                    isFine = True
                else:
                    print("you need to choose 1-2")

            except:
                print("you need to choose 1-2")

