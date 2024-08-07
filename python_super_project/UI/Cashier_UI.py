from python_super_project.DataModels.Customer import Customer
from python_super_project.Sections.HygieneSection import HygieneSection
from python_super_project.Sections.MeatSection import MeatSection
from python_super_project.Sections.VegetablesSection import VegetablesSection


class Cashier_UI:

    def __init__(self):
        pass

    # print("hello cashier. Choose your option:\n ")

    def show(self):
        pass

    def showForCustomer(self, cashier, customer: Customer):
        print(f"hello I am {cashier.name} and I will be your Cashier")
        print("Which section did you visit? (Press Q to finish)\n1. Hygiene\n2. Meat\n3. Vegetables")
        choosSection = int(input())
        print("Which Product?")
        print("   product          price")
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

        for i, product in enumerate(products, 1):
            print(f"{i}. {product.name}   -   {product.price}")
        product_index = int(input()) - 1
        print("How much to add?")
        amount = int(input())

        if choosSection == 1:
            customer.add_product(products[product_index].name, amount, products[product_index].price, products[product_index])
        elif choosSection == 2:
            customer.add_product(products[product_index].name, amount, products[product_index].price, products[product_index])
        elif choosSection == 3:
            customer.add_product(products[product_index].name, amount, products[product_index].price, products[product_index])

        customer.finesh()





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