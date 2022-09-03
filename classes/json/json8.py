'''
2. Faça um programa que tem uma função que lê um arquivo texto 
e conta quantas vogais têm neste arquivo.
'''

def loadData(filename):
    file = open(filename, "r")
    text = file.readlines()
    file.close()
    return text

def countVowel(text):
    counter = 0
    for word in text:
        for letter in word:
            if (letter.lower() in "a" or
                letter.lower() in "e" or 
                letter.lower() in "i" or 
                letter.lower() in "o" or 
                letter.lower() in "u"):
                counter += 1
    return counter

filename = "/Users/luis/python/PythonClassFirstYear/classes/json/arquivo.txt"
text = loadData(filename)
print(text)
totalVowel = countVowel(text)
print(totalVowel)


# def conta_vogal(frase, contador):
#     frase = frase.split()
#     for palavra in frase:
#         for letra in palavra:
#             if letra.lower() in "aeiou":
#                 contador+=1
#     return print(f"\nNa frase {frase} temos: {contador} vogais", end="")

# frase = str(input("Digite a frase para contabilizar a quantidade de vogais: \n--> "))
# contador = 0
# conta_vogal(frase, contador)

# print(f"\nNa palavra {palavra.upper()} temos: ", end="")
