from python_super_project.DataModels.Employee import Usher
from python_super_project.UI import SuperMain_UI


class Super:
    def __init__(self):
        self.sections = []
        self.pro = []
        self.usher = []
        self.clients = []

    def load_Entitys(self):

        # self.clients.append(Client())
        # self.clients.append(Client())
        # self.clients.append(Client())
        # self.clients.append(Client())
        #
        #
        # self.products.append(Product())

        usher1 = Usher.Usher("yisca rosenblatt", 327721288, 19, 585343487, 0, 520027)
        usher2 = Usher.Usher("rosenblatt", 596, 19, 585343487, 1, 123)
        self.usher.append(usher1)
        self.usher.append(usher2)



    def open (self):
        self.load_Entitys()
        SuperMain_UI.SuperMain_UI(self).show()





