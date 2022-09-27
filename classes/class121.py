'''
Faça uma aplicação que permite cadastrar vários clientes de um banco.
Cada cliente possui os seguintes dados:
    cpf
    nome
    numero da conta
    saldo

A aplicação deve permitir consultar o saldo de um cliente escolhido.
'''

class Cliente():

    def __init__(self):
        self.cpf = None
        self.nome = None
        self.numeroConta = None
        self.saldo = None

    def cadastraDados(self):
        self.cpf = input("CPF: ")
        self.nome = input("Nome: ")
        self.numeroConta = int(input("Número da conta: ")) 
        self.saldo = float(input("Saldo: "))

    def listaDados(self):
        print(f"CPF: {self.cpf};\n Nome: {self.nome};\n Número da conta: {self.numeroConta};\n Saldo da conta: {self.saldo}.")

cliente1 = Cliente()
cliente1.cadastraDados()
cliente1.listaDados()   