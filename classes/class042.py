#Atividade 4 / Exercicio 2

n = int(input("Digite um número inteiro para conferir se é divisível por 3, 5 ou se será invalidado(divisível por ambos): "))

if n%3==0 and n%5==0:
    print("O número é inválido pois é divisível por ambos ao mesmo tempo.")
elif n%3==0:
    print("O número é divisível por 3")
elif n%5==0:
    print("O número é divisível por 5")
else:
    print("Não é divisível por nenhum dos casos.")