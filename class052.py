# Fibonacci

print("-"*30)
print("Sequência de Fibonacci")
print("-"*30)

n = int(input("Quantos termos você quer mostrar? "))
t1 = 0
t2 = 1

print("~"*100)
print(f"{t1} --> {t2} ", end="")
contador = 3
while contador <= n:
    t3 = t1 + t2
    print(f"--> {t3} ", end="")
    t1 = t2
    t2 = t3
    contador += 1
print(f"\nO {n}o termo é {t3}.")
print("\nFIM")
print("~"*100)