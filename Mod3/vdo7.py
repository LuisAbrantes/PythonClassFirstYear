'''
1- Crie uma função 1 que recebe uma função 2 como parâmetro e retorne o 
valor da função 2 executada.
'''

# def ola_mundo():
#     return 'ola mundo'

# def mestre(funcao):
#     return funcao()

# executando = mestre(ola_mundo)
# print(executando)

'''
2- Crie uma função 1 que recebe uma função 2 como parâmetro e retorne o 
valor da função 2 executada. Faça a função 1 executar duas funções que 
recebam um número diferente de argumentos.
'''

def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def fala_oi(nome):
    return f"Oi {nome}"

def saudacao(saudacao, nome):
    return f"{saudacao} {nome}"

executando = mestre(fala_oi, "Luis")
executando2 = mestre(saudacao, "Bom dia", "Luis")
print(executando)
print(executando2)