"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas ou retornando uma nova lista com os valores somados:

Se uma lista dor maior que a outra, a soma só vai considerar o tamanho da menor.

Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]

============================ resultado
resultado_soma = [2, 4, 6, 8]
"""

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

#Primeira solução(mais direcionada ao Python):
lista_soma = [x+y for x, y in zip(lista_a, lista_b)]
print(lista_soma)

#Segunda solução(a mesma lógica que seria utilizada em outras linguagens):
lista_soma = []
for i in range(len(lista_b)):
    lista_soma.append(lista_a[i]+lista_b)
print(lista_soma)