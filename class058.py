#segunda questão da prova de PBC

#Faça um programa que permita obter uma quantidade indefinida de valores no console, e ao final apresente o menor valor e a média destes valores.

var = float(input("Entre com os valores desejados. Ao digitar 0, o programa é encerrado: "))

s = 0
qtd = 0
maiorAtual = var
menorAtual = var


while var!=0:
    if var!=0:
    
        if var > maiorAtual:
            maiorAtual = var

        if var < menorAtual:
            menorAtual = var

        s += var
        qtd += 1

        var = float(input("Entre com os valores desejados. Ao digitar 0, o programa é encerrado: "))

    

media = (s/qtd)

print(f"A média é: {media}")
print(f"O maior é: {maiorAtual}")
print(f"O menor é: {menorAtual}")
