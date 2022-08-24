'''
Faça um programa que tem uma função que recebe uma string como parâmetro 
e a criptografa trocando as vogais por símbolos diferentes. Aplique a seguinte substituição: 
a = $, e = #, i = @, o = &, u = !

Faça uma segunda função que recebe a string criptografada e a descriptografa.
'''

def cript():
    txt = input("Digite algo para ser criptografado: \n-->")
    txt = txt.replace("a", "$")
    txt = txt.replace("e", "#")
    txt = txt.replace("i", "@")
    txt = txt.replace("o", "&")
    txt = txt.replace("u", "!")
    return txt

def descript():
    txt = input("\nDigite uma mensagem criptograda \n-->")
    txt = txt.replace("$", "a")
    txt = txt.replace("#", "e")
    txt = txt.replace("@", "i")
    txt = txt.replace("&", "o")
    txt = txt.replace("!", "u")
    return txt


print(f"\nO (primeiro) texto, criptografado é: {cript()}.\n")
print(f"\nO (segundo) texto, descriptografado é: {descript()}.\n")