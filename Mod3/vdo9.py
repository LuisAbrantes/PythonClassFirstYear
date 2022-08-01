#Funções anônimas "Lâmbda".

#Exemplo 1:
a = lambda x, y: x*y
print(a(2,4))

#Exemplo 2:
lista = [
    ["P1", 13],
    ["P2", 3],
    ["P3", 3],
    ["P4", 7],
    ["P5", 10],
    ["P6", 19],
]

# lista.sort(key=lambda item: item[1], reverse=True)
print(sorted(lista, key=lambda i: i[1], reverse=True))