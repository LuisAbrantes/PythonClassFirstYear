'''Faça um programa que contenha informações de diversos ônibus de uma empresa. Cada ônibus possui:

* kilometragem

* fabricante

* nome do motorista

O programa deve permitir cadastrar quantos ônibus o usuário quiser. Ao final do programa apresente os dados do ônibus com a menor kilometragem. 
'''

class Carro():

    def __init__(self):
        self.kilometragem = None
        self.fabricante = None
        self.nomeMotorista = None

    def cadastraDados(self):
        self.kilometragem = float(input(f"kilometragem do carro {contador}: "))
        self.fabricante = input(f"Fabricante do carro {contador}: ")
        self.nomeMotorista = input(f"Nome do Motorista do carro {contador}: ")



qtd = int(input("Quantos carros deseja cadastrar? "))
listaCarro = []
contador = 1

while not (contador > qtd):
    carro = Carro()
    carro.cadastraDados()
    listaCarro.append(carro)
    contador +=1


kilo = float(input("Digite a kilometragem máxima percorrida: "))
for carro in listaCarro:
    if (carro.kilometragem < kilo):
        print(f"O carro de {carro.nomeMotorista} entra na kilometragem percorrida exigida.")
    else:
        print(f"O carro de {carro.nomeMotorista} não entra na kilometragem percorrida exigida.")



