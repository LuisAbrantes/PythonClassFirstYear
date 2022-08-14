"""
Zip - Unindo iteráveis
Zip_longest - Intertools
"""

from itertools import zip_longest, count

indice = count()
cidades = ["San Fransisco", "Las Vegas", "Grand Canyon Village", "Palo Alto", "Others"]
estados = ["CA", "NV", "AZ"]

cidades_estados = zip(
    indice,
    estados,
    cidades
)

for indice, estado, cidade in cidades_estados:
    print(indice, estado, cidade)