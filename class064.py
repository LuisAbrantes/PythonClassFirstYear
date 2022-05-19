'''
Faça um programa para guardar os nomes de diversos alunos de uma escola, e apresente ao final a lista de todos os nomes dos alunos cadastrados.
'''
alunos = list()

qtdeAluno = int(input("Qual é a quantidade de alunos? "))

contador = 0 
while contador < qtdeAluno:
    aluno = input("Digite o nome de um aluno: ")
    alunos.append(aluno)
    contador += 1



print(alunos)

