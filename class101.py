#Dicionários - Curso

d1 = {
    "chave1" : "valor",
    "chave2" : "Outro valor",
    "chave3" : "Tupla",
}

#para vermos as chaves
for k in d1:
    print(k)
print()

#para vermos os valores
for v in d1.values():
    print(v)
print()

#para vermos as chaves e os valores
for k in d1.items():
    print(k, k[0], k[1])
print()

for k, v in d1.items():
    print(k, v)