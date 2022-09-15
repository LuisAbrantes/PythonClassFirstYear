'''
1- Faça um programa com uma função para receber 2 números como parâmetro e apresentar a divisão deles. 
Apresentar uma mensagem de erro caso haja divisão por 0
'''

def div(x: float, y: float) -> float:
    if y!=0:
        return x/y
    else:
        return "Digite um denominador diferente de 0!"

x = float(input("Insira o numerador: "))
y = float(input("Insira o denominador:"))
print(div(x, y))

'''
1- Faça um programa com uma função para receber 2 números como parâmetro e apresentar a divisão deles. 
Apresentar uma mensagem de erro caso haja divisão por 0
'''

# def div(x: float, y: float) -> str:
#     return x/y

# x = float(input("Insira o numerador  :"))
# y = float(input("Insira o denominador:"))
# try:
#     result = div(x, y)
#     print(result)
# except:
#      print("Digite um denominador diferente de 0!")