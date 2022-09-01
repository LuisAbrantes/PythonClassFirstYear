'''
3. Faça um programa com uma função que recebe como parâmetros o nome de um arquivo e uma palavra, 
e retorna o número de vezes que aquela palavra aparece no arquivo.
'''
import json 

def ler():
    arquivo = open("arquivo.txt", "r")
    string = arquivo.read()
    lista = string.lower()
    lista = lista.split()
    arquivo.close()
    return lista

def conta(palavra, lista):
    contador = 0
    palavra = palavra.lower()
    for p in lista:
        if p == palavra:
            contador +=1
    
    return contador



palavra = input("Digite a palavra para verificar quantas vezes ela aparece no arquivo: \n--> ")
lista = ler()
resp = conta(palavra, lista)
print(f"A palavra {palavra} aparece {resp}x na lista")
print(lista)