import os
def limpar():
    os.system("cls")


from rich import print  # py -m pip install rich
from rich.panel import Panel


class Churrasco:

    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.quant = quant

    def mostrar(self):
        return f"Esse é {self.titulo} com {self.quant} pessoas participando"

    def analisar(self):
        conteudo = f"Analisando {self.titulo} com {self.quant} participantes"
        painel = Panel(conteudo, title=self.titulo)
        print(painel)


c1 = Churrasco("Churrasco do TI", 11)
c1.analisar()
