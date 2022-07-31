'''
Split, Join, Enumerate em Python
 *Split - Dividir uma string # str
 *Join - Juntar uma lista #str
 *Enumerate - Enumerar elementos da lista # iteráveis
'''

string = "O Brasil é o o o país do futebol, o Brasil é penta."
lista_1 = string.split(" ")
lista_1 = string.split(",")

palavra = ""
contador = 0
for valor in lista_1:
    qtd_vezes = lista_1.count(valor)