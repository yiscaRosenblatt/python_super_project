from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name: str, ID: int, age: int, phon: str):
        self.name = name
        self.ID = ID
        self.age = age
        self.phon = phon


    def __str__(self):
        pass

    def __eq__(self, other):
        pass


