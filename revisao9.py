import os
def limpar():
    os.system("cls")
limpar()



class Pessoa:
    def __init__(self, nome):
        self.nome = nome


class Aluno(Pessoa):
    def estudar(self):
        print(f"{self.nome}, está estudando")


a = Aluno("Lucas")
a.estudar()