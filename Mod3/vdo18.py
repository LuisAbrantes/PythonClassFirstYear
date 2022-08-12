#Dictionary Comprehension

lista = [
    ("chave1", "valor1"),
    ("chave2", "valor2"), 
]

d1 = {x.upper(): y.upper() for x, y in lista}
print(d1)


d2 = {x: y for x, y in enumerate(range(5))}
print(d2)

d3 = {f"chave_{x}: y" for x in range(5)}
print(d3, type(d3))