'''
Faça um programa que contenha uma classe jogador.
Cada jogador pode ter:
* nome
* classe
* equipamentos

Cada equipamento pode ter:
* nome
* tipo
* durabilidade
'''

class Jogador():

    def __init__(self):
        self.nomeJogador = None
        self.classe = None
        self.equipamentos = None

    def cadastraJogador(self):
        self.nomeJogador = input("Nome do jogador: ")
        self.classe = input("Classe do jogador: ")

        self.equipamentos = list()
        qtd = int(input(f"\nQuantos equipamentos {self.nomeJogador} tem? "))
        contador = 1
        if qtd != 0:
            while not contador > qtd:
                equipamento = Equipamento()
                equipamento.cadastraEquipamento()
                self.equipamentos.append(equipamento)
                contador += 1
    
    def apresentaJogador(self):
        print(f"\nNome do jogador:{self.nomeJogador}")
        print(f"Classe do jogador:{self.classe}")

    def apresentaEquipamento(self):
        for equipamento in self.equipamentos:
            equipamento.apresenta()


    
class Equipamento():
    def __init__(self):
        self.nomeEquipamento = None
        self.tipo = None
        self.durabilidade = None

    def cadastraEquipamento(self):
        self.nomeEquipamento = input("\nNome do equipamento: ")
        self.tipo = input("Tipo do equipamento: ")
        self.durabilidade = int(input("Durabilidade do equipamento: "))

    def apresenta(self):
        print(f"\nNome: {self.nomeEquipamento}")
        print(f"Tipo: {self.tipo}")
        print(f"Durabilidade: {self.durabilidade}")


jogador1 = Jogador()
jogador1.cadastraJogador()
jogador1.apresentaJogador()
jogador1.apresentaEquipamento()