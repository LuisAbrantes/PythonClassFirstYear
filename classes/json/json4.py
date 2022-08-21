import json

pessoa = dict()
pessoa["nome"] = "Luis"
pessoa["idade"] = 15
pessoa["endereco"] = "Av. Qualquer coisa"


arquivo = open("cadastro_pessoas.txt", "w")

json.dump(pessoa, arquivo)
arquivo.close()