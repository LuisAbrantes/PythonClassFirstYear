# Atividade 5 / Exercicio 4

numString = input("Digite um número inteiro: ")

# Não pediu para tratar mas estou fazendo.
try:
    num = int(numString)
except:
    print("Digite um número válido")
    exit()

maxDivisor = num//2
divisores = []

soma = 0
for i in range(1, maxDivisor):
    if num % i == 0:
        soma += num

print(f"A soma de {numString} é {soma}")


# def divisores(num):
#     for i in range(1, num//2+1):
#         if num % i == 0: 
#             yield i
#     yield num

# num = 47587950
# print(list(divisores(num)))

