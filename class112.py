'''
Faça um programa que receba um número e verifique se ele é primo ou não.
Caso seja primo, retorne True. Caso contrário, retorne False.
'''

def primo(x):
    contador = 2
    primo = 1
    while contador < x:
        if x%contador == 0:
            primo = 0
        contador +=1
    if primo ==0:
        return False
    else:
        return True

x = int(input("Insira um número para verificar se é primo ou não: "))
run = primo(x)
print(run)