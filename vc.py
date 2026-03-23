def depositar(self):
    saldo2 = float(input(f"Quantos reais deseja depositar sr(a) {self.titular}: "))
    self.saldo += saldo2
    print(f"Depósito de R$ {saldo2:.2f} realizado com sucesso!")
valor = float(input("Quanto deseja depositar: "))
banco1.depositar(valor)