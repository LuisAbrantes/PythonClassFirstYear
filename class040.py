# Atividade 3 / Exercicio 1

# #Atividade 3 / Exercicio 1

num = int(input('Digite um numero: '))
maior = num
menor = num

cc = str(input('Deseja continuar? S - Sim / 0 - Não  ')).upper()

while cc not in '0':
    num = int(input('Digite um numero: '))
    
    if num > maior:
        maior = num
    if maior < menor:
        menor = num

    cc = str(input('Deseja continuar? S - Sim / 0 - Não  ')).upper()


print('O MAIOR número digitado foi {}.'.format(maior))
print('O MENOR número digitado foi {}.'.format(menor))