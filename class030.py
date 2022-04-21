#Atividade 2 / Exercicio 1

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

media = (n1+n2+n3+n4)/2
if (media <= 6):
    print("Ta de rec")
else:
    print("Passou de ano")