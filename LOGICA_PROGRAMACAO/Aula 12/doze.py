# TKINTER

# Componentes Widgets
# tk: Tk() # Janela
# lb: Label() # Rótulo
# bt: Button() # Botão
# et: Entry () # Caixa de texto

# import tkinter as tk
# from tkinter import messagebox

# # 1. Criar a janela principal
# janela = tk.Tk()
# janela.title("Minha primeira janela GUI")
# janela.configure(bg="#ffccd7") # Cor de fundo
# janela.geometry("400x200") #Largura x Altura

# # 2. Criar a função do botão (evento)
# def mostrar_mensagem():
#     messagebox.showinfo("Sucesso!", "Você clicou no botão")

# # 3. Criar os componentes
# lbl_titulo = tk.Label(janela, text="Bem-vindo a nossa aula de Tkinter", font=("Arial", 14, "bold"))
# btn_clique = tk.Button(janela, text="Clique aqui", font=("Arial", 11), bg="#da1959", fg="white", command=mostrar_mensagem)
# btn_close = tk.Button(janela, text="Fechar", font=("Arial", 14, "bold"), bg="#cce2ee", command=janela.destroy)

# # 4. Posicionar os componentes
# lbl_titulo.pack(pady=20) # 'pady' adiciona um espaçamento vertical
# btn_clique.pack(pady=10)
# btn_close.pack(pady=5)


# # 5. Rodar o loop da interface
# janela.mainloop()

# import tkinter as tk
# from tkinter import messagebox
# def saudar_usuario():
#     # .get() serve para buscar o texto que vamos digitar


#     nome= campo_nome.get()

#     if nome == "":
#         messagebox.showwarning("Aviso", "Por favor", "Digite seu nome!")
#     else:
#         messagebox.showinfo("Saudações Alunos", f"Olá, {nome}! Seja bem-vindo ao mundo das interfaces gráficas")

# # configurações da janela
# app = tk.Tk()
# app.title = ("Exemplo 1")
# app.geometry("350x200")

# # Componentes
# ibl_instrucao = tk.Label(app, text="Digite seu nome abaixo:")
# ibl_instrucao.pack(pady=5)

# campo_nome = tk.Entry(app, font=("Arial", 12))
# campo_nome.pack(pady=5)

# btn_enviar = tk.Button(app, text="enviar", command=saudar_usuario)
# btn_enviar.pack(pady=15)

# app.mainloop()

# Exercicio: Crie uma interface gráfica que calcule a média de três notas digitadas pelo usuario. A interface deve conter campos para o usuario inserir as notas e um botao para calcular a média. Ao clicar no botão, a média deve ser exibida em uma mensagem.


import tkinter as tk
from tkinter import messagebox


janela = tk.Tk()
janela.title("Seja bem-vindo a Gráfica")
janela.configure(bg="#ffccd7") # Cor de fundo
janela.geometry("400x300") #Largura x Altura

# def mostrar_mensagem():
#     messagebox.showinfo("Sucesso!", "Você clicou no botão")

# lbl_titulo = tk.Label(janela, text="Bem-vindo a nossa gráfica", font=("Arial", 14, "bold"))
# btn_clique = tk.Button(janela, text="Clique aqui", font=("Arial", 11), bg="#da1959", fg="white", command=mostrar_mensagem)
# btn_close = tk.Button(janela, text="Fechar", font=("Arial", 14, "bold"), bg="#cce2ee", command=janela.destroy)

# lbl_titulo.pack(pady=20)
# btn_clique.pack(pady=10)

def calcular_media():

    media1 = float(media_total1.get())
    media2 = float(media_total2.get())
    media3 = float(media_total3.get())
 
    media_total = (media1 + media2 + media3) / 3
 
    if media_total >= 7:
        resultado = "Aprovado"
        messagebox.showinfo("Resultado", f"Média: {media_total:.2f}\nSituação: {resultado}")
    else:
        resultado = "Reprovado"
        messagebox.showerror("Erro", "Por favor, digite apenas números nas três notas.")

janela = tk.Tk()
janela.title = ("Exemplo 1")
janela.geometry("1000x800")


lbl_media1 = tk.Label(janela, text="Digite a sua primeira média abaixo: ")
lbl_media1.pack(pady=5)

lbl_media2 = tk.Label(janela, text="Digite a sua segunda média abaixo: ")
lbl_media2.pack(pady=5)

lbl_media3 = tk.Label(janela, text="Digite a sua terceira média abaixo: ")
lbl_media3.pack(pady=5)


media_total1 = tk.Entry(janela, font=("Arial", 12))
media_total1.pack(pady=5)


media_total2 = tk.Entry(janela, font=("Arial", 12))
media_total2.pack(pady=5)


media_total3 = tk.Entry(janela, font=("Arial", 12))
media_total3.pack(pady=5)

botao_calcular = tk.Button(janela, text="Calcular Média", command=calcular_media)
botao_calcular.pack(pady=15)

janela.mainloop()