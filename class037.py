#Atividade 2 / Exercicio 7

numero = int(input("Informe um número inteiro"))
soma = 0
while numero > 0 :    
    soma += numero % 10   
    numero = numero // 10
    print(soma)
if numero <= 0: 
    print("Número inválido")