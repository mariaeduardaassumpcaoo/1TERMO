# 1- Exercicio 1
# import tkinter as tk 
# from tkinter import messagebox, ttk

# def cadastrar_usuario():
#     nome = entry_nome_operador.get()
#     turno = entry_turno_operador.get()

#     if not nome or not turno:
#         messagebox.showerror("Bem-Vindo", "Digite seu nome e turno.")
#         return

#     if turno.upper() not in ["A", "B", "C"]:
#         messagebox.showerror("Erro", "Turno inválido. Digite A, B ou C.")
#         return

#     messagebox.showinfo("Sucesso", f"Usuário cadastrado com sucesso!\nNome: {nome}\nTurno: {turno.upper()}")

# janela = tk.Tk()
# janela.title("Exercicio 1")
# janela.geometry("400x400")
# janela.configure(bg="pink")

# lbl_nome_operador = tk.Label(janela, text="Digite seu nome.:")
# lbl_nome_operador.grid(row=0, column=0, pady=10, padx=10)
# lbl_turno_operador = tk.Label(janela, text="Digite se seu turno é A, B ou C.:")
# lbl_turno_operador.grid(row=8, column=0, pady=10, padx=10)

# entry_nome_operador = tk.Entry(janela, font=("Arial", 14), width=30)
# entry_nome_operador.grid(row=2, column=0, pady=10, padx=10)
# entry_turno_operador = tk.Entry(janela, font=("Arial", 14), width=30)
# entry_turno_operador.grid(row=10, column=0, pady=10, padx=10)

# btn_realizar_cadastro = tk.Button(janela, text="Cadastrar", font=("Arial", 14), fg="Pink", command=cadastrar_usuario)
# btn_realizar_cadastro.grid(row=16, column=0, pady=10, padx=10)
# btn_fechar_janela = tk.Button(janela, text="Fechar", command=janela.destroy, font=("Arial", 14), fg="Pink")
# btn_fechar_janela.grid(row=18, column=0, pady=10, padx=10)

# janela.mainloop()

# Exercico 2

# import tkinter as tk
# from tkinter import messagebox, ttk
# def calcular_producao():
#     quantidade_de_pecas = entry_quantidade_de_pecas.get()
#     horas_de_turno = entry_horas_de_turno.get()
#     if not quantidade_de_pecas or not horas_de_turno:
#         messagebox.showerror("Bem-Vindo", "Digite a quantidade de peças e horas de turno.")
#     else:
#         producao_por_hora = int(quantidade_de_pecas) * int(horas_de_turno)
#         messagebox.showinfo("Producao Calculada", f"A produção é de {producao_por_hora} peças por hora.")

# janela = tk.Tk()
# janela.title("Exercicio 2")
# janela.geometry("400x400")
# janela.configure(bg="pink")

# lbl_quantidade_de_pecas = tk.Label(janela, text="Digite a quantidade de peças.:")
# lbl_quantidade_de_pecas.grid(row=0, column=0, pady=10, padx=10)
# lbl_horas_de_turno = tk.Label(janela, text="Digite as horas de turno.:")
# lbl_horas_de_turno.grid(row=2, column=0, pady=10, padx=10)

# entry_quantidade_de_pecas = tk.Entry(janela, font=("Arial", 14), width=30)
# entry_quantidade_de_pecas.grid(row=1, column=0, pady=10, padx=10)
# entry_horas_de_turno = tk.Entry(janela, font=("Arial", 14), width=30)
# entry_horas_de_turno.grid(row=3, column=0, pady=10, padx=10)

# btn_calcular_producao = tk.Button(janela, text="Calcular", font=("Arial", 14), fg="pink", command = calcular_producao)
# btn_calcular_producao.grid(row=16, column=0, pady=10, padx=10)     
# btn_fechar_janela = tk.Button(janela, text="Fechar", command=janela.destroy, font=("Arial", 14), fg="pink")                                                             
# btn_fechar_janela.grid(row=18, column=0, pady=10, padx=10)

# janela.mainloop()

# Exercicio 3
# 

import tkinter as tk
from tkinter import messagebox
# from tkinter import messagebox

# def converter_pressao():
#     try:
#         pressao_bar = float(entrada_bar.get())
#         pressao_psi = pressao_bar * 14.5
       
#         messagebox.showinfo("Resultado", f"A pressão é de {pressao_psi} PSI")
#     except ValueError:
#         messagebox.showerror("Erro", "Digite um valor correto.")

# janela = tk.Tk()
# janela.title("Conversor Bar para PSI")
# janela.geometry("400x500")
# janela.configure(bg="pink")

# lbl_bar = tk.Label(janela, text="Digite a pressão em Bar:", font=("Arial", 14), fg="white", bg="pink")
# lbl_bar.grid(row=0, column=0, pady=10, padx=10)

# entrada_bar = tk.Entry(janela, font=("Arial", 14), width=30)
# entrada_bar.grid(row=2, column=0, pady=10, padx=10)

# btn_converter = tk.Button(janela, text="Converter", font=("Arial", 14), fg="white", bg="pink", command=converter_pressao)
# btn_converter.grid(row=15, column=0, pady=10, padx=10)

# janela.mainloop()

# Exercicio 4

# import tkinter as tk
# from tkinter import messagebox

# def calcular_media():

#     media1 = float(media_total1.get())
#     media2 = float(media_total2.get())
#     media3 = float(media_total3.get())
 
#     media_total = (media1 + media2 + media3) / 3
 
