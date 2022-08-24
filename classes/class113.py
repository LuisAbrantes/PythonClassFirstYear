'''
2- Faça um programa que tem uma função que recebe uma lista de números por parâmetro, 
e retorna a quantidade de números pares nesta lista.
'''

lista = []
contador = 0

def func(contador, lista):
    while True:
        print("\nBEM-VINDO AO MENU: SELECIONE UMA DAS OPÇÕES: \n1- Adicionar mais um item à lista; \n2- Sair e mostrar lista.")
        resp = int(input("--> "))
        if resp == 1:
            n = float(input("Digite o número que irá adicionar na lista: "))
            lista.append(n)
            if n%2 == 0:
                contador +=1
        elif resp == 2:
            return print(f"A lista é: {lista} e existem {contador} números pares nela.") 
        else:
            return print("Digite uma opção válida.")

func(contador, lista)