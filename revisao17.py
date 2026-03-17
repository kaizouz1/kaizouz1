import os
def limpar():
    os.system("cls")
limpar()



class Conta:
    def __init__(self, saldo):
        self.__saldo = saldo

    def set_saldo(self, valor):
        if valor >= 0:
            self.__saldo += valor
        print(self.__saldo)


c = Conta(100)
c.set_saldo(-50)
print(c.set_saldo)