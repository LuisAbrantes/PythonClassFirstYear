#Jogo da forca em Python utilizando Listas[]

secreto = "perfume"
digitadas = []
chances = 3

while True:
    if chances == 0:
        print("Você perdeu, suas chances acabaram!")
        break 

    letra = input("Insira uma letra: ")

    if len(letra) > 1:
        print("Digite apenas uma letra.")
        continue

    digitadas.append(letra)

    if letra in secreto:
        print("Muito bem, a letra digitada faz parte da palavra decreta.")
    else:
        print("A letra não existe na palavra secreta.")
        digitadas.pop()

    secreto_temporario = ""
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += "*"

    if secreto_temporario == secreto:
        print(f'Que legal! Você acertou! A palavra certa é "{secreto}"')
    else:
        print(f"A palavra correta está assim: {secreto_temporario}")

    if letra not in secreto: 
        chances -= 1

    print(f"Você ainda tem {chances} chances.")
    print()