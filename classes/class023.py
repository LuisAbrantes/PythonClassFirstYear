senha = input("Crie uma senha: ")
resp = input("Digite a senha: ")

while(resp!=senha):
    if(resp!=senha):
      print("Senha incorreta. Digite novamente")
      resp = input("Digite a senha: ")

print("Você conseguiu acessar o sistema corretamente.")
