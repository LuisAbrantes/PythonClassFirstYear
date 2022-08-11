lista = [1, 2, 3, 4, 5]
teste = list()
contador = 0 
while(contador < 4):
    valor = lista[contador]*2
    teste.append(valor)
    teste.append((contador, valor))
    contador += 1

print(teste)