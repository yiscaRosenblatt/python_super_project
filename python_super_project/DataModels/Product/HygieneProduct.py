from python_super_project.DataModels.Product.Date import Date
from python_super_project.DataModels.Product.Product import Product
from python_super_project.Sections.Section import Section


class HygieneProduct(Product):
    def __init__(self, name: str, amount: int, price: int, date: Date):
        super().__init__(name, amount, price, date)
        self.name = name
        self.amount = amount
        self.price = price
        self.date = date