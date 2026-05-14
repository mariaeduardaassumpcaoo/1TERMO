# Tratamento de erros com python
# Erros comuns:
# - ZeroDivisionError: divisão por zero
# - ValueError: conversão de tipo inválida 
# - IndexError: acesso a índice fora do limite
# - KeyError: acesso a chave inexistente em dicionário

# Exemplo de erros:
# print("Exemplo de tratamento de erros")
# try:
#     num1 = int(input("Digite o primeiro número..."))
#     num2 = int(input("Digite o segundo número..."))
#     resultado = num1 / num2 
#     print(f"O resultado da divisão é: {resultado:.2f}")
 
# except ZeroDivisionError:
#      print("Erro: Não é possível dividir por zero.")

# except ValueError:
#     print("Erro: Entrada inválida. Por favor, digite um número inteiro.")

# except Exception as e:
#       print(f"Ocorreu um erro inesperado: {e}")

# except NameError:
#      print("Erro: Variável não definida.")

# if num1 > 100:
#      print("O número digitado é maior que 100.")
#      for i in range(1, 6):
#           print(f"{num1} x {i} = {num1 * i}")
#           if num1 * i > 1000:
#                print("O resultado da multiplicação é maior que 1000.")
#                try:
#                     pass
#                except Exception as e:
#                     print(f"Ocorreu um erro inesperado: {e}")

# else:
#      print("O numero digitado é menor ou igual a 100.")

# Exercicio 1:
# Escreva um programa que solicite ao usuário um número inteiro e calcule a media de uma lista de números. O programa deve tratar os seguintes erros:
# - ValueError: se o usuario digitar um valor que não seja um número inteiro.

# print("lista de números")
# try:
#      n1 = ("Digite o primeiro valor \n")
#      n2 = ("digite o segundo valor: \n")
#      resultado = (n1 + n2 / 2)
#      print(f"O resultado da média é: {resultado:.2f}")
      
# except ValueError:
#     print(f"Digite um numero inteiro.")

# Exercicio 2
# Escreva um programa que solicite ao usuario uma lista de palavras e conte quantas vezes cada palavra aparece na lista. O programa deve tratar os seguintes erros:
# - ValueError: se o usuario digitar um valor que não seja uma string


# print("Lista de palavras")
# try:
   
#      palavra = str(input("Digite sua palavra \n"))
#      texto = "palavra" 
#      print(texto.strip().count("palavra"))

#      for i in range(8):
#           print({palavra})

# except ValueError:
#      print("Não conhecido como palavra, digite novamente")

# Exercicio 3
# Escrever um programa mais simples com texto de tratamento de erros, como por exemplo, solicitar ao usuario um número. O programa deve tarar os seguintes erros:
# - ValueError: se o usuario digitar o valor que não seja um número
# - ZeroDivisionError: se o usuario digitar zero como divisor

print("Tratamento de erro")
try:
     numero = int(input("Digite um número"))
     # print(f"o numero é {numero}")
except ValueError:
     print("Erro: isto não é um numero, digite novamente")
except ZeroDivisionError:
     print("Não é possivel reconhecer zero")