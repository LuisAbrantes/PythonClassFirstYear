#Atividade 2 / Exercício 6

idade = int(input("Insira a idade do atleta: "))

if (idade >= 5 and idade <= 7):
    print("A categoria do atleta é Infantil A")
elif (idade >= 8 and idade <= 10):
    print("A categoria do atleta é Infantil B")
elif (idade >= 11 and idade <= 13):
    print("A categoria do atleta é Juvenil A")
elif (idade >= 14 and idade <= 17):
    print("A categoria do atleta é Juvenil B")
elif (idade >= 18):
    print("Sênior")