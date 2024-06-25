from typing import List

from python_super_project.DataModels.Product import Product


class Section:
    def __init__(self, products_in_section):
        self.products: List[Product] = products_in_section


