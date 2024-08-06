from python_super_project import Super
from python_super_project.DataModels.Employee.Employee import Employee
from python_super_project.Sections.HygieneSection import HygieneSection
from python_super_project.Sections.MeatSection import MeatSection
from python_super_project.Sections.VegetablesSection import VegetablesSection


class Usher (Employee):


    def __init__(self, name: str, ID: int, age: int, phon: str, numberUsher: int, password: int):
        super().__init__(name, ID, age, phon)
        self.numberUsher = numberUsher
        self.isAvailable = True
        self.password = password


    def __str__(self):
        return f"Employee Name: {self.name}\nID: {self.ID}\nAge: {self.age}\nPhone: {self.phon}\nUsher Number: {self.numberUsher}"
    def __eq__(self, other):
        if (isinstance(other, Usher)):
            if (self.name == other.name and self.ID == other.ID and self.age == other.age and self.phon == other.phon):
                return True
        return False



    def finishUsher(self):
        self.isAvailable = True

    def addProduct(meat_section: MeatSection, Higiene_Section: HygieneSection, Vegetables_Section: VegetablesSection):
        print("Which section?\n1. Hygiene\n2. Meat\n3. Vegetables")
        section = int(input())
        if section == 1:
            print("Which Product?\n1. Toilet Paper\n2. Wipes\n3. Ear stick\n4. toothpicks\n5. Soap")
            product_index = int(input()) - 1
            print("how much to add?")
            amount = int(input())
            Higiene_Section.addHigieneproduct(Higiene_Section, product_index, amount)

        elif section == 2:
            print("Which Product?\n1. Chicken Breast\n2. Chicken Wings\n3. Hotdog\n4. Mince\n5. Spring Chicken")
            product_index = int(input()) - 1
            print("how much to add?")
            amount = int(input())
            meat_section.add_product(meat_section, product_index, amount)

        elif section == 3:
            print("Which Product?\n1. tomato\n2. cucumber\n3. Potato\n4. sweet potato\n5. cabbage")
            product_index = int(input()) - 1
            print("how much to add?")
            amount = int(input())
            Vegetables_Section.addVegetablesProduct(Vegetables_Section, product_index, amount)


    def bringDownProduct(meat_section: MeatSection, Higiene_Section: HygieneSection, Vegetables_Section: VegetablesSection):
        print("Which section?\n1. Hygiene\n2. Meat\n3. Vegetables")
        section = int(input())
        if section == 1:
            print("Which Product?\n1. Toilet Paper\n2. Wipes\n3. Ear stick\n4. toothpicks\n5. Soap")
            product_index = int(input()) - 1
            print("how much to bring Down?")
            amount = int(input())
            Higiene_Section.bringDownMeatProdect(Higiene_Section, product_index, amount)
        elif section == 2:
            print("Which Product?\n1. Chicken Breast\n2. Chicken Wings\n3. Hotdog\n4. Mince\n5. Spring Chicken")
            product_index = int(input()) - 1
            print("how much to bring Down?")
            amount = int(input())
            meat_section.bringDownMeatProdect(meat_section, product_index, amount)

        elif section == 3:
            print("Which Product?\n1. tomato\n2. cucumber\n3. Potato\n4. sweet potato\n5. cabbage")
            product_index = int(input()) - 1
            print("how much to add?")
            amount = int(input())
            Vegetables_Section.addVegetablesProduct(Vegetables_Section, product_index, amount)

    @staticmethod
    def chakUsher(ushers: list, password: int):
        for user in ushers:
            if user.password == password:
                return {"status": True, "user": user}
        return {"status": False,"user": None}

    @staticmethod
    def loadUsher(super: Super):
        usher1 = Usher("yisca rosenblatt", 327721288, 19, "0585343487", 0, 520027)
        usher2 = Usher("rosenblatt", 596, 19, "0585343487", 1, 123)
        super.ushers.append(usher1)
        super.ushers.append(usher2)

