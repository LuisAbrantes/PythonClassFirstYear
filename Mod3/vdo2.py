#função def pt.2

def divisao(n1, n2):
    return n1/n2

n1 = int(input("Primeiro numero: "))
n2 = int(input("Segundo numero: "))
divide = divisao(n1,n2)
if divide:
    print(divide)
else:
    print("Conta invalida.")