'''
Faça um programa que contenha informações de diversos alunos de uma escola. Cada aluno possui:

* nome

* idade

* media

O programa deve permitir cadastrar quantos alunos o usuário quiser. Ao final do programa apresente os dados de todos os alunos.
'''

class Aluno():

    def __init__(self):
        self.nome = None
        self.idade = None
        self.media = None

    def cadastraDados(self):
        self.nome = input(f"\nNome do aluno {contador}: ")
        self.idade = input(f"Idade do aluno {contador}: ")
        self.media = input(f"Média do aluno {contador}: ")
    
    def listaDados(self):
        print(f"\nNome: {self.nome}; \nIdade: {self.idade}; \nMedia: {self.media}")


qtd = int(input("Quantos alunos deseja cadastrar? "))
listaAluno = []
contador = 1

while not (contador > qtd):
    aluno = Aluno()
    aluno.cadastraDados()
    listaAluno.append(aluno)
    aluno.listaDados()
    contador +=1