from python_super_project.UI import Cashier_UI, ShiftManager_UI, Usher_UI, Administrator_UI


class Employee_UI:
    def __init__(self):
        pass

    def show(self):
        print("Which employee?\n1. Usher\n2. cashier\n3. shift manager\n4. Administrator")
        employee = int(input())
        if (employee == 1):
            Usher_UI.Usher_UI().show()
        if (employee == 2):
            Cashier_UI.Cashier_UI.show
        if (employee == 3):
            ShiftManager_UI.ShiftManager_UI.show
        if (employee == 4):
            Administrator_UI.Administrator_UI.show