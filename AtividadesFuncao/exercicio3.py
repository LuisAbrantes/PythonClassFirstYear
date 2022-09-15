'''
3- Faça um programa que tem uma função que recebe um inteiro como parâmetro 
e retorna verdadeiro ou falso caso o número seja primo ou não, respectivamente.
'''
# 0 e 1 nao sao primos
def primo(x):
    contador = 2
    primo = True
    while contador < x:
        if x % contador == 0:
            primo = False
        contador+=1
    return primo

x = int(input("--> "))
print(primo(x))