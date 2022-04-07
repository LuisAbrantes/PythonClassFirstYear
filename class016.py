#questão 4 da primeira prova de pbc

conta = int(input("Digite 1 para: 'km/h para m/s', ou 2 para: 'm/s para km/h'. "))

if(conta==1):
    num_inicial = float(input("Digite o número em km/h para a convertê-lo em m/s"))
    num_final = num_inicial * 3.6
    print("O número que você escreveu convertido para m/s é: ", num_final)
elif(conta==2):
    num_inicial = float(input("Digite o número em m/s para a convertê-lo em km/h"))
    num_final = num_inicial / 3.6
    print("O número que você escreveu convertido para km/h é: ", num_final)
else:
    print("Você deveria ter digitado 1 ou 2.")
