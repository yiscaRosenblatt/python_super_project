from typing import List

from python_super_project.DataModels.Product.Date import Date
from python_super_project.DataModels.Product.HygieneProduct import HygieneProduct


class HygieneSection:

    def __init__(self):
        self.HygieneSection: List[HygieneProduct] = []
        self.craectHigieneProducts()

    def craectHigieneProducts(self):
        self.HygieneSection.append(HygieneProduct("Toilet Paper", 50, 42, Date(2025, 5, 1)))
        self.HygieneSection.append(HygieneProduct("Wipes", 50, 10, Date(2025, 1, 2)))
        self.HygieneSection.append(HygieneProduct("Ear stick", 50, 2, Date(2024, 12, 22)))
        self.HygieneSection.append(HygieneProduct("toothpicks", 50, 6, Date(2025, 6, 23)))
        self.HygieneSection.append(HygieneProduct("Soap", 50, 20, Date(2025, 4, 8)))

    @staticmethod
    def addHigieneproduct(self, product_index: int, amount: int):
        if 0 <= product_index < len(self.HygieneSection):
            self.HygieneSection[product_index].amount += amount
            print(
                f"Added {amount} {self.HygieneSection[product_index].name}. New amount: {self.HygieneSection[product_index].amount}")
        else:
            print("Invalid product index.")

    @staticmethod
    def bringDownMeatProdect(self, product_index: int, amount: int):
        if 0 <= product_index < len(self.HygieneSection):
            if self.HygieneSection[product_index].amount >= amount:
                self.HygieneSection[product_index].amount -= amount
                print(
                    f"Decreased {amount} {self.HygieneSection[product_index].name}. New amount: {self.HygieneSection[product_index].amount}")
            else:
                print(f"Not enough {self.HygieneSection[product_index].name} in stock to decrease by {amount} ther is {self.HygieneSection[product_index].amount}.")
                return
        else:
            print("Invalid product index.")