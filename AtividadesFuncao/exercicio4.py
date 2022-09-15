'''
4- Faça um programa que tem uma função que recebe uma lista de números como parâmetro, 
e retorna a soma de todos os números da lista.
'''

def conta(lista):
    contador = 0
    for n in lista:
        contador = contador+n
    return contador

# def conta2(lista):
#     total = 0
#     return [total := total + x for x in lista]

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"A soma é {conta(lista)}")
# print(f"A soma é {conta2(lista)}")