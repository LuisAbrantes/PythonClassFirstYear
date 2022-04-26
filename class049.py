# Atividade 5 / Exercicio 2

lab = float(input("Insira a nota do Trabalho de Laboratório: "))
avaliação = float(input("Insira a nota da Avaliação Semestral: "))
exame = float(input("Insira a nota do Exame Final: "))

media = ((lab*2)+(avaliação*3)+(exame*5))/(2+3+5)

print(f"A média do aluno é {media}")