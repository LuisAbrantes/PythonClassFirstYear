'''
Faça um programa para guardar os nomes de diversos alunos de uma escola, e apresente ao final a lista de todos os nomes dos alunos cadastrados.
'''
medias = list()
nomes = list()

qtdeAluno = int(input("Qual é a quantidade de alunos? "))

contador = 0 
while(contador < qtdeAluno):
    n = input("Digite o nome de um aluno: ")
    v = float(input("Nota: "))

    nomes.append(n)
    medias.append(v)

    contador += 1

contador = 0
while(contador<qtdeAluno):
    if medias[contador] >= 6.0:
        print(nomes[contador])

    contador += 1  

