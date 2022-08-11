"""
Manupulando strings - Aula 6:
 *Strings Indices
 *Fatiamento de Strings [inicio:fim:passo]
 *Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo
"""

#positivos  [012345678]
texto = 'Python s2'
#negativos  -[987654321]

new_string = texto[0:6:2]
print(new_string)

print ( len(texto) )

for letra in texto:
    print ( letra )