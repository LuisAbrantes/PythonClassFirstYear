# Atividade 4 / Exercicio 7
# 1/3  * Carlos = Joao
# Carlos - Poupanca   - 2%/mes
# Joao   - Renda Fixa - 5%/mes


salCarlos = float(input("Digite o salário de Carlos: "))
salJoao = (1/3) * salCarlos
numMeses = 0

while (salJoao < salCarlos):
    salJoao *= 1.05
    salCarlos *= 1.02
    numMeses += 1

print(f"Após {numMeses} meses, os salários serão:")
print(f"Patrimônio de Carlos = {salCarlos:.2f}")
print(f"Patrimônio de João   = {salJoao:.2f}")
