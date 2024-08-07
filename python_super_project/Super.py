# In Super.py

from python_super_project.Sections.HygieneSection import HygieneSection
from python_super_project.Sections.MeatSection import MeatSection
from python_super_project.Sections.VegetablesSection import VegetablesSection
from python_super_project.UI.SuperMain_UI import SuperMain_UI
from colorama import Fore


class Super:
    def __init__(self):
        self.cashiers = []
        self.ushers = []
        self.Customers = []
        self.load_entities()
        self.meat_section = MeatSection()
        self.Hygiene_Section = HygieneSection()
        self.Vegetables_Section = VegetablesSection()


    def load_entities(self):
        print('Loading entities...')

    def open(self):
        print("Opening SuperMain_UI...")
        self.meat_section.craectmeatProducts()
        self.Hygiene_Section.craectHigieneProducts()
        self.Vegetables_Section.craectmeatVegetablesProducts()
        SuperMain_UI(self).show()
