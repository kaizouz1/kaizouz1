import os
def limpar():
    os.system("cls")
limpar()

class Conta:
 def __init__(self, saldo):
    self.__saldo = saldo

 def depositar(self, valor):
    if valor > 0:
     self.__saldo += valor
    print(self.__saldo)


conta = Conta(1000)
conta.depositar(-500)
print(conta.depositar)