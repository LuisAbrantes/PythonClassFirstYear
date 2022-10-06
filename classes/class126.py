'''
Altere a resposta da questão 1 para ter um método de alteração de um único atributo da classe.
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

    def editaNome(self):
        self.nome = input("Novo nome: ")

qtd = int(input("Quantos alunos deseja cadastrar? "))
listaAluno = []
contador = 1

while not (contador > qtd):
    aluno = Aluno()
    aluno.cadastraDados()
    listaAluno.append(aluno)
    aluno.listaDados()
    contador +=1

alterar = input("Deseja alterar algum nome (S/N)? ")
if alterar == "S":
    nome = input("Nome a ser buscado: ")
    for aluno in listaAluno:
        if (aluno.nome == nome):
            aluno.editaNome()
            aluno.listaDados()
            break

