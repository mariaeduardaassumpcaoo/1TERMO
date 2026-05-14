
# def saudacao(nome):
#     return f"Olá, {nome}!"

# mensagem = saudacao ("Maria")
# print(mensagem)

# Exemplo 2
# nome = input("Seu nome: ")
# idade = int(input("Sua idade ")) # Converter texto para inteiro
# print(f"{nome} tem {idade} anos.")

#Exercicio 1
# Cálculo de notas por semestre onde terá duas notas formativas e uma nota somativa para encerrar o semestre. 
# os valores de notas são de 0 a 100

# n1 = int(input("Digite a sua primeira nota: \n"))
# n2 = int(input("Digite a sua segunda nota: \n"))
# n3 = int(input("Digite a sua terceira nota: \n"))
# ntotal = (n1 + n2 + n3) / 3 
# print("Sua nota final foi?: \n", ntotal)

#Exercicio 2
# Cálculo de notas por semestre onde terá duas notas formativas e uma nota somativa para encerrar o semestre. 
# os valores de notas são de 0 a 100 no final exibir o resultado do ano e incluir nota de média do primeiro e segundo semestre

# n1 = int(input("Digite a sua primeira nota: \n"))
# n2 = int(input("Digite a sua segunda nota: \n"))
# n3 = int(input("Digite a sua terceira nota: \n"))
# ntotal = (n1 + n2 + n3) / 3 
# print("seu resultado é: \n", round(ntotal,2))


# n11 = int(input("Digite a sua primeira nota: \n"))
# n22 = int(input("Digite a sua segunda nota: \n"))
# n33 = int(input("Digite a sua terceira nota: \n"))
# ntotal2 = (n1 + n2 + n3) / 3 
# print("seu resultado é: \n", round(ntotal2,2))


# print(f"A nota dos dois semestres é: \n {ntotal} e {ntotal2}")


# # Arredondar casas decimais
# # s1 = n1+ n2 + n3 /3
# # round(ntotal),2
# def boas_vindas(nome, cargo):
#      print(f"Olá, {nome}! Você é o nome {cargo}.")

# boas_vindas("Duda", "Desenvolvedora")
# boas_vindas("Carlos", "Gerente")

# #exemplo 4
# def configurar_conexão(servidor, porta=8080):
#     print(f"Conectando a {servidor} na porta {porta}...")

# configurar_conexão("192.168.1.1")      #Usa a porta 8080
# configurar_conexão("10.0.0.1", 3000)   #Usa a porta 3000
# configurar_conexão("192.168.1.2")
# configurar_conexão("10.0.0.2", 3001)

# #Exercico 2
# #Calculo de idade: Deve apresentar o nome, curso, data de nascimento e apresentar a idade sua no final.

# nome = str(input("Digite seu nome \n"))
# curso = str(input("Digite seu curso \n"))
# nasc = int(input("Digite o ano do seu nascimento \n"))
# ano = int(input("Digite o ano atual \n"))
# idade = ano - nasc
# print(f"{nome} tem {idade} anos.")

#Exercicio 3
# Calcular gorjetas: receba o valor da conta de um restaurante e retorne o valor da gorgeta(considerando 10% do valor da conta).

# v1 = float(input("O valor da conta: \n"))
# gorgeta = int(input("Digite o valor da porcentagem da gorgeta: \n"))
# vgorgeta = v1 / gorgeta 
# print("o valor da gorgeta é: ", vgorgeta)
 

#exercicio 4
# Criar um sistema para calcular o sucessor e antecessor de um valor 

# p1 = int(input("Digite o número \n"))
# print("Antecessor é: \n", p1-1)
# print("sucessor é: \n", p1+1)

#exercicio 5
# criar um algoritmo para calcular a venda de livros e que toda venda apresente um desconto fixo de 5%

qtd = int(input("Digite a quantidade de livros \n"))
valor = float(input("Digite o valor dos livros \n"))
resultado = qtd * valor /5
print("O valor final do desconto é: \n", resultado)











