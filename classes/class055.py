#Soma dos divisores

num = int(input("Digite um número inteiro maior que 0 para somar seus divisores: "))
soma = 0
if num > 0:
    for c in range(1, num):
        if num%c == 0:
            soma += c
            print(c)
            
else: 
    print("Número inválido.")

print(f"A soma dos divisores é igual a {soma}")