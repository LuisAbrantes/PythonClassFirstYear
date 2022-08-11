"""
Sets em Python(Conjuntos):

add(adiciona), update(atualiza), clear, discard
union | (une)
intersection & (todos os dois elementos presentes no dois sets)
difference - (elementos apenas no set da esquerda)
symmetric_defference ^ (Elementos que estão nos dois sets, mas não em ambos)

-set serve também para eliminar elementos duplicados de uma lista.
"""

s1 = set()
s1.add(1)
s1.add(2)
s1.discard(2)
s1.update("Python", [1, 2, 3, 4, 5],{5, 6, 7, 8})

print(s1)