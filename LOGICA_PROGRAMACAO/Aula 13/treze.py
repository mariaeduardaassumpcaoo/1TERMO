# revisão Tkinter

import tkinter as tk
from tkinter import messagebox, ttk

# DEF funções em bloco
def cadastrar_usuario():
    #.get
    nome_usuario = entry_nome_usuario.get()
    curso_usuario = entry_curso_usuario2.get()
    nome_escola = cmb_nome_escola.get()

    if nome_usuario == "" and curso_usuario == "" and nome_escola == "":
        messagebox.showerror("Bem-vindo", "Digite seu nome, curso e selecione sua escola.")
    else:
        messagebox.showinfo("Bem-vindo", f"olá {nome_usuario}! seu curso E {curso_usuario} e sua escola é {nome_escola}.")

# 0 - Etapa Janela
janela = tk.Tk()
janela.title("revisão Tkinter")
janela.geometry("400x400")
janela.configure(bg="pink")

# 1 - Etapa Componentes 
lbl_nome_usuario = tk.Label(janela, text="Digite seu nome.:", bg="pink",font=("Arial", 14), fg="black")
lbl_nome_usuario.grid(row=0, column=0, pady=10, padx=10)
lbl_curso_usuario2 = tk.Label(janela, text="Digite seu curso.:", bg="pink",font=("Arial", 14), fg="black")
lbl_curso_usuario2.grid(row=8, column=0, pady=10, padx=10)

# Entrys = Caixa de texto antigos input
entry_nome_usuario = tk.Entry(janela, font=("Arial", 14), width=30)
entry_nome_usuario.grid(row=2, column=0, pady=10, padx=10)
entry_curso_usuario2 = tk.Entry(janela, font=("Arial", 14), width=30)
entry_curso_usuario2.grid(row=10, column=0, pady=10, padx=10)
lbl_nome_escola = tk.Label(janela, text="Selecione sua escola.:", bg="pink",font=("Arial", 14), fg="black")
lbl_nome_escola.grid(row=12, column=0, pady=10, padx=10)

# ComboBox = Caixa de seleção
cmb_nome_escola = ttk.Combobox(janela, values=["SESI05", "SESI408"])
cmb_nome_escola.grid(row=14, column=0, pady=10, padx=10)

# Botões de clique
btn_realizar_cadastro = tk.Button(janela, text="Cadastrar", font=("Arial", 14), fg="Pink", command=cadastrar_usuario)
btn_realizar_cadastro.grid(row=16, column=0, pady=10, padx=10)
btn_fechar_janela = tk.Button(janela, text="Fechar", command=janela.destroy, font=("Arial", 14), fg="Pink")
btn_fechar_janela.grid(row=18, column=0, pady=10, padx=10)


    



# 4 - Etapa Loop
janela.mainloop()

