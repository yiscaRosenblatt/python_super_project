from python_super_project import Super
from python_super_project.DataModels.Employee import Usher


class Usher_UI:
    def __init__(self):
        pass

    def show(self):
        print("Enter your password")
        password = int(input())
        usher_instance = Usher.Usher(None, None, None, None, None, None)
        if usher_instance.chakUsher(password):
            usher_instance = Usher.Usher().corentUser
            print(f"Hello {usher_instance.name}")
        else:
            print("no")
