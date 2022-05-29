'''
While usado em Python - Aula 7
 -Utilizado para realizar ações enquanto uma condição for verdadeira
'''

from operator import truediv


x = 0 
while x<10:
    y = 0

    while y<5:
        print(f"({x},{y})")
        y += 1

    x += 1

print("Acabou!")

print("")
print("")
print("")
print("")

while True:
    print("")
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))
    operador = input("Digite o operador('+'; '-'; '/'; '*'): ")
    sair = input("Deseja sair? [s]im ou [n]ão: ")

    if sair == 's':
        break

    if not num1.isnumeric() or not num2.isnumeric():
        print("Você precisa digitar um NÚMERO.")

    if operador == "+":
        print(f"{num1} + {num2} = {num1+num2}")
    elif operador == "-":
        print(f"{num1} - {num2} = {num1-num2}")
    elif operador == "/":
        print(f"{num1} / {num2} = {num1/num2}")
    elif operador == "*":
        print(f"{num1} * {num2} = {num1*num2}")
    else:
        print("Digite um operador válido!")