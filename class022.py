opt=0
while(opt!=3):
    print("1- Converter de celsius para fahrenheit.")
    print("2- Converter de fahrenheit para celsius.")
    print("3- Sair")
    opt = int(input("Digite sua resposta: "))

    if(opt==1):
        temp = float(input("Digite a temperara em celsius: "))
        print("F: ", temp*1.8+32)
    elif(opt==2):
     print("converte para celsius")
    elif(opt==3):
     print("Fim do programa!")