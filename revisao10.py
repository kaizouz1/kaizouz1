import os
def limpar():
    os.system("cls")
limpar()


class Animal:
    def __init__(self, nome):
        self.nome = nome


class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f"{self.nome} Au au")


animais = [Cachorro("Bolt")]

for a in animais:
 a.falar()