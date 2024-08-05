from python_super_project import Super
from python_super_project.DataModels.Employee.Employee import Employee



class Usher (Employee):

    def __init__(self, name: str, ID: int, age: int, phon: int, numberUsher: int, password: int):
        super().__init__(name, ID, age, phon)
        self.numberUsher = numberUsher
        self.isAvailable = True
        self.password = password
        self.corentUser: Usher = None

    def __str__(self):
        return f"Employee Name: {self.name}\nID: {self.ID}\nAge: {self.age}\nPhone: {self.phon}\nUsher Number: {self.numberUsher}"
    def __eq__(self, other):
        if (isinstance(other, Usher)):
            if (self.name == other.name and self.ID == other.ID and self.age == other.age and self.phon == other.phon):
                return True
        return False



    def finishUsher(self):
        self.isAvailable = True

    def addProduct (self):
        pass


    def chakUsher(self, password: int):
        for user in Super.Super().usher:
            if user.password == password:
                self.corentUser = user
                return True
        return False







