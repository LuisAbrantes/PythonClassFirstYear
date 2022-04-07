#questão 2 da primeira prova de pbc
num = int(input("Insira um número para a seleção de divisores: "))

if(num%5==0 and num%3==0):
    print("É inválido pois é divisível por 5 e por 3 simultaneamente.")
elif(num%5==0):
    print("É válido pois é divisível por 5.")
elif(num%3==0):
    print("É válido pois é divisível por 3.")
else: 
    print("Não é válido pois não é divisível por nenhum dos dois números.")