# Atividade 5 / Exercicio 3

numString = input("Digite um número inteiro e maior que 0: ")
soma = 0

# Não pediu para tratar mas estou fazendo.
try:
    num = int(numString)
except:
    print("Digite um número válido")
    exit()

if (num<0):
    print("Digite um número maior do que zero")
    exit()

for digito in numString:
    soma += int(digito)

print(f"A soma de {numString} é {soma}")