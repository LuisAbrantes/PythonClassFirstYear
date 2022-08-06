#Dicionários - Curso

d1 = {
    "str" : "valor",
    123 : "Outro valor",
    (1, 2, 3, 4) : "Tupla",
}

print("str" in d1)
print("str" in d1.keys())
print("valor" in d1.values())
print(len(d1))