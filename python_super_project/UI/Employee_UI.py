# In Employee_UI.py

from python_super_project.UI.Usher_UI import Usher_UI
from python_super_project.UI.Cashier_UI import Cashier_UI
from python_super_project.UI.ShiftManager_UI import ShiftManager_UI
from python_super_project.UI.Administrator_UI import Administrator_UI
class Employee_UI:
    def __init__(self, super):
        self.super = super

    def show(self):
        isFine = False
        while not isFine:
            # try:
                print("Which employee?\n1. Usher\n2. cashier\n3. shift manager\n4. Administrator")
                employee = int(input())
                if employee == 1:
                    Usher_UI(self.super).show()
                    isFine = True
                elif employee == 2:
                    Cashier_UI(self.super).show()
                    isFine = True
                elif employee == 3:
                    ShiftManager_UI(self.super).show()
                    isFine = True
                elif employee == 4:
                    Administrator_UI(self.super).show()
                    isFine = True
                else:
                    print("You need to choose 1-4")
            # except Exception as e:
            #     print(f"An error occurred: {e}. Please choose 1-4")