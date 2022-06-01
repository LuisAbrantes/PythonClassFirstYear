'''
Faça um programa que obtenha do teclado 5 temperaturas em Celsius e as armazene em uma lista. Em seguida, converta cada uma destas temperaturas para Fahrenheit, 
a armazenando em uma segunda lista
'''

lista = list()
for contador in range(5):
    lista.append(float(input("Temperatura: ")))

lista2 = lista()
for temperatura in lista:
    lista2.append((temperatura*1.8) + 32.0)

print(lista)
print(lista2)