#     if media_total >= 7:
#         resultado = "Aprovado"
#         messagebox.showinfo("Resultado", f"Média: {media_total:.2f}\nSituação: {resultado}")
#     else:
#         resultado = "Reprovado"
#         messagebox.showerror("Erro", "Por favor, digite apenas números nas três notas.")

# janela = tk.Tk()
# janela.title = ("Exercicio 4")
# janela.geometry("400x400")


# lbl_media1 = tk.Label(janela, text="Digite a sua primeira média abaixo: ")
# lbl_media1.pack(pady=5)

# lbl_media2 = tk.Label(janela, text="Digite a sua segunda média abaixo: ")
# lbl_media2.pack(pady=5)

# lbl_media3 = tk.Label(janela, text="Digite a sua terceira média abaixo: ")
# lbl_media3.pack(pady=5)


# media_total1 = tk.Entry(janela, font=("Arial", 12))
# media_total1.pack(pady=5)


# media_total2 = tk.Entry(janela, font=("Arial", 12))
# media_total2.pack(pady=5)


# media_total3 = tk.Entry(janela, font=("Arial", 12))
# media_total3.pack(pady=5)

# botao_calcular = tk.Button(janela, text="Calcular Média", command=calcular_media)
# botao_calcular.pack(pady=15)

# janela.mainloop()

# Exercicio 5

# import tkinter as tk
# from tkinter import messagebox

# def verificar_temperatura():
#     try:
#         temperatura = float(entrada_temp.get())

#         if temperatura < 40:
#             resultado.config(text="Baixa carga", fg="blue")
#         elif 40 <= temperatura <= 70:
#             resultado.config(text="Normal", fg="green")
#         else:
#             resultado.config(
#                 text="ALERTA: Resfriamento Ativado!",
#                 fg="red"
#             )

#     except ValueError:
#         messagebox.showerror(
#             "Erro",
#             "Digite uma temperatura válida!"
#         )


# janela = tk.Tk()
# janela.title("exercicio 5")
# janela.geometry("400x400")


# lbl_temp = tk.Label(janela, text="Digite a temperatura do motor:", font=("Arial", 14))
# lbl_temp.pack(pady=10)

# entrada_temp = tk.Entry(janela, font=("Arial", 14), width=30)
# entrada_temp.pack(pady=10)

# btn_verificar = tk.Button(janela, text="Verificar", font=("Arial", 14), command=verificar_temperatura)
# btn_verificar.pack(pady=10)

# resultado = tk.Label(janela, text="", font=("Arial", 14))
# resultado.pack(pady=10)

# janela.mainloop()

# Exercicio 6
# import tkinter as tk
# from tkinter import messagebox

# def classificar_lote():
#     codigo = entry_codido.get().strip().upper()

#     if codigo.startswith("A"):
#         resultado.config(text="Categoria: Alimentos", fg="pink")
#     elif codigo.startswith("E"):
#         resultado.config(text="Categoria: Eletrônicos", fg="pink")
#     else:
#         resultado.config(text="Categoria: Desconhecido", fg="pink")
#     messagebox.showinfo("Sua Categoria é:", f"{resultado.cget('text')}")
# janela = tk.Tk()
# janela.title("Exercicio 6")
# janela.geometry("400x400")

# lbl_codigo = tk.Label(janela, text="Digite o código do lote:", font=("Arial", 14))
# lbl_codigo.grid(row=0, column=0, padx=10, pady=10)

# entry_codido = tk.Entry(janela, font=("Arial", 14), width=30)
# entry_codido.grid(row=1, column=0, padx=10, pady=10)

# btn_classificar = tk.Button(janela, text="Classificar", font=("Arial", 14), command=classificar_lote)
# btn_classificar.grid(row=2, column=0, padx=10, pady=10)

# resultado = tk.Label(janela, text="", font=("Arial", 14))
# resultado.grid(row=3, column=0, padx=10, pady=10)

# janela.mainloop()

# Exercicio 7

# import tkinter as tk
# from tkinter import messagebox
# def verificar_porta():
#     sensor_porta = entry_porta.get().strip().lower()

#     if sensor_porta == "aberta":
#         resultado.config(text="A maquina pode ser iniciada.", fg="pink")
#     elif sensor_porta == "fechada":
#         resultado.config(text="ALERTA: A maquina não pode ser iniciada!", fg="pink")
#     else:
#         resultado.config(text="Entrada inválida. Digite 'aberta' ou 'fechada'.", fg="pink")
#     messagebox.showinfo("Resultado", f"{resultado.cget('text')}")

# janela = tk.Tk()
# janela.title("Exercicio 7")
# janela.geometry("400x400")

# lbl_porta = tk.Label(janela, text="Digite se o sensor da porta está aberto ou fechado:", font=("Arial", 14), fg="pink")
# lbl_porta.grid(row=0, column=0, padx=10, pady=10)

# entry_porta = tk.Entry(janela, font=("Arial", 14), width=30)
# entry_porta.grid(row=1, column=0, padx=10, pady=10)

# btn_verificar = tk.Button(janela, text="Verificar", font=("Arial", 14), command=verificar_porta)
# btn_verificar.grid(row=2, column=0, padx=10, pady=10)

# resultado = tk.Label(janela, text="", font=("Arial", 14))
# resultado.grid(row=3, column=0, padx=10, pady=10)
# janela.mainloop()

# Exercicio 8

import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title = ("Exercicio 8")
janela.geometry = ("400x400")

