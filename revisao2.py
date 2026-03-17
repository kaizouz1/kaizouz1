import os
def limpar():
    os.system("cls")
limpar()


class Conta:
    def __init__(self, saldo):
     self._saldo = saldo


    def sacar(self, valor):
        if valor <= self.__saldo:
            self._saldo -= valor
           

conta = Conta(1000)
print(conta._saldo)