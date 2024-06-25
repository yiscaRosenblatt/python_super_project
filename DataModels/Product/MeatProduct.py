from python_super_project.DataModels.Product.Product import Product
from python_super_project.Sections.Section import Section


class MeatProduct(Product):
    def __init__(self,price, ID, name, date):
        super().__init__(price, ID, name)

