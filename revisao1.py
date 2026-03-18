import os


def limpar():
    os.system("cls")


limpar()


class Animal:
    def __init__(self, nome):
        self.nome = nome


class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)  # chama o construtor da classe pai
        self.raca = raca


c = Cachorro("Bolt", "Labrador")
print(c.nome)
print(c.raca)
