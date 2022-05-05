#faça um programa para obter um valor no console e dizer se eh primo ou nao

num = int(input("Digite um número inteiro para verificar se ele é primou ou não: "))
contador = 2
primo = 1
while contador < num:
    if num%contador == 0:
        primo = 0
    contador +=1
if primo == 0:
    print("Não é primo")
else:
    print("É primo")
