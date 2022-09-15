'''
Faça um programa com uma função que recebe uma temperatura em Fahrenheit e uma string por parâmetros. 
A função deve retornar a temperatura em graus Celsius, caso a string seja "C", e retornar a temperatura em graus Kelvin, caso a string seja "K".
Sabe-se que a temperatura em Celsius(C) é:

C=(F−32)∗5/9,

e a temperatura em Kelvin (K) é:

K=((F−32)∗5/9)+273.15

onde F é o valor da temperatura em Fahrenheit.
'''

# def paraCelsius(f, s):
#     c=(f-32)*5/9
#     return c

# def paraKelvin(f, s):
#     k = ((f-32)*5/9)+273.15
#     return k


def converte(f, s):
    if s == "C":
        c=(f-32)*5/9
        return c
    elif s =="K":
        k = ((f-32)*5/9)+273.15
        return k
    else:
        print("Digite uma opção válida!")

s = str(input('\nDigite "C" para converter o valor de Fharenheit para Celsius; \nDigite "K" para converter o valor de Fharenheit para Kelvin: '))
f = float(input("Insira a temperatura em Fahrenheit: "))


print(f"Sua temperatura convertida é {converte(f, s)} graus.")