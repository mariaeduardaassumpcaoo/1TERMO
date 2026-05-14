# Celan cocde aula - 8
# para que usar?
# como usar?
# print("Clean code - Aula 8")
# aula = 8
# print(f"Estamos na aula {aula} de Clean Code")

#manipulação de arquivos e texto
# texto = " Python é muito legal! "
# print(texto.strip().upper()) # "PYTHON"
# print(texto.strip().lower()) # "python"
# print(texto.strip().capitalize()) #"Python"
# print(texto.strip().title()) # "Python"
# print(texto.strip().replace(" ", "_")) # "Python"
# print(texto.strip().split()) #["Python"]

#escrevendo
# with open("notas.txt", "w") as arquivo:
#      arquivo.write("Estudar Python hoje!")
#      arquivo.write("\nLer sobre Clean Code.")

# #Lendo
# with open("notas.txt", "r") as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)

# # Execucão de comandos do sistema
import os # importa o módulo os para interagir com o sistema operacional

# # # Onde estou?
print(os.getcwd())

# # # Listar arquivos na pasta
# # print(os.listdir())
# # print(os.listdir("..")) # Lista arquivos da pasta pai
# # print(os.listdir("..\\..")) # lista arquivos da pasta avô
# # print(os.listdir("C:\\")) # lista arquivos da raiz do C
# # print(os.listdir("C:\\Users")) # lista arquivos da pasta user
# # print(os.listdir("C:\\Users\\publica")) # lista aqruivos da pasta publica

# # Outros comando úteis:
# # Criar pasta
# # os.mkdir("nova_pasta")
# # # Renomear pasta
# # os.rename("nova_pasta", "pasta_renomeada")
# # # # Excluir pasta
# os.rmdir("Pasta_renomeada")

# Exercicio 1
# Crie um script que mostre o caminho da pasta atual

# os.mkdir("projetos")
# os.rename("projetos", "meus_projetos")
# os.rmdir("meus_projetos")


# Exercicio 2
# liste os arquivos da pasta atual
print(os.listdir())

# Exercico 3
# crie uma pasta chamada "projetos" e depois renomeia para "meus_projetos". por fim, exclua a pasta
# os.mkdir("projetos")
# os.rename("projetos", "meus_projetos")
# os.rmdir("meus_projetos")

# Exercicio 4:
# crie um arquivo chamado "log.txt" e escreva a mensagem "log de atividades". depois, leia o conteudo do arquivo e exiba na tela.
# with open("log.txt", "w") as arquivo:
#     arquivo.write("Log de atividades")
# with open("log.txt", "r") as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)

# # Exemplo de dicionario
# # Crie um dicionario com informações sobre uma pessoa e acesse um valor usando uma chave
# pessoa = {
#     "nome": "Alice",
#     "idade": 30,
#     "cidade": "São Paulo"
# }
# print(pessoa ["nome"])

# pessoa2 = {
#     "nome": "Duda",
#     "idade": 16,
#     "cidade": "Limeira"
# }
# print(pessoa ["nome"])
# print(pessoa ["idade"])
# print(pessoa ["cidade"])

# Exercico 6: desligar o PC (comando para Windows)
# with open("desliga.bat", "w") as desligar:
#     desligar.write("shutdow -s -t 3600 -c \"Desligamento progamado para daqui a uma hora. Salve seu trabalho!\"")
#     # -s comando para desligar
#     # -t tempo definir
#     # -a cancelar desligamento

# with open("desliga.bat", "r") as desligar:
#     conteudo = desligar.read()
#     print(conteudo)

# Exercicio 7: Criar um arquivo de backup
# Escreva um script que crie um arquivo de backup do arquivo "notas.txt" com o nome "notas_backup.txt". O script deve ler o conteúdo de "notas.txt" e escrever no novo arquivo

# with open("notas.txt", "r") as notas:
#     conteudo = notas.read()

# with open("notas_backup.txt", "w") as backup:
#     backup.write(conteudo)

# Exemplo 2: Criar um script de limpeza de arquivos 
# Escreva um script que liste os arquivos de uma pasta e exclua os arquivos com extensão ".temp". O script deve exibir uma mensagem para cada arquivo ecluido.
# pasta = os.listdir()
# for arquivo in pasta:
#     if arquivo.endswith(".tmp"):
#         os.remove(arquivo)
#         print(f"Arquivo {arquivo} excluido.")
# print("Limpeza de arquivos concluída")

# Exercicio 8: Criar um script de monitoramento de temperatura
# Escreva um script que monitore a temperatura de um motor. O script deve ler a temperatura de um arquivo "temperatura.txt" e exibir uma mensagem de alerta se a temperatura estiver acima de 70°C.



