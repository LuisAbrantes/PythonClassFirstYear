'''
Faça um programa para armazenar em uma lista, a metade dos valores da seguinte lista: [2, 4, 6, 8, 10]
'''

lista = [2, 4, 6, 8, 10]

metades = list()
contador = 0

while(contador < 5):
    val = lista[contador]/2
    metades.append(val)

    contador+=1

print(metades)