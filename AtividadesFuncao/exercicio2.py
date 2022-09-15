'''
2- Faça um programa que tem uma função que recebe uma lista de números por parâmetro, 
e retorna a quantidade de números pares nesta lista.
'''

def par(list):
    cont = 0
    for n in list:
        if n%2==0:
            cont+=1
    return cont

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(f"Existem {par(list)} números pares.")