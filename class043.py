#Atividade 4 / Exercicio 3

print("Primeiramente, você irá inserir o preço original do produto, e depois, a sigla do estado em que deseja enviar.")

p = float(input("Insira o preço do produto: "))
e = str(input("Qual estado você desenja enviar? Digite uma das siglas: MG SP RJ MS. "))

if e == "MG":
    p = (p*0.07)+p
    print("O preço é ", p, "reais.")

elif e == "SP":
    p = (p*0.12)+p
    print("O preço é ", p, "reais.")

elif e == "RJ":
    p = (p*0.15)+p
    print("O preço é ", p, "reais.")

elif e == "MS":
    p = (p*0.08)+p
    print("O preço é ", p, "reais.")

else: 
    print("Digite um endereço válido.")