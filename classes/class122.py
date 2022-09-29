'''
Aprendendo a associar uma classe a uma outra.

Cada cliente pode ter ao menos uma conta.
'''

class Cliente():

    def __init__(self):
        self.nome = None
        self.idade = None
        self.conta = None

    def cadastraCliente(self):
        self.nome = input("Nome: ")
        self.idade = int(input("Idade: "))
        self.conta = Conta()
        self.conta.cadastraConta()


class Conta():
    def __init__(self):
        self.numeroConta = None
        self.saldo = None

    def cadastraConta(self):
        self.numeroConta = int(input("Número da conta: ")) 
        self.saldo = float(input("Saldo: "))

cliente = Cliente()
cliente.cadastraCliente()


print(cliente.conta.saldo)