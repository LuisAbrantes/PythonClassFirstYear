#Atividade 4 / Exercicio 4

txt = "Insira um número: "
n = float(input(txt))
s = 0
qtd = 0

while n > 0:
    s += n
    qtd += 1
    n = float(input(txt))

print(f"Média: {s/qtd}")
print(f"Quadrado da soma: {s**2}")
print(f"Cubo da soma: {s**3}")
