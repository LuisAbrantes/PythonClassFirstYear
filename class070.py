#Crie uma lista para armazenar o dobro dos valores da primeira lista

lista1 = [1, 2, 3, 3.5, 9.5]
lista2 = list()

for val in lista1: 
    dobro = val * 2
    lista2.append(dobro)
print(lista2)