# Correção prova
# Exercicio 1
# print("Registro de operador")
# operador = input("Digite seu nome:...")
# turno = input("Digite seu turno...")
# print(f"Operador {operador} registrado no turno {turno}. Boa jornada!")

# Exercicio 2
# print("Calculo de produção")
# producao_hora = int(input("Digite a quantidade de peças produzidas em 1 hora..."))
# producao_turno = producao_hora * 8
# print(f"Quantidade de peças produzidas em um turno de 8 horas: {producao_turno}")

# Exercicio 3
# print("Conversor de unidade")
# pressao_bar = float(input("Digite a pressao em bar"))
# pressao_psi = pressao_bar * 14.5
# print(f"pressao em PSI: {pressao_psi:.2f}")
# print(f"pressao em PSI: {pressao_psi}",round(pressao_psi, 2))

# Exercicio 4
# print("ispenção de peças")
# nota1 = float(input("Digite a nota da inspeção 1 (0 a 10)"))
# nota2 = float(input("Digite a nota da inspeção 2 (0 a 10)"))
# nota3 = float(input("Digite a nota da inspeção 3 (0 a 10)"))
# media = (nota1 + nota2 + nota3) / 3
# print(f"Média de qualidade da peça: {media:.2f}")
# print("Média de qualidade da peça: ", round(media,2))

# Exercicio 5
# print("Termostando Inteligente")
# temperatura = float(input("Digite a temperatura do motor em °C"))
# if temperatura < 40:
#     print("Baixa carga")
# elif 40 <= temperatura <= 70:
#     print("Normal")
# else:
#     print("ALERTA: Resfriamento ativado!")

# print("Termostando Inteligente- versão 2")
# temperatura = float(input("Digite a temperatura do motor em °C"))
# if temperatura < 40:
#     print("Baixa carga")
# elif temperatura > 70:
#     print("ALERTA: Rsfriamento ativado!")
# else:
#     print("Normal")


# Execicio 6
# print ("Classificador de lotes")
# codigo_produto = input("Digite o código do produto")
# if codigo_produto == "A":
#     print("Alimentos")
# elif codigo_produto("E"):
#     print("Eletronicos")
# else:
#     print("Desconhecido")

# print ("Classificador de lotes- versao2")
# codigo_produto = input("Digite o código do produto")
# if codigo_produto.startswith("A"):
#     print("Alimentos")
# elif codigo_produto.startswith("E"):
#     print("Eletronicos")
# else:
#     print("Desconhecido")

# # Exercicio 7
# print("SEgurança de Operação")
# sensor_porta = input("Digite o status do sensor da porta (fechada/aberta)")
# botao_emergencia = input("Digite o status do botão de emergencia (ligado/desligado)")
# if sensor_porta == "fechada" and botao_emergencia == "desligado":
#     print("A maquina pode iniciar.")
# else:
#     print("A maquina não pode iniciar.")

# # Exeecicio 8
# print("Calculo de descarte")
# total_pecas = int(input("Digite o total de peças produzidas"))
# total_defeituosas = int(input("Digite o total de peças defeituosas"))
# descarte_percentual = (total_defeituosas / total_pecas) * 100
# if descarte_percentual > 5:
#     print("Revisar processo")
# else:
#     print("Processo Otimizado")
# print(f"Descarte percentual: {descarte_percentual:.2f}%")

 # Exercico 9
# print("Validação de medida")
# medida = float(input("Digite a medida da peça em mm"))
# if medida < 9.8:
#     print("A peça esta abaixo da tolerancia.")
# elif medida > 10.2:
#     print("A peça esta acima da tolerancia.")
# else:
#     print("A peça esta dentro da tolerancia")

# # Exercio 10
# print("contagem regressiva de Setup")
# for contagem in range(10, 0, -1):
#     print(contagem)
# print("prensa ativada!")

# # Exercicio 11
# print("Soma de produção(Acumulador)")
# peso_total = 0
# while True:
#     peso_caixa = float(input("Digite o peso da caixa(0 para parar)"))
#     if peso_caixa == 0:
#         break
#     peso_total += peso_caixa
# print(f"peso total acumulado: {peso_total:.2f} kg")

# Exercicio 12
# print("Multiplas leituras")
# temperaturas = [10, 20, 30, 40, 50]
# for i in range(1, 6):
#     temp = float(input(f"Digite a temperatura do sensor {i} em °c"))
#     temperaturas.append(temp)

# print(f"Maior temperatura lida: {max(temperaturas):.2f} °C")
# print(f"Menor temperatura lida: {min(temperaturas):.2f} °C")
# print(f"soma temperatura lida: {sum(temperaturas):.2f} °C")

# # Exercicio 13 
# print("Painel de login")
# senha_correta = "admin123"
# tentativas = 3
# while tentativas > 0:
#     senha = input("Digite a senha do supervisor")
#     if senha == senha_correta:
#         print("Acesso permitido")
#         break
#     else:
#         tentativas -= 1
#         print(f"Acesso negado. tentativas restantes: {tentativas}")
# if tentativas == 0:
#     print("Painel Bloqueado")

# Exercicio 14
# print("simulador de estoque")
# estoque = 100
# while True:
#     print("\nMenu")
#     print("1. Adicionar itens")
#     print("2. Remover itens")
#     print("3. sair")
#     escolha = input("Escolha uma opção (1, 2 ou 3)")

#     if escolha == 1:
#         quantidade = int(input("Digite a quantidade de itens a adicionar"))
#         estoque += quantidade 
#         print(f"Estoque atualizado: {estoque} itens")
#     elif escolha == "2":
#         quantidade = int(input("Digite a quantidade de itens a remover"))
#         estoque -= quantidade
#         print(f"estoque atualizado: {estoque} itens")
#         if estoque < 10:
#             print("estoque critico!")
#     elif escolha == "3":
#         print("saindo do simulador de estoque")
#         break
#     else:
#         print("opção inválida. tente novamente.")

# # Exercico 15
# print("relatorio de turno completo")
# total_pecas = 5
# pecas_aprovadas = 0
# for i in range(1, total_pecas +1):
#     diametro = float(input(f"digite o diametro da peça {i} em mm"))
#     if 19.9 <= diametro <= 20.1:
#         pecas_aprovadas += 1
# eficiencia = (pecas_aprovadas / total_pecas) * 100
# print(f"total de peças aprovadas: {pecas_aprovadas}")
# print(f"eficiencia do lote: {eficiencia:.2f}%")

