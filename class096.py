#Terceiro Exercício
'''
Faça uma função que receba dois números, e apresente a subtração
desses números
'''

def subtracao(n1, n2):
    return n1-n2

n1 = int(input("Primeiro numero: "))
n2 = int(input("Segundo numero: "))
subtrai = subtracao(n1,n2)
if subtrai:
    print(subtrai)
else:
    print("Conta invalida.")