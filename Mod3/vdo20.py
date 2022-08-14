#listas, tuplas, str --> Sequences --> Iteráveis

nome = "Luis Henrique"
iterador = iter(nome)
gerador = (letra for letra in nome)

#GERADOR:
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))

print("OLHA O FOR!")

for letra in gerador:
    print(letra)

print(next(gerador))


print()
print()


#ITERADOR
try:
    print(next(iterador)) #L
    print(next(iterador)) #U
    print(next(iterador)) #I
    print(next(iterador)) #S
    print(next(iterador)) 
    print(next(iterador)) #H
    print(next(iterador)) #E
    print(next(iterador)) #N
    print(next(iterador)) #R 
    print(next(iterador)) #I
    print(next(iterador)) #Q
    print(next(iterador)) #U
    print(next(iterador)) #E
except:
    pass

print("CADÊ OS VALORES?")
for valor in iterador:
    print(valor)

for letra in nome:
    print(letra)

print("#"*80)

for letra in nome:
    print(letra)

print(nome)