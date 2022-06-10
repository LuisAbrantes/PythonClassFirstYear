'''
Fornecer opções para cadastro de ao menos 2 tipos de elementos a serem armazenados em estruturas de dados.
 Exemplo: Cadastro de funcionários, jogador de futebol, cardápio, paciente, imóvel, etc. 
Fornecer ao menos 2 opções para consulta de dados cadastrados.
 Exemplo: listar dados de um funcionário pelo código ou nome, listar os pedidos em uma data específica, listar os imóveis de um determinado cliente, etc. 
Fornecer ao menos 2 opções de alteração de dados cadastrados.
 Exemplo: alterar o cadastro de um corretor, alterar os dados de um pet, etc. 
Fornecer ao menos 2 opções de exclusão de dados cadastrados
 Exemplo: apagar todos os dados de um cabeleireiro, apagar dados de um aluno, apagar uma compra, etc. 
'''


print("WELCOME TO SUNDERLAND AFC REGISTRATION SYSTEM!")
print("What you want to add? Press 1 to: A new Player; Press 2 to: A new match.")
first_answer = input("")
players_name = []
players_number = []

if first_answer == "1":
    times = int(input("How many players you want to add? "))

    for c in range(0, times):
        players_name.append(input("Player`s name: "))
        players_number.append(input("Player shirt number: "))
        print("")

    for i in range(0, len(players_name)):
        print(players_name[i])
        print(players_number[i])

