from typing import List

from python_super_project.DataModels.Product.Product import Product
from python_super_project.DataModels.Receipt import Receipt



class Customer:
    def __init__(self, name: str):
        self.name = name
        self.totalPaid = 0
        self.receipts: List[Receipt] = []

    def addCustomer(Customer, Customers:list):
        Customers.append(Customer)


    def add_product(self, name: str, amount: int, price_of_one: float, prodect: Product):
        if prodect.amount < amount:
            print(f"ther is onle {prodect.amount} did you went to odd them?\n1. no\n2. yes")
            answer = int(input())
            if answer == 1:
                return
            if answer == 2:
                self.receipts.append(Receipt(name, prodect.amount, price_of_one, prodect.amount * price_of_one))
                self.totalPaid += prodect.amount * price_of_one
                prodect.amount = 0
        else:
            self.receipts.append(Receipt(name, amount, price_of_one, amount * price_of_one))
            self.totalPaid += amount * price_of_one
            prodect.amount -= amount






    def finesh(self):
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
        print("name       amount        price Of One        final Price")
        for product in self.receipts:
            print(f"{product.nameProduct}   -   {product.amount}      -      {product.priceOfOne}      -       {product.finalPrice}")

        print(f"\ntotalPaid = {self.totalPaid}")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
