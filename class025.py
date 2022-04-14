qt_alunos = 10

nota = list()

contador = 0
while(contador < qt_alunos):
    valor = float(input("Entre com a nota do aluno "+str(contador+1)+": "))
    nota.append(valor)
    contador += 1

soma = 0
contador=0
while(contador<qt_alunos):
    soma = soma+nota[contador]
    contador = contador+1

media = soma/qt_alunos
print(media)
