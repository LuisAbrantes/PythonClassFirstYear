#Dicionários - Curso

d1 = {
    1:2,
    2:3,
    4:5,
}


"""
Comando 'pop()' serve para excluir um item a partir da chave.
'popitem()' serve para excluir o último item, independente de qual seja.
"""
d1.pop(4)
print(d1)

#

d2 = {
    "a":"b",
    "c":"d",
}
"""
O comando 'update()' serve para concatenar os valores do dicionário(por exemplo) que está 
dentro do parênteses, juntamente aos valores do dicionário que está antes do comando.
"""
d1.update(d2)
print(d1)