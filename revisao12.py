import os
def limpar():
    os.system("cls")
limpar()



class Animal:
    def falar(self):
        print("Som")


class Gato(Animal):
    def falar(self):
        print("Miau")


class Cachorro(Animal):
    def falar(self):
        print("Au au")


animais = [Gato, Cachorro]

for a in animais:
    obj = a()
    obj.falar()