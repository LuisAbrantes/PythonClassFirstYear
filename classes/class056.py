from calendar import c


var = float(input("Entre com um valor maior que 20. Digite um menor para parar o programa: "))
print(var)

maiorAtual = var
menorAtual = var


while var>=20:
    var = float(input("Entre com um valor maior que 20. Digite um menor para parar o programa: "))

    if var > maiorAtual:
        maiorAtual = var

    if var < menorAtual:
        menorAtual = var

print("voltei normalmente para o programa.")

print(f"O maior é: {maiorAtual}")
print(f"O menor é: {menorAtual}")
