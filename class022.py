opt=0
while(opt!=3):
    print("1- Converter de celsius para fahrenheit.")
    print("2- Converter de fahrenheit para celsius.")
    print("3- Sair")
    opt = int(input("Digite sua resposta: "))

    if(opt==1):
        celsius = float(input("Digite a temperatura em celsius: "))
        fahreiheit = 1.8*celsius+32
        print("A temperatura em fahreiheit é: ", fahreiheit)
    elif(opt==2):
        fahreiheit = float(input("Entre com a temperatura em fahreiheit: "))
        celsius = (fahreiheit-32)*(5/9)
        print("A temperatura em celsius é: ", celsius)
    elif(opt==3):
     print("Fim do programa!")

