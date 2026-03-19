class Pessoa:
            def __init__(self, nome, idade, cidade, profissao):
                self.nome = input("Digite o nome: ")
                self.idade = input("Digite sua idade:")
                self.profissao = input("Digite sua profissao: ")
                self.cidade = input("Digite sua cidade: ")
    
            def apresentar(self):
                print(f"eu me chamo {self.nome} e tenho {self.idade} anos. Sou um {self.profissao} e moro na cidade de {self.cidade}")

            

            def mensagem2(self):
                print(f"eu me chamo {self.nome} e tenho {self.idade} anos. Sou um {self.profissao} e moro na cidade de {self.cidade}")
            
pessoa1 = Pessoa("Carlos", 25, "Vitoria", "programador")
pessoa1.apresentar()

        