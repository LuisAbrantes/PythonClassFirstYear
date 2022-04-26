#Atividade 4 / Exercicio 5

contador = 0
#pergunta 1
print("A música mais ouvida do spotify foi 'Cavalo de Tróia'. Digite - S para sim e - N para não.")
acertou = False
while not acertou:
    jogador = str(input(""))
    if jogador == "N":
        print("Acertou!")
        contador+=1
    else:
        print("Errou!")
    break

print()

#pergunta 2
print("Neymar tem uma Champions League. Digite - S para sim e - N para não.")
acertou = False
while not acertou:
    jogador = str(input(""))
    if jogador == "S":
        print("Acertou!")
        contador += 1
    else:
        print("Errou!")
    break

print()

# pergunta 3
print("Zlatan Ibrahimovic tem mais de 50 gols em Champions League. Digite - S para sim e - N para não.")
acertou = False
while not acertou:
    jogador = str(input(""))
    if jogador == "S":
        print("Acertou!")
        contador += 1
    else:
        print("Errou! Ibrahimovic tem 49 gols.")
    break

print()

#pergunta 4
print("Mc Kevin que canta a música 'Joga Bola'. Digite - S para sim e - N para não.")
acertou = False
while not acertou:
    jogador = str(input(""))
    if jogador == "S":
        print("Acertou!")
        contador += 1
    else:
        print("Errou!")
    break

print(f"Você acertou {contador}x.")