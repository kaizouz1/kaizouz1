import os
def limpar():
    os.system("cls")
limpar()


class Conta:
    def __init__(self, saldo):
        self.__saldo = saldo

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        return self.__saldo


c = Conta(500)
print(c.sacar(100))