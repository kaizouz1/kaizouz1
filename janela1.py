import os
def limpar():
    os.system("cls")
limpar()

import tkinter as tk # Importa a biblioteca tkinter e dá o apelido "tk"

# 1. cria a janela principal
janela = tk.Tk() # Cria a janela principal da aplicação
janela.title("Absolute Cinema") # Define o titulo da janela
janela.geometry("400x500") # Define o tamanho da janela(Largura x Altura)


# 2. Adicionar um rótulo (Label)
label = tk.Label(janela, text="Yurigagaia, o Satoru Gojo morreu para o Ryomen Sukuna, chore.", font=("Arial", 15)) # Cria um texto ("Label") dentro da janela
label.pack(pady=20) # Posiciona o label na janela com espaçamento vertical de 20 pixels

# 3. Adicionar um botão
botao = tk.Button(
    janela, # Define a janela onde o botao será colocado
    text="Chorar", # Texto exibido no botão
    command=lambda: label.config(text="Chorando!") # Define a ação ao clicar (muda o texto do label)
)
botao.pack() #Posiciona o botão na janela

# 4. Iniciar o loop inicial
janela.mainloop() # Mantém a janela aberta e rodando (escutando eventos)