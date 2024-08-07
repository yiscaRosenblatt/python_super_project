from python_super_project.DataModels.Employee.Usher import Usher
from python_super_project.Sections.HygieneSection import HygieneSection
from python_super_project.Sections.MeatSection import MeatSection
from python_super_project.Sections.VegetablesSection import VegetablesSection


class ShiftManager_UI:
    def _init_(self, super):
        self.super = super


    def show(self):
        print("Hello shift menager.\nWhat to you want to do?\n1. Update products from product list.\n2. update "              
              "employees.\n3. customer list.\n4. List of purchased products")

        option = int(input())
        if option == 1:

            print("Which section?\n1. meat.\n2. hygiene.\n3. vegetables")
            whichSec = int(input())
            if whichSec == 1:

                print("1.To Add\n2. To delete")
                isFine = False
                while isFine == False:
                    try:
                        addOrDelete = int(input())
                        if addOrDelete == 1:
                            MeatSection.add_product(self.super.meat_section, self.super.Hygiene_Section, self.super.Vegetables_Section)
                            isFine = True
                        elif addOrDelete == 2:
                            MeatSection.bringDownMeatProdect(self.super.meat_section, self.super.Hygiene_Section, self.super.Vegetables_Section)
                            isFine = True
                    except:
                        print("you need to choose one of the opshin")

            if whichSec == 2:

                print("1.To Add\n2. To delete")
                isFine = False
                while isFine == False:
                    try:
                        addOrDelete = int(input())
                        if addOrDelete == 1:
                            HygieneSection.addHigieneproduct(self.super.meat_section, self.super.Hygiene_Section,self.super.Vegetables_Section)
                            isFine = True
                        elif addOrDelete == 2:
                            HygieneSection.bringDownMeatProdect(self.super.meat_section, self.super.Hygiene_Section,
                                                             self.super.Vegetables_Section)
                            isFine = True
                    except:
                        print("you need to choose one of the opshin")
            if whichSec == 3:

                print("1.To Add\n2. To delete")
                isFine = False
                while isFine == False:
                    try:
                        addOrDelete = int(input())
                        if addOrDelete == 1:
                            VegetablesSection.addVegetablesProduct(self.super.meat_section, self.super.Hygiene_Section,self.super.Vegetables_Section)
                            isFine = True
                        elif addOrDelete == 2:
                            VegetablesSection.bringDownVegetablesProdect(self.super.meat_section, self.super.Hygiene_Section,self.super.Vegetables_Section)
                            isFine = True
                    except:
                        print("you need to choose one of the opshin")


        elif option == 2:

            print("Which employee?\n1. Cashiers\n2. Ushers")
            whichEmployee = int(input())
            if whichEmployee == 1:
                print("1. To add\n2. To bring down")
                addOrDelet = int(input())
                if addOrDelet == 1 or addOrDelet == 2:
                    print("צריך להכין מתודה של להוריד או להעלות עובדים")
            if whichEmployee == 2:
                print("--Ushers--\n1. To add\n2. To bring down")
                addOrDeletUsher = int(input())
                isFine = False
                # while isF…