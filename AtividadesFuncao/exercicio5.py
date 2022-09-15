'''
Faça um programa que tem uma função que recebe uma string 
como parâmetro e a criptografa trocando as vogais por símbolos diferentes. 
Aplique a seguinte substituição: 
a = $, e = #, i = @, o = &, u = !

Faça uma segunda função que recebe a string criptografada e a descriptografa.
'''

def criptografa2(texto):
    for c in texto:
        if c in "Aa":
            c = "$"
        if c in "Ee":
            c = "#"
        if c in "Ii":
            c = "@"
        if c in "Oo":
            c = "&"
        if c in "Uu":
            c = "!"
    return texto

def criptografa3(texto):
    lista = list(texto)
    for i in range(0, len(lista)-1):
        if lista[i] in "Aa":
            lista[i] = "$"
        if lista[i] in "Ee":
            lista[i] = "#"
        if lista[i] in "Ii":
            lista[i] = "@"
        if lista[i] in "Oo":
            lista[i] = "&"
        if lista[i] in "Uu":
            lista[i] = "!"
    return ''.join(lista)

def criptografa(texto):
    r = ""
    for c in texto:
        if c in "Aa":
            r = r + "$"
        elif c in "Ee":
            r = r + "#"
        elif c in "Ii":
            r = r + "@"
        elif c in "Oo":
            r = r + "&"
        elif c in "Uu":
            r = r + "!"
        else:
            r += c
    return r


nString = str(input("Digite o texto para ser criptografado: "))
print(f'A frase criptografada é "{criptografa(nString)}".')
