from python_super_project import Super
from python_super_project.DataModels.Employee.Employee import Employee


class Cashier(Employee):

    def __init__(self, name: str, ID: int, age: int, phon: str, numberCashier: int, password: int):
        super().__init__(name, ID, age, phon)
        self.numberCashier = numberCashier
        self.isAvailable = True
        self.password = password
    @staticmethod
    def loadCashier(super):
        Cashier1 = Cashier("Daniel", 327721288, 19, "0585343487", 0, 520027)
        Cashier2 = Cashier("rosenblatt", 596, 19, "0585343487", 1, 123)
        super.cashiers.append(Cashier1)
        super.cashiers.append(Cashier2)

    @staticmethod
    def CashierAvailable(cashiers: list):
        for cashier in cashiers:
            if cashier.isAvailable == True:
                cashier.isAvailable == False
                return {"status": True, "cashier": cashier}
        return {"status": False, "cashier": None}