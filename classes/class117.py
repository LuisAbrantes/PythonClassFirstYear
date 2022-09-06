'''
Faça um programa com uma função que recebe uma lista
como parâmetro e retorna o maior. 

Faça uma segunda função que receba uma lista de 
números por parâmetro e retorna o menor.
'''

def contaMenor(lista):
    maiorNumero = -9999999
    for num in lista:
        if num > maiorNumero:
            maiorNumero = num
    return maiorNumero

def contaMaior(lista):
    menorNumero  = 9999999
    for num in lista:
        if num < menorNumero:
            menorNumero = num
    return menorNumero


lista = [1, 2, 3, 4, 5]

menor = contaMenor(lista)
maior = contaMaior(lista)

print(f"O Maior número é o {maior}")
print(f"O Menor número é o {menor}")