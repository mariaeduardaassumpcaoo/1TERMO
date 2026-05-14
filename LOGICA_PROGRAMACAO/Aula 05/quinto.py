# 1. O Laço 'For'(Repetições Determinadas)
# Use o 'for' quando você sabe exatamente quantas vezes algo dee acontecer (como ler 10 sensores ou processar uma lista de peças).
# Exemplo: Relatório de Produção Diária
# Imagine que você tem uma meta de produzir 5 lotes e quer numerar cada um:

# Exemplo 1
# for lote in range(1, 6):
#     print(f"Processando lote número {lote}...")
#     print("Qualidade verificada. [OK]")
#     print("Produção do dia finalizada!")

# Imagine que você queira armazenar 10 carros
# for carros in range(10):
#     print(f"Quantidade de carros {carros}")

# # Exemplo 2
# # Contar até 4
# for i in range(5):
#     print(i)

# # Exemplo 3
# pecas = ["Engrenagem" , "Eixo", "Rolamento", "Parafuso"]
# maquinas = ["Máquina 1", "Máquina 2"]

# for item in pecas:
#     print(f"Item em estoque: {item}")
#     for maq in maquinas:
#         print(f"Máquinas que temos {maq}")

# Exercício 1
# 1. Contador de produção(for)
# Uma esteira processa 10 peças por ciclo. Crie um programa que use um for para contar de 1 a 10 e, para cada número, imprima: "Peça n° X processada com sucesso". No final, exiba "Ciclo de produção concluído".

# for peças in range (1, 10):
#     print(f"Peça n° {peças} processada com sucesso") 
#     print(f"Ciclo de produção concluído")

# Exercício 2
# Imagine a produção de frutas em uma feira. Desejo apresentar as frutas banana, manga, melancia, abacaxi com uma quantidade de 10 bananas, 5 mangas, 10 melancias e 13 abacaxi

# for banana in range(10):
#     print(f"Quantidade de {banana} Bananas \n")
# for manga in range(5):
#     print(f"Quantidade de {manga} manga \n")
# for melancia in range(10):
#     print(f"Quantidade de {melancia} melancia \n")
# for abacaxi in range(13):
#     print(f"Quantidade de {abacaxi} abacaxi \n")
# bananas = int(input("Digite o valor das bananas \n"))
# mangas = int(input("Digite o valor das mangas \n"))
# melancias = int(input("Digite o valor das melancias \n"))
# abacaxis = int(input("Digite o valor dos abacaxis \n"))
# resultado = bananas + mangas + melancias + abacaxis
# print(f"a quantidade de todas as frutas são: ", resultado)

# Exercicio 3
# Montar uma tabuada inicialmente pode ser usado por um valor fixo e depois usar a pergunta

# print("Bem-vindo a sua tabuada")
# valores = int(input("Escolha o valor da tabuada para realizar os resultados \n"))
# for numeros in range (1, 11):
#     print(valores*numeros)
#     print(f"{valores} x {numeros}")

# 2. O laço while (Repetições Indeterminadas)
# Use o while quando você não sabe quando vai parar. Ele depende de uma condição (como um sensor de segurança ou um botão de emergência).
# Exemplo: Monitor de Temperatura estiver segura

# Início
# temperatura = 25
# while temperatura < 40:
#     print(f"Temperatura atual: {temperatura} °C. Sistema operando...")
#     temperatura += 3 # Simulando o aquecimento de máquina
# print("ALERTA! Temperatura atingiu o limite. Desligando motor...")

# Exemplo: Menu de Interação
# opcao = ""

# while opcao != "sair":
#     opcao = input("Digite a leitura do sensor ou 'sair' para fechar: ").upper().lower()
#     if opcao != "sair":
#         print(f"Dado '{opcao}' registrado no banco de dados.")
# print("Sistema encerrado")

# Exercicio 4
#Criar um menu de opções com 4 itens ex: Escolher series aoresente sua escolha de series das outras três.
# qualquer opcao diferente sair do menu


# series= ""
# while series != "drama" and "romance" and "acao":
#     series= input("Digite o genero da serie: \n")
#     if series != "drama" and "romance" and "acao":
#      print(f"Tema" ' {series}' "registrado")
# print("Escolha feita com sucesso")


