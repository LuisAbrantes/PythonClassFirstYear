'''
For / Else em Python
'''

val = ["Luiz Otavio", "Joaozinho", "Maria"]

for valor in val:
    if valor.lower().startswith("j"):
        continue
    print(valor)