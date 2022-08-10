'''
Faça um programa que crie uma função para 
obter o nome de pessoas de maneira indefinida, 
e armazene esses nomes em uma lista.
Em seguida, apresente os nomes da lista.
'''

def criaLista():

    resp = 1
    listaNomes = list()
    while(resp != 0):
        nome = input("Digite o nome: ")
        listaNomes.append(nome)
        resp = int(input("Deseja dicionar mais um nome? (0 para sair) "))
    print(listaNomes)

criaLista()