import os
def limpar():
    os.system("cls")
limpar()



class Pessoa:
    def __init__(self, nome):
        self.nome = nome


class Professor(Pessoa):

    def ensinar(self):
        print(self.nome, "ensina")


prof = Professor("Girafales")
prof.ensinar()