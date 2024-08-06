from python_super_project import Super
from python_super_project.DataModels.Employee.Usher import Usher


class Usher_UI:
    def __init__(self, super: Super):
        self.super = super

    def show(self):

        print("Enter your password")
        password = int(input())
        response = Usher.chakUsher(self.super.ushers, password)
        if response["status"]:
            print(f"Hello {response["user"].name}")
            self.action()
        else:
            print("Incorrect password")


    def action(self):
        isFine = False
        while isFine == False:
            try:
                print("what you wont to do?\n1. to add Products\n2. to bring down Products")
                action = int(input())
                if action == 1:
                    Usher.addProduct(self.super.meat_section, self.super.Hygiene_Section, self.super.Vegetables_Section)
                    isFine = True
                elif action == 2:
                    Usher.bringDownProduct(self.super.meat_section, self.super.Hygiene_Section, self.super.Vegetables_Section)
                    isFine = True
                    print("you need to choose 1-2")
            except:
               print("you need to choose one of the opshin")