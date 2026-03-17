import os
def limpar():
    os.system("cls")
limpar()



class Animal:
    def __init__(self, nome):
        self.nome = nome


class Vaca(Animal):
    def falar(self):
        print(self.nome, "faz muuu")


v = Vaca("Yurigagaia")
v.falar()