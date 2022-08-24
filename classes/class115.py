'''
4- Faça um programa que tem uma função que recebe uma lista de números como parâmetro, 
e retorna a soma de todos os números da lista.
'''


lista = []
contador = 0

def func(lista):
    while True:
        print("\nBEM-VINDO AO MENU: SELECIONE UMA DAS OPÇÕES: \n1- Adicionar mais um item à lista; \n2- Sair e mostrar soma dos itens da lista.")
        resp = int(input("--> "))
        if resp == 1:
            n = float(input("Digite o número que irá adicionar na lista: "))
            lista.append(n)
        elif resp == 2:
            lista_somada = sum(lista)
            return print(f"A lista é: {lista} e o resultados dos itens somados é igual a: {lista_somada}.") 
        else:
            return print("Digite uma opção válida.")

func(lista)