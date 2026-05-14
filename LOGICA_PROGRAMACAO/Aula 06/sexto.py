# for i in range(1, 11):
#     print(f"\nTabuada do {i}:")
#     for j in range(1,11):
#         print(f"{i} x {j} = {i * j}") 

#lista de temperaturas lidas pelo sensor por minuto
# leituras = [70, 75, 82, 98, 110, 85, 80]

# for temp in leituras:
#     if temp > 100:
#         print(f"CRÍTICO: {temp}°C detectado! Acionando parada de emergência.")
#         break # O loop para aqui e NÃO lê os próximos valores (85 e 80)
#     print(f"Temperatura está em {temp}°C. Operação normal.")

# print("Sistema desligado. Aguardando manutenção.")

# materiais = ["metal", "metal", "plastico", "metal", "vidro", "metal"]
# for peca in materiais:
#    if peca != "metal":
#     print(f"Aviso: Peça de {peca} detectada. Desviando para descarte...") 
#     continue # Pule o restante do código abaixo e vai para a próxima peça 
   
# # Este código só roda se a peça for de metal
# print("Processando peça de {peça}. Furando e polindo...") 

#Exercicio 1
# Tente criar um código que conte de 1 a 10, mas use o continue para não imprimir o número 5 (simulando uma falha de sensor específica no item 5)


# for temp in range(1, 10):
#     if temp == 5:
#         continue # Pule o numero 5 e vá para o proximo numero
#     print(f"falha detectada no sensor {temp}")

# from time import sleep
# for i in range(1,11):
#     if i ==5:
#         print(f"Falha ao ler o n° {i}")
#         sleep(1.8)
#         continue
#     print(i)
#     sleep(0.7)
# print("Acabou")

# from time import sleep
# print("vermelho=1")
# print("amarelo=2")
# print("verde=3")

# cores = int(input("Qual cor você deseja?"))

# if cores ==3:
#     print("verde")
#     sleep(5)
# elif cores ==1:
#     print("vermelho")
#     sleep(3)
# elif cores ==2:
#     print("Amarelo")
#     sleep(2)
# else:
#     ("somente essas cores!!")

# Exercicio 4- Soma de cargas de energia(for)
# Uma fábrica tem 5 máquinas. Peça ao usuário (via input dentro do loop) o consumo de KWH de cada uma das 5 máquinas. Ao final do loop, o programa deve exibir o consumo total da fábrica.

# for i in range(5):
#     consumo = float(input(f"Digite o valor do consumo das máquinas: \n"))
#     total = consumo + i
#     print("o valor final do consumo das máquinas é:", total)

# Exercico 5 - identificador de peças defeituosas (for + if)
# percorra uma lista de medidas de peças:
# medidas = [50.1, 49.8, 52.0, 50.0, 48.5].
# O padrão de qualidade aceita apenas peças com exatamente 50.0 ou mais.
# use um for para ler a lista e, para cada peça, diga se ela esta "aprovada" ou "reprovada".

# print("identificador de peças defeituosas")
# leituras = [50.1, 49.8, 52.0, 50.0, 48.5]

# for temp in leituras:
#     if temp > 50.0:
#         print(f"{temp} sua temperatura está OK")

#     elif temp < 50.0:
#         print(f"{temp} sua temperatura está baixa")

# else:
#     print("encerramos o sistema")

# Exercicio 6 - uma balança industrial esta pesando um lote de 6 sacos de insumos. O peso ideal de cada saco é 50kg, mas o sistema aceita varições.
 
# peso = float(input("Digite o peso"))
# for i in range(1,6):
#     if peso >50.0:
#         print(f"{peso} o peso esta OK")

#     elif peso <50.0:
#         print(f"{peso} o peso esta fora do padrão")

# Exercicio 7: Sistema inteligente de manutenção
# crie um programa que receba dois dados: a pressão atual(float) e as horas de uso acumuladas(int) de uma turbina.
# O programa deve classificar o estado da maquina seguindo esta hierarquia:
# Critico (Prioridade 1): Se a pressão for maior que 100 OU as horas de uso forem maiores que 10.000.
# Mensagem: "PARADA IMEDIATA: Risco de falha catastrofica"
# Alerta (prioridade 2): Se a pressão estiver entre 80 e 100 (inclusive).
# Mensagem "Manutenção Agendada: Pressão acima do ideal."
# Monitoramento (prioridade 3): Se as horas de uso forem entre 8.000 a 10.000.
# Mensagem: "AVISO: Máquina aproximando-se da revisão de 10k horas."
# Normal: Para qualquer outro caso que não se encaixe nos acima.
# Mensagem: "SISTEMA OPERAL: Todos os parâmetros dentro da normalidade."





