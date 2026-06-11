# Exercicio - Crie uma aplicação que faça o cálculode idade de pessoas.
# Deve perguntar o nome da pessoa e o ano de nascimento.

import tkinter as tk
from tkinter import messagebox
def calcular_idade():
    nome = entry_nome.get()
    ano_nascimento = entry_ano_nascimento.get()
    if nome == "" and ano_nascimento == "":
        messagebox.showerror("Bem-vindo", "Digite seu nome e ano de nascimento.")
    else:
        idade = 2026 - int(ano_nascimento)
        messagebox.showinfo("Idade Calculada", f"Olá {nome}! Sua idade é {idade} anos.")


janela = tk.Tk()
janela.title("Calculadora de Idade")
janela.geometry("400x300")
janela.configure(bg="purple")

lbl_nome = tk.Label(janela, text="Digite seu nome:", bg="purple", font=("Arial", 14), fg="black")
lbl_nome.grid(row=0, column=0, pady=10, padx=10)
lbl_ano_nascimento = tk.Label(janela, text="Digite seu ano de nascimento:", bg="purple" ,font=("Arial", 14), fg="black")
lbl_ano_nascimento.grid(row=2, column=0, pady=10, padx=10)

entry_nome = tk.Entry(janela, bg="white", font=("Arial", 14), width=30)
entry_nome.grid(row=1, column=0, pady=10, padx=10)
entry_ano_nascimento = tk.Entry(janela, bg="white", font=("Arial", 14), width=30)
entry_ano_nascimento.grid(row=3, column=0, pady=10, padx=10)

btn_calcular_idade = tk.Button(janela, text="Calcular Idade", font=("Arial", 14), fg="black", command=calcular_idade)
btn_calcular_idade.grid(row=4, column=0, pady=10, padx=10)
btn_fechar = tk.Button(janela, text="Fechar", font=("Arial", 14), fg="black", command=janela.destroy)
btn_fechar.grid(row=5, column=0, pady=10, padx=10)

janela.mainloop()

