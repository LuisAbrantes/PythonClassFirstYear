#terceira questão da prova de PBC
#O funcionário chamado Carlos tem um colega chamado João que recebe um salário que equivale a um terço do seu salario. Carlos gosta de fazer aplicações na caderneta de poupança e vai aplicar seu salário integralmente nela, pois está rendendo 3% ao mês. João aplicará seu salário integralmente no fundo de renda fixa, que está rendendo 7% ao mês.
# 1/3  * Carlos = Joao
# Carlos - Poupanca   - 3%/mes
# Joao   - Renda Fixa - 7%/mes
# Rodar:
# pip install colorama
# ou 
# pip3 install colorama
from colorama import Fore, Back
print(Fore.BLUE, end=" ")
print(Back.BLACK, end=" ")

salCarlos = float(input("Digite o salário de Carlos: "))
salJoao = (1/3) * salCarlos
numMeses = 0

while (salJoao < salCarlos):
    salJoao *= 1.07
    salCarlos *= 1.03
    numMeses += 1

print(Fore.YELLOW, end=" ")
print(f"Após {numMeses} meses, os salários serão:")
print(Fore.GREEN, end=" ")
print(f"Patrimônio de Carlos = {salCarlos:.2f}")
print(Fore.BLUE, end=" ")
print(f"Patrimônio de João   = {salJoao:.2f}")
