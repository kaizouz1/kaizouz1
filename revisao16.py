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


g = Gato()
g.falar()