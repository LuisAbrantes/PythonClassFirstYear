"""
1. Faça um programa com uma função que armazena em arquivo diversas palavras até que o usuário digite 0. Ao digitar 0, o programa fecha o arquivo.  
Crie uma segunda função para abrir o arquivo e apresentar todas as palavras salvas.
"""

#Não está salvo nem criado o arquivo txt

filename = "arquivo.txt"

def adiciona(lista):
    print(lista)
    arquivo = open("arquivo.txt", "a")

    for v in lista:
        arquivo.write(v+'\n')
    arquivo.close()

# def apresenta(x, lista):
#     arquivo = open(filename, "r")

lista = []
x=1

while (x != "0"):
    x = input("Digite palavras para serem adicionadas ao arquivo. \nDigite 0 para encerrar o programa. \n--> ")
    if x != '0':
        lista.append(x)


adiciona(lista)