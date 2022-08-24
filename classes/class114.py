'''
3- Faça um programa que tem uma função que recebe um inteiro como parâmetro 
e retorne verdadeiro ou falso caso o número seja primo ou não, respectivamente.
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