print("Seja bem-vindo ao o ano do último treinamento da Brigada de incêndio")
def nome ():
    nome = input("Digite seu nome: \n")
print(f"Olá, {nome()}!")

def setor():
    setor = input("Me fale o setor que você trabalha: \n")
print(f"{nome()} vai comparecer ao {setor()} !")

def status():
    status = input("Defina de qual status você é entre esses: NR-10, NR-35 ou brigada")
print(f"{nome()} vai comparecer ao {setor()} nos status {status()} !")

print("Entramos na Verificação de EPI")
setor = input("Digite novamente seu setor: \n")

if setor == "Elétrica":
    print(f"Para esse setor é obrigatório o uso de luvas de alta tensão e botas dielétricas.")
    print("Se estiver com todos os equipamentos, pode liberar.")
    print("liberado !")

    if setor == "Trabalho em altura":
        print(f"para esse setor é obrigatório o uso de cinturão de segurança e talabarte.")
        print("Se estiver com tos os equipamentos, pode liberar.")
        print("liberado !")

def alerta_de_reciclagem():
    alerta = int(input("Qual foi o ano do ultimo treinamento?: \n"))
    ano_atual = int(input("Digite o ano que estamos"))
    total_ano = ano_atual - alerta
    while total_ano > 2:
        print("Treinamento vencido, mandar para reciclagem....")

    while total_ano < 2:
        print("Treinamento válido")