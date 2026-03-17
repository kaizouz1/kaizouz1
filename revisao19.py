import os
def limpar():
    os.system("cls")
limpar()



class Produto:
    def __init__(self, preco):
        self.__preco = preco

    def set_preco(self, valor):
        if valor >= 0:
            self.__preco += valor
        print(self.__preco)


p = Produto(300)
p.set_preco(-200)
print(p.set_preco)