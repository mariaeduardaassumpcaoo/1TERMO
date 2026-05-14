# Conteúdo sobre lógica
# Exemplo 1
# print("Expressões lógicas")
# idade = int(input("Digite sua idade:"))

# if idade >=18:
#     print("Você é maior de idade.")
#     print("Pode tirar carta de motorista.")
# elif idade >=16:
#     print("Você ainda não é maior de idade, mas já pode votar.")
# else:
#     print("Você é menor de idade.")

# if: "Se" a condção for verdadeira.
# elif: "Senão, se" (usado para múltiplas condções).
# else: "Senão" (executa se nenhuma das anteriores for verdadeira).

# Exemplo 2
# print("Escolha sua modalidade?")
# print("Opção 1: TI")
# print("Opção 2: Humanas")
# print("Opção 1: Exatas")
# modalidade = int(input("Digite sua opção de modalidade por números"))
# if modalidade == 1:
#     print("Você escolheu TI")
# elif modalidade == 2: 
#     print("Você escolheu Humanas")
# else:
#     print ("Você escolheu Exatas")

# Exemplo 3
# print("Categoria de Series e Filmes")
# print("Escolha uma categoria")
# print("Séries = S")
# print("Filmes = F")
# categoria = input("Digite sua categoria")
# if categoria == "S":
#     print("Sua escolha foi para Séries")
# elif categoria == "F":
#     print("Sua escolha foi para Filmes")
# else:
#     print("Você não escolheu nenhuma opção")
#     print("Finalizando aplicativo")

# Exemplo 4
# print("Calculadora com condições")
# print("Escolha como quer calcular")
# print("1 = Soma")
# print("2 = Subtração")
# print("3 = Multiplição")
# print("4 = Divisão")
# calculadora = float(input("Digite sua opção para calcular \n"))
# if calculadora == 1:
#     print("1 = Você escolheu soma")
#     soma1 = int(input("Digite o primeiro valor \n"))
#     soma2 = int(input("Digite o segundo valor \n"))
#     print(soma1+soma2)
# elif calculadora == 2: 
#     print("2 = Você escolheu subtração")
#     subtração1 = int(input("Digite o primeiro valor \n"))
#     subtração2 = int(input("Digite o segundo valor \n"))
#     print(subtração1-subtração2)
# elif calculadora == 3:
#     print("3 = Você escolheu multiplicação")
#     multiplicação1 = int(input("Digite o primeiro valor \n"))
#     multiplicação2 = int(input("Digite o segundo valor \n"))
#     print(multiplicação1*multiplicação2)
# elif calculadora == 4:
#     print("4 = Você escolheu divisão")
#     divisão1 = int(input("Digite o primeiro valor \n"))
#     divisão2 = int(input("Digite o segundo valor \n"))
#     print(divisão1/divisão2)
# else:
#     print("Você não escolheu nenhuma opção")
#     print("Sair do programa")

# Exercio 1
# Criar um algoritmo para calcular a média e com base em notas, podemos inserir duas notas e apresente a média porém a nota base de 50 é aprovado e menor que esse valor será reprovado

# nota1= int(input("Digite a primeira nota \n"))
# nota2 = int(input("Digite o segundo valor \n"))
# média = (nota1+nota2) / 2

# if média>= 50:
#     print("Aprovado")
# else:
#     print("Reprovado")

# Exercicio 3
# Criar um algoritmo para demonstrar a sinalização de um semaforo

# print ("Bem-vindo ao semaforo")
# print("vermelho = 1")
# print("amarelo = 2")
# print("verde = 3")
# cores = int(input("Escolha a cor do semaforo \n"))

# if cores == 1:
#     print("vermelho")
# elif cores == 2:
#     print("amerelo")
# elif cores == 3:
#      print("verde")
# else:
#     print("Somente essas cores!!")

# Exercicio 3
# Criar um algoritmo para aplicação de descontos para produtos como sapatos aplicar 10%, para produtos como roupas 5% e perfumes 2%

# Exercicio 4 
# Criara um algoritmo para calcular a média e com base em notas, podemos inserir duas notas e apresente a média porém a nota 0 a 100 para ser aprovado será acima de 70 e menos que 50 esse valor séra reprovado porém vamos acrescentar uma nova condição que entre 50 e 70 recuperação 

# Exercicio 3

# print("Bem-vindo a loja da duda")
# print("roupas = 1")
# print("sapatos = 2")
# print("perfumes = 3")
# produtos = int(input("Escolha seu produto \n"))

# if produtos == 1:
#     qnt = int(input("Digite a quantidade do produto"))
#     valor = int(input("Digite o valor do produto"))
#     resultado = (qnt * valor) 5/ 100
#     print("O valor final do desconto é: \n", resultado)

# elif produtos == 2:
#     qnt = int(input("Digite a quantidade do produto"))
#     valor = int(input("Digite o valor do produto"))
#     resultado = (qnt * valor) 10/ 100
#     print("O valor final do desconto é: \n", resultado)

# elif produtos == 3:
#     qnt = int(input("Digite a quantidade do produto"))
#     valor = int(input("Digite o valor do produto"))
#     resultado = (qnt * valor) 2/ 100
#     print("O valor final do desconto é: \n", resultado)

# else:
#      print("Obrigado pela compra")

# Exercicio 4

# nota1= int(input("Digite a primeira nota \n"))
# nota2 = int(input("Digite o segundo valor \n"))
# media = (nota1+nota2) / 2

# if media>= 70:
#    print("Aprovado")
# elif media > 50:
#     print("Recuperação")
# elif media < 50:
#     print("Reprovado")
