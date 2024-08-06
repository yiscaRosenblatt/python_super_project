from python_super_project.DataModels.Product import Date
from python_super_project.DataModels.Product.Product import Product


class MeatProduct(Product):

    def __init__(self, name: str, amount: int, price: int, date: Date):
        super().__init__(name, amount, price, date)
        self.name = name
        self.amount = amount
        self.price = price
        self.date = date

    @staticmethod
    def loadMeatProduct(self):
        ChickenBreast = MeatProduct("Chicken Breast", 50, 60, Date.Date(2025, 5, 1))
        ChickenWings = MeatProduct("Chicken wing", 50, 25, Date.Date(2025, 1, 2))
        Hotdog = MeatProduct("hot dog", 50, 15, Date.Date(2024, 12, 22))
        SpringChicken = MeatProduct("spring chicken", 50, 54, Date.Date(2025, 6, 23))
        Mince = MeatProduct("Mince", 50, 30, Date.Date(2025, 4, 8))

