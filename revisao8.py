import os
def limpar():
    os.system("cls")
limpar()




class Animal:
    def __init__(self, nome):
     self.nome = nome

    def falar(self):
        print(f" Som")


class Pato(Animal):
    def falar(self):
        print(f"{self.nome} disse Quack")

class Vaca(Animal):
    def falar(self):
     print(f"{self.nome} disse muu")




p = Pato("yuri")
p.falar()

v = Vaca("Rafael")
v.falar()