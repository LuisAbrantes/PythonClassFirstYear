#Atividade 4 / Exercicio 6

num = int(input("Insira um número inteiro de 1 a 10 para exibir as tabuadas: "))

#soma
print("TABUADA DE SOMA")
for soma in range(1,11):
    print(f"{num} + {soma} = {num+soma}")
print()

#subtração
print("TABUADA DE SUBTRAÇÃO")
for sub in range(num+1,num+11):
    print(f"{sub} - {num} = {sub-num}")
print()

#multiplicação
print("TABUADA DE MULTIPLICAÇÃO")
for m in range(1,11):
    print(f"{num} x {m} = {num*m}")
print()

#divisão
print("TABUADA DE DIVISÃO")
for div in range(num, num+9):
    print(f"{div} ÷ {num} = {div/num}")