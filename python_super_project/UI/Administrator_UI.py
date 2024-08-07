from python_super_project.Sections.MeatSection import MeatSection
from python_super_project.Sections.Section import Section
from python_super_project.Sections.VegetablesSection import VegetablesSection
from python_super_project.Sections.HygieneSection import HygieneSection




class Administrator_UI:

    def __init__(self, Super):
        self.Super = Super

    def show(self) -> None:
        print("hello Administor. Choose your option:\n1. List of products\n2. List of employees?\n3. List of "
              "customers who bought that day\n4. How much money was put in today?\nQ. back")
        option = int(input())

        if option == 1:
            print("Which section?\n1. Vegetables section\n2. Hygiene section\n3. Meat section")
            optionSection = int(input())
            if optionSection == 1:
                print(VegetablesSection().craectmeatVegetablesProducts())
            elif optionSection == 2:
                print(HygieneSection().craectHigieneProducts())
            elif optionSection == 3:
                print(MeatSection().craectmeatProducts())
        # רשימה של העובדים
        elif option == 2:
            for names in self.Super.ushers:
                name = names.name
                print(f"The names of the ushers that worked today {name}")
            for names in self.Super.cashiers:
                name = names.name
                print(f"The names of the cashiers that worked today {name}")

        elif option == 3:
            print("אנחנו צריכות לעשות רשימת לקוחות ")

        elif option == 4:
            sum = 0
            for money in HygieneSection.HygieneSection():
                sum += money.price

        # elif option == 'Q':
        #     # Employee_UI.Show()

        return None