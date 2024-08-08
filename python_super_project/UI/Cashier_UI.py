from python_super_project.DataModels.Customer import Customer
from python_super_project.Sections.HygieneSection import HygieneSection
from python_super_project.Sections.MeatSection import MeatSection
from python_super_project.Sections.VegetablesSection import VegetablesSection


class Cashier_UI:

    def __init__(self, super_main_ui):
        self.super_main_ui = super_main_ui

    # print("hello cashier. Choose your option:\n ")



    def showForCustomer(self, cashier, customer: Customer):

        try:
            print(f"Hello, I am {cashier.name} and I will be your Cashier.")
            while True:
                print(
                    "Which section did you visit? (Press Q to finish, B to go back)\n1. Hygiene\n2. Meat\n3. Vegetables")
                choosSection = input().strip()

                if choosSection.upper() == 'Q':
                    print("Finishing checkout process. Thank you!")
                    break
                elif choosSection.upper() == 'B':
                    print("Going back to section selection.")
                    continue

                try:
                    choosSection = int(choosSection)
                except ValueError:
                    print("Invalid input. Please enter a number corresponding to a section.")
                    continue

                if choosSection == 1:
                    hygiene_section = HygieneSection()
                    products = hygiene_section.HygieneSection
                elif choosSection == 2:
                    meat_section = MeatSection()
                    products = meat_section.MeatSection
                elif choosSection == 3:
                    veg_section = VegetablesSection()
                    products = veg_section.VegetablesSection
                else:
                    print("Invalid section. Please choose again.")
                    continue

                print("Which Product?")
                print("   product          price")
                for i, product in enumerate(products, 1):
                    print(f"{i}. {product.name}   -   {product.price}")

                product_index = input().strip()
                if product_index.upper() == 'Q':
                    print("Finishing checkout process. Thank you!")
                    break
                elif product_index.upper() == 'B':
                    print("Going back to section selection.")
                    continue

                try:
                    product_index = int(product_index) - 1
                    if product_index < 0 or product_index >= len(products):
                        print("Invalid product selection. Please choose again.")
                        continue
                except ValueError:
                    print("Invalid input. Please enter a valid product number.")
                    continue

                print("How much to add?")
                amount = input().strip()
                if amount.upper() == 'Q':
                    print("Finishing checkout process. Thank you!")
                    break
                elif amount.upper() == 'B':
                    print("Going back to section selection.")
                    continue

                try:
                    amount = int(amount)
                except ValueError:
                    print("Invalid input. Please enter a valid amount.")
                    continue

                customer.add_product(products[product_index].name, amount, products[product_index].price, products[product_index])

            customer.finesh()

        except Exception as e:
            print(f"An error occurred: {e}")


        self.super_main_ui.show()



    # def showForCustomer(cashier):
    #     print(f"hello i {cashier.name} and i will be your Cashier")
    #     print("which section you went to buy?(prees Q to finish)\n1. Hygiene\n2. Meat\n3. Vegetables")
    #     choosSection = int(input())
    #     print("Which Product?")
    #     print("   product          price")
    #     if choosSection == 1:
    #         print(f"1. Toilet Paper   -   {HygieneSection().HygieneSection[0].price}\n2. Wipes   -   {HygieneSection().HygieneSection[1].price}\n3. Ear stick   -   {HygieneSection().HygieneSection[2].price}\n4. toothpicks   -   {HygieneSection().HygieneSection[3].price}\n5. Soap   -   {HygieneSection().HygieneSection[4].price}")
    #         product_index = int(input()) - 1
    #         print("how much to add?")
    #         amount = int(input())
    #         Customer.add_product_hygiene(HygieneSection(), HygieneSection().HygieneSection[product_index].name, amount, HygieneSection().HygieneSection[product_index].price)
        #     Higiene_Section.addHigieneproduct(Higiene_Section, product_index, amount)
        #
        # elif section == 2:
        #     print("Which Product?\n1. Chicken Breast\n2. Chicken Wings\n3. Hotdog\n4. Mince\n5. Spring Chicken")
        #     product_index = int(input()) - 1
        #     print("how much to add?")
        #     amount = int(input())
        #     meat_section.add_product(meat_section, product_index, amount)
        #
        # elif section == 3:
        #     print("Which Product?\n1. tomato\n2. cucumber\n3. Potato\n4. sweet potato\n5. cabbage")
        #     product_index = int(input()) - 1
        #     print("how much to add?")
        #     amount = int(input())
        #     Vegetables_Section.addVegetablesProduct(Vegetables_Section, product_index, amount)