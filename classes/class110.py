"""
Sets em Python(Conjuntos) pt.3:

add(adiciona), update(atualiza), clear, discard
union | (une)
intersection & (todos os dois elementos presentes no dois sets)
difference - (elementos apenas no set da esquerda)
symmetric_defference ^ (Elementos que estão nos dois sets, mas não em ambos)

-set serve também para eliminar elementos duplicados de uma lista.
"""

l1 = ["luis", "henrique", "joao"]
l2 = [
    "luis", "joao", "henrique", "henrique", "luis", "joao", "joao", "joao", "joao", "henrique",
    "luis"
]
print(l1 != l2)

l1 = set(l1)
l2 = set(l2)
print(l1 == l2)

if set(l1) == set(l2):
    print("l1 é igual a l2!")
else:
    print("l1 é diferente de l2.")