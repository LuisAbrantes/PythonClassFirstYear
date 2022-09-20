'''
Faça um programa que possa cadastrar dados de funcionários de uma empresa.
Cada funcionário tem:
* nome
* idade
* cpf
* salário

No programa é possível: 
* cadastrar dados
* listar dados cadatrados

'''

class Funcionario():

    #Construtor da classe
    def __init__(self):
        self.nome = None
        self.idade = None
        self.cpf = None
        self.salario = None

    def cadastraDados(self):
        self.nome = input("\nInsira o nome do funcionário: ")
        self.idade = int(input("Insira a idade do funcionário: "))
        self.cpf = input("Insira o cpf do funcionário: ")
        self.salario = float(input("Insira o salário do funcionário: "))

    def listaDados(self):
        print(f"\nNome: {self.nome}; \nIdade: {self.idade}; \nCPF: {self.cpf}; e \nSalário: {self.salario} \n.")

    def editaNome(self):
        self.nome = input("Insira o novo nome do funcionário:")


qtd = int(input("Entre com a quantidade: "))

listaFunc = []

cont = 0
while(cont < qtd):
    funcionario = Funcionario()
    funcionario.cadastraDados()
    listaFunc.append(funcionario)
    cont +=1

nome = input("Digite o nome a ser buscado: ")

encontrou = False
for funcionario in listaFunc:
    if (funcionario.nome == nome):
        encontrou = True
        break
    else:
        encontrou = False

if (encontrou == True):
    print("Funcionário encontrado.")
else:
    print("Funcionário não encontrado.")


# funcionario1 = Funcionario()
# funcionario2 = Funcionario()

# funcionario1.cadastraDados()
# funcionario2.cadastraDados()

# funcionario1.listaDados()
# funcionario2.listaDados()