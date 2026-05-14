# Projeto Cancela Automática
# Criar um algoritmo que consiga gerenciar entrada e saída de veículos, inserindo valores por hora permanecida.
# A forma de entrada e saída deve ser especificada e permitir o usuário inserir os dados necessários para registro do veículo

# Passos

# 1 - Pressionar o botão, imprimiu um ticket

# Pegar o ticked, a cancela abre e o carro entra. A partir desse momento, o tempo de permanencia começa a contar...
# calcular tempo de permanencia
# pagar o ticket 
# devolver ticket na saida
# liberar e fechar cancelas

# 2 - Acesso por TAGs(Sem parar, Connect car...)

# calcular tempo de permanencia
# gerar pagamento em fatura
# liberar e cancelar cancelas

# 3 - Erros

# verificar sinal de transmissão  da TAG
# Verificar acesso por ticket ou tag ao mesmo tempo
# perdeu ticket(levantar informações)
# problemas com cancela

print("Bem-vindo ao estacionamento")
entrar = input("Você deseja entrar por?:")

if entrar == "ticket":
    print("pega o ticket e a cancela abre")
    tempo = int(input(f"Quantas horas que você passou no shopping? \n"))
    totaldepermanencia = 12 * tempo
    print(f"o total do pagamento foi de {totaldepermanencia}")
    print("Realize o pagamento no caixa")
    erro_ticket = input("Está com o ticket?")

    if erro_ticket == "Sim":
       print("ticket pago, devolver ticket na saída")
       input("cancela abre, carro liberado")
       print("Até logo, volte sempre!")

    else:
          print("Erro detectado")
          input("Resolver problema no caixa, apresentar a placa do carro para a analise")
          print("problema resolvido")
          print("cancela abre, carro liberado")
          print("Até logo, volte sempre!")
    
if entrar == "TAGs":
 print("Sensor lê seu Sem Parar")
 print("a cancela abre")
 tempo2 = int(input(f"Quantas horas que você passou no shopping? \n"))
 totaldepermanencia2 = 12 * tempo2
 print(f"o total foi de {totaldepermanencia2}")
 print("pagamento ira para sua fatura")
 input("cancela abre novamente lendo seu Sem Parar, carro liberado")
 print("Até logo, volte sempre!")


 



