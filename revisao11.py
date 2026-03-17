import os
def limpar():
    os.system("cls")
limpar()


class Produto:
    
    def __init__(self, preco):
        self._preco = preco


p = Produto(100)
p._preco = -200
print(p.__preco)