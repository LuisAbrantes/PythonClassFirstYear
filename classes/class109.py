"""
Sets em Python(Conjuntos) pt.3:

add(adiciona), update(atualiza), clear, discard
union | (une)
intersection & (todos os dois elementos presentes no dois sets)
difference - (elementos apenas no set da esquerda)
symmetric_defference ^ (Elementos que estão nos dois sets, mas não em ambos)

-set serve também para eliminar elementos duplicados de uma lista.
"""

s1 = {1, 2, 3, 4, 5, 7}
s2 = {1, 2, 3, 4, 5, 6}
# s3 = s1 | s2 #--> une os "sets".
# s3 = s1 & s2 #--> considera apenas os termos que têm em comum.
# s3 = s1 - s2 #--> considera apenas os termos que existem no set da esquerda e não existem no da direita
# s3 = s1 ^ s2 #--> considera apenas os termos que existem em apenas um dos sets / 6 e 7 neste caso.

# print(s3)