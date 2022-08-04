#Quinto Exercício:
'''
Faça um progama que crie uma função que receba um número e retorne
o valor True caso o número recebido seja par, e false caso o valor
recebido seja ímpar.
'''

def boolean(x):
    if x % 2 ==0:
        result = "True"
        return result
    elif x % 2 ==1:
        result = "False"
        return result

x = float(input("Type an integer value for X: "))

run_boolean = boolean(x)
if run_boolean == "True" or run_boolean == "False":
    print(run_boolean)
else:
    print("invalid calculation!")

