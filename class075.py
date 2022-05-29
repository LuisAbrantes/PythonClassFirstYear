frase = "o rato roeu a roupa do rei de roma" #Iterável
tamanho_frase = len(frase)
contador = 0
novaString = ''

input_usuario = input("Qual letra deseja colocar em maiúscula? ")

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == input_usuario:
        novaString += input_usuario.upper()
    else:
        novaString += letra
    contador += 1

print(novaString)    