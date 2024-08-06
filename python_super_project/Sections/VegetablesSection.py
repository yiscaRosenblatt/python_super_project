from typing import List

from python_super_project.DataModels.Product.Date import Date
from python_super_project.DataModels.Product.VegetablesProduct import VegetablesProduct


class VegetablesSection:

    def __init__(self):
        self.VegetablesProduct = VegetablesProduct
        self.VegetablesSection: List[VegetablesProduct] = []

    def craectmeatVegetablesProducts(self):
        self.VegetablesSection.append(VegetablesProduct("tomato", 50, 1, Date(2025, 5, 1)))
        self.VegetablesSection.append(VegetablesProduct("cucumber", 50, 1, Date(2025, 1, 2)))
        self.VegetablesSection.append(VegetablesProduct("Potato", 50, 1, Date(2024, 12, 22)))
        self.VegetablesSection.append(VegetablesProduct("sweet potato", 50, 1, Date(2025, 6, 23)))
        self.VegetablesSection.append(VegetablesProduct("cabbage", 50, 2, Date(2025, 4, 8)))

    @staticmethod
    def addVegetablesProduct(self, product_index: int, amount: int):
        if 0 <= product_index < len(self.VegetablesSection):
            self.VegetablesSection[product_index].amount += amount
            print(
                f"Added {amount} {self.VegetablesSection[product_index].name}. New amount: {self.VegetablesSection[product_index].amount}")
        else:
            print("Invalid product index.")

    @staticmethod
    def bringDownVegetablesProdect(self, product_index: int, amount: int):
        if 0 <= product_index < len(self.VegetablesSection):
            self.VegetablesSection[product_index].amount -= amount
            print(
                f"bring Down {amount} {self.VegetablesSection[product_index].name}. New amount: {self.VegetablesSection[product_index].amount}")
        else:
            print("Invalid product index.")
