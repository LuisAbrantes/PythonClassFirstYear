'''
2. Faça um programa que tem uma função que lê um arquivo texto e conta quantas vogais têm neste arquivo.
'''

import json

def ler():
    arquivo = open("arquivo.txt", "r")
    string = arquivo.read()
    lista = string.split()
    print(lista)
    arquivo.close()
    return lista

def contaVogal(lista):
    contador = 0
    for palavra in lista:
        for letra in palavra:
            if (letra.lower() in "aeiou"):
                contador +=1
    return contador


#Corpo
lista = ler()
#lista = Luis Henrique dos Santos Abrantes

print(lista)
totalVogais = contaVogal(lista)
print(totalVogais)
