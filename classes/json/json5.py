import json

arquivo = open("cadastro_pessoas.txt", "r")

string = arquivo.read()

dicionario = json.loads(string)

arquivo.close()


print(dicionario["nome"])