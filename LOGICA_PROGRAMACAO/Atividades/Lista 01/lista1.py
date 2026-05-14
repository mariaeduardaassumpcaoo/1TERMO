# Atividade 1: Mensagem de Boas-Vindas
# Crie um script que use a função print() para exibir a mensagem "Bem-vindo ao mundo da programação em Python!".
 
# print ("Bem-vindo ao mundo da programação em Python!.")

# Atividade 2: Informações Pessoais
# Escreva um programa que imprima seu nome completo em uma linha e sua idade em outra linha.
# Exemplo de saída:
# Fulano de Tal
# 30

# nome = input("Qual seu nome?")
# idade = input("Qual sua idade?")
# print("Seu nome é, ", nome)
# print("Sua idade é, ", idade)

# Atividade 3: Calculadora de Soma e Subtração
# Crie um script que exiba o resultado da soma de 135 com 246 e o resultado da subtração de 512
# por 128. Cada resultado deve ser exibido em uma linha separada.
# ● Dica: Use o print() diretamente com os operadores (print(135 + 246)).
# ● Obs: Realize também a mesma situação com variáveis


# print ("Bem-vindo a calculadora")
# valor1 = int(input("Digite o primeiro valor da adição:"))
# valor2 = int(input("Digite o segundo valor:"))
# resultado1 = valor1+valor2
# valor3 = int(input("Digite o primeiro valor da subtração:"))
# valor4 = int(input("Digite o segundo valor:"))
# resultado2 = valor3-valor4 
# print ("O resultado da adição é, /n", resultado1)
# print ("O resultado da subtração é, /n", resultado2)

# Atividade 4: Multiplicação e Divisão
# Escreva um programa que mostre o resultado da multiplicação de 15 por 8 e o resultado da
# divisão de 78 por 3.

# print("Bem-vindo a calculadora")
# v1 = int(input("Digite o primeiro valor da multiplicação: "))
# v2 = int(input("Digite o segundo valor: "))
# r1 = v1*v2 
# v3 = int(input("Digite o primeiro valor da divisão: "))
# v4 = int(input("Digite o segundo valor: "))
# r2 = v3/v4
# print("O resultado da multiplicação é: ", r1)
# print("O resultado da divisão é: ", r2)

# Atividade 5: Potenciação
# Calcule e exiba o resultado de "5 elevado à 3a potência" (53).
# ● Dica: O operador de potenciação em Python é **.

# v1 = int(input("Digite o primeiro valor"))
# v2 = int(input("Digite o segundo valor"))
# resultado = v1 ** v2
# print("O resultado é: ", resultado)

# Atividade 6: Concatenando Palavras
# Crie um script que declare o seu primeiro nome em uma string e seu sobrenome em outra. Use
# o operador + para concatenar (juntar) as duas strings e exibir seu nome completo.
# ● Exemplo: print("Maria" + " " + "Silva")

# print("Meu nome é: Maria Eduarda \n")
# print("Meu sobrenome é: Assumpção \n")
# print("Maria Eduarda" +" " + "Assumpção \n") 

# Atividade 7: Cálculo de Eficiência (OEE)
# ● Peça a quantidade de peças produzidas e a quantidade de peças defeituosas. Calcule
# e exiba a taxa de aproveitamento (peças boas / total).

# pecas1 = int(input("Digite a quantidade de peças produzidas \n"))
# pecas2 = int(input("Digite a quantidade de peças defeituosas \n"))
# r1 = pecas1 - pecas2
# print("Aproveitamos essa quantidade de pecas: ", r1)

# Atividade 8: Descrição com Cálculos
# Crie um script que exiba a seguinte frase, substituindo os cálculos pelos seus resultados:
# "Eu tenho 25 anos e, em 10 anos, terei 35 anos."
# ● Dica: Use a vírgula dentro do print() para combinar strings e cálculos.
# ● Ex: print("Texto", 25 + 10).

# idade = 25
# idadefutura = idade + 10
# print("Eu tenho", idade, "anos e, em 10 anos, terei", idadefutura, "anos.")

# Atividade 9: Orçamento de Viagem (Cálculo com float)
# Imagine que você está planejando uma viagem. O custo do hotel é de R$ 250.50 por noite e
# o custo da passagem é R$ 412.00. Calcule e exiba o custo total para uma viagem por noites.
# ● Ex: Fórmula: (custo_hotel * 3) + custo_passagem

# print("Orçamento da viagem")
# hotel = 250.50
# passagem = 412.00
# r1 = hotel * 5 + passagem 
# print("O custo total por 5 noites é de: \n", r1)

# Atividade 10: Desafio - Mini Relatório
# Crie um script que imprima um pequeno relatório. Use print() várias vezes para formatar a
# saída de forma organizada.
# ● Exemplo de saída:

# ==========================
# Relatório de Vendas
# ==========================
# Produto: Notebook Gamer
# Quantidade vendida: 15
# Preço unitário: R$ 5499.50
# Total de vendas: R$ 82492.50

# print("Relatorio de vendas")
# print("produto: livros")
# print("Quantidade vendida: 20")
# print("preço Unitario: R$65.00")
# print("total de vendas: R$1300.00")