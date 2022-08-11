#primeira questão da segunda prova de PBC

#Faça um programa que apresente o maior divisor de um número lido no console, com exceção dele mesmo. Por exemplo, o maior divisor de 6, com exceção do próprio 6, é 2.

#Soma dos divisores

num = int(input("Digite um número inteiro maior que 0 para mostrar seu maior divisor: "))
maior_divisor = 0
if num > 0:
    for c in range(1, num):
        if num%c == 0:
            maior_divisor = c
print(f"O maior divisor de {num} é {maior_divisor}")
