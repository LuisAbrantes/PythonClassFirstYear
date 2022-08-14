carrinho = []

carrinho.append(("Produto 1", 30))
carrinho.append(("Produto 2", 20))
carrinho.append(("Produto 3", 50))

total = []
for produto in carrinho:
    total.append(produto[1])
print(sum(total))