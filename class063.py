#Introdução à LISTAS

notas = list()

qtdeNotas = int(input("Qual é a quantidade de notas? "))

contador = 0 
while contador < qtdeNotas:
    nota = float(input("Insira uma nota: "))
    nota.append(nota)
    contador += 1

contador = 0
soma = 0 
while contador < qtdeNotas:
    soma += nota[contador]
    contador += 1

#calcular a média:

soma = notas[contador]
media = soma/qtdeNotas

print(notas)