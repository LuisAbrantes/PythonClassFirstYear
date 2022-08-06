#Dicionários - Curso

d1 = {
    "str" : "valor",
    123 : "Outro valor",
    (1, 2, 3, 4) : "Tupla",
}

#melhor jeito de atualizar as chaves, é o jeito comentado
# d1["nomedachave"] = "Agora ela existe"

# if d1.get("str") is not None:
#     print(d1.get("nomedachave"))

# print(123)

d1.update({"nova_chave":"novo_valor"})

if d1.get("nova_chave") is not None:
    print(d1.get("nova_chave"))

print(123)