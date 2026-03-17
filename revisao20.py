import os
def limpar():
    os.system("cls")
limpar()


class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print("Som")


class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)
        self.raca = raca

    def falar(self):
        print("Au au")


animais = [Cachorro("Bolt", "Labrador")]

for a in animais:
    a.falar()