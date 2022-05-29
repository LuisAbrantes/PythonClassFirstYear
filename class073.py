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

    if operador == "+":
        print(f"{num1}+{num2}")
    elif operador == "-":
        print(f"{num1}-{num2}")
    elif operador == "/":
        print(f"{num1}/{num2}")
    elif operador == "*":
        print(f"{num1}*{num2}")
    else:
        print("Digite um operador válido!")