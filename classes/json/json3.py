arquivo = open("teste.txt", "w")

variavel = ["\nFulano", "\nBeltrano", "\nCiclano"]

for v in variavel:
    arquivo.write(v)

arquivo.close()