#terceira questão da prova de PBC

#O funcionário chamado Carlos tem um colega chamado João que recebe um salário que equivale a um terço do seu salario. Carlos gosta de fazer aplicações na caderneta de poupança e vai aplicar seu salário integralmente nela, pois está rendendo 3% ao mês. João aplicará seu salário integralmente no fundo de renda fixa, que está rendendo 7% ao mês.

# Construa um programa que deverá calcular e mostrar a quantidade de meses necessários para que o valor pertencente a João iguale ou ultrapasse o valor pertencente a Carlos. Teste com outros valores para as taxas.

# 1/3  * Carlos = Joao
# Carlos - Poupanca   - 3%/mes
# Joao   - Renda Fixa - 7%/mes


salCarlos = float(input("Digite o salário de Carlos: "))
salJoao = (1/3) * salCarlos
numMeses = 0

while (salJoao < salCarlos):
    salJoao *= 1.07
    salCarlos *= 1.03
    numMeses += 1

print(f"Após {numMeses} meses, os salários serão:")
print(f"Patrimônio de Carlos = {salCarlos:.2f}")
print(f"Patrimônio de João   = {salJoao:.2f}")
