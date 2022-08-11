#Atividade 2 / Exercicio 9

print("Vamos calcular uma raíz de segundo grau. A variavel 'a' não pode ser 0.")
a = float(input("Insira o valor de a: "))
b = float(input("Insira o valor de b: "))
c = float(input("Insira o valor de c: "))
if a == 0:
    print("Não é equação de segundo grau.")
else:
    D = (b**2 - 4*a*c)
    x1 = (-b + D**(1/2)) / (2*a)
    x2 = (-b - D**(1/2)) / (2*a)

    print("O valor de x1 é: ", x1)
    print("O valor de x2 é:", x2)