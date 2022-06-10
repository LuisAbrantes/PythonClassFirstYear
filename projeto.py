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
players = []
player_details = {}
matchs = []
match_details = {}


if first_answer == "1":
    times = int(input("How many players you want to add? "))

    for c in range(0, times):
        player_details["name"] = input("Player`s name: ")
        player_details["number"] = input("Player shirt number: ")
        print("")
        players.append(player_details.copy())
    print(players)

if first_answer == "2":
    times = int(input("How many matchs you want to add? "))

    for c in range(0, times):
        match_details["Stadium"] = input("Stadium name: ")
        match_details["team"] = input("Against who?: ")
        print("")
        matchs.append(match_details.copy())
    print(matchs)