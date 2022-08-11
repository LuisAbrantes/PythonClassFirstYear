# Atividade 5 / Exercicio 1

preco = float(input("Digite o preço do produto: "))

desconto = preco - (preco*0.1)
parcela = preco / 3
comi_vista = desconto * 0.05
comi_parc = preco * 0.05

print(f"O valor do desconto de 10% é {desconto}")
print(f"O valor de cada parcela 3x sem juros é {parcela}")
print(f"O valor da comissão do vendedor de uma venda à vista é {comi_vista}")
print(f"O valor da comissão do vendedor de uma venda parcelada é {comi_parc}")
