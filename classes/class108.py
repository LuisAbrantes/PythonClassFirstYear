"""
Sets em Python(Conjuntos) pt.2:

add(adiciona), update(atualiza), clear, discard
union | (une)
intersection & (todos os dois elementos presentes no dois sets)
difference - (elementos apenas no set da esquerda)
symmetric_defference ^ (Elementos que estão nos dois sets, mas não em ambos)

-set serve também para eliminar elementos duplicados de uma lista.
"""

l1 = [1,2,1,1,3,4,5,6,6,6,6,6,7,8,9, "Luis", "Luis"]
l1 = set(l1)
l1 = list(l1)

print(l1[-1 ])