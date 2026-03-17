import os
def limpar():
    os.system("cls")
limpar()

class Animal:
    def falar(self):
        print("Som")


class Cachorro(Animal):
    def falar(self):
        print("Au au")


class Gato(Animal):
    def falar(self):
        print("Miau")


animais = [Cachorro(), Gato()]

for a in animais:
    a.falar()