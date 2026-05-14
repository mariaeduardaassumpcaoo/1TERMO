# 1. Registro de Operador: Peça o nome do operador e o turno (A, B ou C). Exiba:
## "Operador [Nome] registrado no Turno [Turno]. Boa jornada!"

# nome = input("Digite seu nome: \n")
# turno = input("Digite seu turno: \n")
# print(f"{nome} registrado no turno {turno}. Boa jornada!")

# 2. Cálculo de Produção: Peça a quantidade de peças produzidas em 1 hora. Calcule e
# exiba quantas peças serão produzidas em um turno de 8 horas.

# peças = int(input("Qual foi a quantidade de peças produzidas em 1 hora?: \n "))
# total = peças * 8 
# print("foram produzidas: ", total)
# print("no turno de 8 horas foram produzidas esse totalde peças: ", total)

# 3. Conversor de Unidade: O sistema lê uma pressão em Bar. Converta para PSI (1 Bar
# ≈ 14.5 PSI) e exiba com duas casas decimais.

# pressão = float(input("Qual a pressão do bar hoje?: \n"))
# bar = 14.5
# total = 14.5 * pressão
# print("o resultado em casas decimais foram: \n", total)

# 4. Média de Qualidade: Peça 3 notas de inspeção de uma peça (0 a 10). Exiba a média
# aritmética simples delas.

# n1 =int(input("Digite o valor da primeira peça (de 0 a 10): \n "))
# n2 =int(input("Digite o valor da segunda peça (de 0 a 10): \n"))
# n3 =int(input("Digite o valor da terceira peça (de 0 a 10): \n"))
# total = (n1 + n2 + n3) /3
# print("a qualidade foi de:", total)

# 5. Termostato Inteligente: Peça a temperatura de um motor.
# ● Abaixo de 40°C: "Baixa carga".
# ● Entre 40°C e 70°C: "Normal".
# ● Acima de 70°C: "ALERTA: Resfriamento Ativado!".

# print("identificador de temperatura de motor")
# temperatura = int(input("Digite a temperatura: \n"))
# if temperatura <= 40:
#     print("sua temperatura está com baixa carga")

# elif 40 < temperatura < 70:    
#     print("ALERTA: resfriamento ativado")

# else:
#    print("Sistema desligando") 

# 6. Classificador de Lotes: O usuário insere o código do produto. Se começar com "A",
# exiba "Alimentos". Se "E", "Eletrônicos". Para qualquer outro, "Desconhecido".

# lotes = str(input("Digite oque deseja: \n"))

# if lotes == "A":
#     print("Sua escolha foi alimento")
    
# elif lotes == "E":
#     print("Sua escolha foi eletronicos")

# else:
#     print("Desconhecido")

# 7. Segurança de Operação: A máquina só liga se o sensor_porta == "fechada" E o
# botao_emergencia == "desligado". Peça esses dois inputs e diga se a máquina pode
# iniciar.

# sensorporta = str(input("Digite se a porta esta fechada ou aberta \n"))
# botaoemergencia = str(input("Digite se esta ligado ou desligado \n"))

# if sensorporta == "fechada" and botaoemergencia == "desligado":
#     print("Ligar sensor")
#     print("Pode inicar a maquina")

# elif sensorporta == "aberta" and sensorporta == "ligado":
#     print("desligar sensor")
#     print("nao iniciar a maquina")

# else:
#     print("iniciar maquina")

# 8. Cálculo de Descarte: Peça o total de peças produzidas e o total de defeituosas. Se
# o descarte for maior que 5% do total, exiba "Revisar Processo", caso contrário,
# "Processo Otimizado".

# produzidas = int(input("Digite quantas peças foram produzidas: \n"))
# defeituosas = int(input("Digite quantas peças estao defeituosas"))
# total = defeituosas * 0.05
# if defeituosas > total:
#     print("Revisar processo")

# elif defeituosas < total:
#     print("Processo otimizado")

# else:
#     print("calculo encerrado")

# 9. Validação de Medida: Uma peça deve ter entre 9.8mm e 10.2mm. Peça a medida e
# diga se está dentro da tolerância, acima ou abaixo.

# peça = float(input("Digite o mm da peça: \n"))
# if peça == 9.8:
#     print("Dentro da tolerancia")
# elif peça == 10.2:
#     print("Dentro da tolerancia")

# elif peça >10.2:
#     print("acima da tolerancia")

# elif peça <9.8:
#     print("abaixo da tolerancia")

# else:
#     print("encerrar validação")

      
# 10.Contagem Regressiva de Setup: Use um for para fazer uma contagem regressiva
# de 10 até 1 para o início de uma prensa, e finalize com "Prensa Ativada!".

# print("inicie a prensa")
# for i in range(10,0 ,-1):
#     print(i)
# print("prensa ativada")

# 11.Soma de Produção (Acumulador): Use um while para pedir o peso de várias caixas.
# O loop para quando o usuário digitar 0. No fim, mostre o peso total acumulado.

# totalpeso = 0
# while True:
#     peso =float(input("digite o peso: \n"))
#     if peso == 0:
#         continue
#     totalpeso += peso
#     print(f"Peso total acumulado {totalpeso}")


        
    
