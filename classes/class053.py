# Números primos

n = int(input("Até qual número quer imprimir primos:"))
for i in range(0, n):
    isPrime = True
    if i==0 or i==1:
        isPrime = False
    for j in range(2, i//2+1):
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        print(i)