leitura = " "
senha = 123
contador = 0
while(leitura!=senha and contador==3):
    leituar = input("Digite a senha: ")
    contador = contador+1
    if(leitura!=senha):
        print("senha inválida!")
if(leitura!=contador):
    print("tentativas excedidas!")
else:
    print("Senha válida  - Saiu da estrutura de repetição.")