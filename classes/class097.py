#Exercício quatro
'''
Faça um programa que crie uma 
função que receba 3 números : x, y, z. E faça o seguinte calculo:
(x+y)*z. Em seguida, apresente o resultado na tela.
'''
def conta(x, y, z):
    return (x+y)*z

x = float(input("Digite x: "))
y = float(input("Digite y: "))
z = float(input("Digite z: "))

faz_conta = conta(x, y, z)
if faz_conta:
    print(faz_conta)
else:
    print("Conta Inválida!")