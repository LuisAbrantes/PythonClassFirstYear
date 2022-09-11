'''
Bloco de notas
'''

import json
tit = "Título"
cont = "Conteúdo"

def salva(conteudo):
    arquivo = open("blocoNotas.txt", "w")
    json.dump(conteudo, arquivo)
    arquivo.close()

def carrega():
    arquivo = open("blocoNotas.txt", "r")    
    jsonText = arquivo.read()
    arquivo.close()
    return json.loads(jsonText)

def menu():
    print("\nBEM-VINDO AO MENU. O QUE DESEJA FAZER?")
    print("1. Adicionar uma nova nota; \n2. Excluir uma nota; \n3. Editar uma nota; \n4. Apresentar anotações; e \n5.Sair")
    return int(input("Insira um número: "))

notas = carrega()
resp = 0

while (resp!=5):
    resp = menu()

    if resp == 1:
        nota = dict()
        nota[tit] = str(input("Digite o título da nota: "))
        nota[cont] = str(input("Digite o conteúdo da nota: "))
        notas.append(nota)
        salva(notas)
    
    if resp == 2:
        apaga = str(input("Insira o título da apresentação em que deseja apagar: "))
        for nota in notas:
            if apaga == nota[tit]:
                notas.remove(nota)
        print("Pronto.")

    if resp == 3:
        edita = str(input("Insira o título da apresentação em que deseja editar: "))
        for nota in notas:
            if edita == nota[tit]:
                nota[tit] = str(input("Digite o novo título da nota: "))
                nota[cont] = str(input("Digite o novo conteúdo da nota: "))
                salva(notas)
    if resp == 4:
        contador = 1
        for nota in notas:
            print(f"\n──────── NOTA {contador} ────────")
            print(f"{tit} = {nota[tit]}")
            print(f"{cont}  = {nota[cont]}")
            contador += 1
