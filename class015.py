#questão 3 da primera prova de pbc


preco_fab = float(input("Insira o preço de fábrica: "))

#primeira tabela de preço
if(preco_fab <= 12000):
    precofinal = preco_fab + (preco_fab*0.05)
    print(precofinal)

#segunda tabela de preço
elif(preco_fab >= 12000 and preco_fab <= 25000):
    precofinal = preco_fab + (preco_fab*0.1) + (preco_fab*0.15)
    print(precofinal)

#terceira tabela de preço
else:
    precofinal = preco_fab + (preco_fab*0.15) + (preco_fab*0.2)