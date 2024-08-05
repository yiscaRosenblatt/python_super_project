from python_super_project.DataModels.Product.Product import Product
from python_super_project.Sections.Section import Section


class MeatProduct(Product):
    pass

ChickenBreast = MeatProduct("Chicken Breast", 60, (2025, 5, 1))
ChickenWings = MeatProduct("Chicken wing", 25, (2025, 1, 2))
Hotdog = MeatProduct("hot dog", 15, (2024, 12, 22))
SpringChicken = MeatProduct("spring chicken", 54, (2025, 6, 23))
Mince = MeatProduct("Mince", 30, (2025, 4, 8))


