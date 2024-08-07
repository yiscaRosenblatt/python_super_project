from typing import List
from python_super_project.DataModels.Product.Date import Date
from python_super_project.DataModels.Product.MeatProduct import MeatProduct
# from python_super_project.Sections.Section import Section


class MeatSection:
    def __init__(self):
        self.MeatProduct = MeatProduct
        self.MeatSection: List[MeatProduct] = []
        self.craectmeatProducts()

    def craectmeatProducts(self):
        self.MeatSection.append(MeatProduct("Chicken Breast", 50, 60, Date(2025, 5, 1)))
        self.MeatSection.append(MeatProduct("Chicken wing", 50, 25, Date(2025, 1, 2)))
        self.MeatSection.append(MeatProduct("hot dog", 50, 15, Date(2024, 12, 22)))
        self.MeatSection.append(MeatProduct("spring chicken", 50, 54, Date(2025, 6, 23)))
        self.MeatSection.append(MeatProduct("Mince", 50, 30, Date(2025, 4, 8)))

    @staticmethod
    def add_product(self, product_index: int, amount: int):
        if 0 <= product_index < len(self.MeatSection):
            self.MeatSection[product_index].amount += amount
            print(
                f"Added {amount} {self.MeatSection[product_index].name}. New amount: {self.MeatSection[product_index].amount}")
        else:
            print("Invalid product index.")

    @staticmethod
    def bringDownMeatProdect(self, product_index: int, amount: int):
        if 0 <= product_index < len(self.MeatSection):
            self.MeatSection[product_index].amount -= amount
            print(
                f"bring Down {amount} {self.MeatSection[product_index].name}. New amount: {self.MeatSection[product_index].amount}")
        else:
            print("Invalid product index.")