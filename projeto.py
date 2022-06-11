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

players = []
player_details = {}
matchs = []
match_details = {}


while True:

    print("\n\nWELCOME TO SUNDERLAND AFC REGISTRATION SYSTEM!")
    print("What you want to change? Press 0 to: Quit; Press 1 to: Players Menu; Press 2 to: Matchs Menu.")
    first_answer = input("--> ")

    #-------Players Menu--------
    if first_answer == "1":
        print("This is the Players Menu, what you want to do? \n0: Back to main menu \n1: Add a new player \n2: Delete a player \n3: Change a player configuration \n4: See all players")
        second_answer = input("--> ")
        print("")


        if second_answer == "0":
            print("Returning to main menu...")


        elif second_answer == "1":
            times = int(input("How many players you want to add? \n--> "))
            for c in range(0, times):
                player_details["name"] = input("Player name: ")
                player_details["number"] = input("Player shirt number: ")
                print("")
                players.append(player_details.copy())
            print(players)

        
        elif second_answer == "2":
            print("What do you want to delete? \n1: All Players \n2: A Single Player")
            delete_function = input("--> ")
            if delete_function == "1":
                players.clear()
                print("All players deleted.")
                print(players)
            elif delete_function == "2":
                delete_player = input("Player name: ")
                for player in players:
                    if delete_player == player["name"]:
                        players.remove(player)
                        print("Player deleted.")
                        print(players)

        elif second_answer == "3":
            print("What do you want to change? \n1: Player name \n2: Player number")
            change_function = input("--> ")
            if change_function == "1":
                change_player = input("Player number: ")
                for player in players:
                    if change_player == player["number"]:
                        player["name"] = input("New name: ")
                        print("Player name changed.")
                        print(players)
            elif change_function == "2":
                change_player = input("Player name: ")
                for player in players:
                    if change_player == player["name"]:
                        player["number"] = input("New number: ")
                        print("Player number changed.")
                        print(players)


        elif second_answer == "4":
            print(players)

    #---------------------------


    #-------Matchs Menu---------
    elif first_answer == "2":
        print("This is the Matchs Menu, what you want to do? \n0: Back to main menu \n1: Add a new match \n2: Delete a match \n3: Change a match configuration \n4: See all matches")
        second_answer = input("--> ")
        print("")


        if second_answer == "0":
            print("Returning to main menu...")


        elif second_answer == "1":
            times = int(input("How many matchs you want to add? \n--> "))

            for c in range(0, times):
                match_details["opponent"] = input("Opponent's name: ")
                match_details["stadium"] = input("Stadium name: ")
                print("")
                matchs.append(match_details.copy())
            print(matchs)


        elif second_answer == "2":
            print("What do you want to delete? \n1: All Matches \n2: A Single Match")
            delete_function = input("--> ")
            if delete_function == "1":
                matchs.clear()
                print("All matches deleted.")
                print(matchs)
            elif delete_function == "2":
                delete_match = input("Opponent's name: ")
                for match in matchs:
                    if delete_match == match["opponent"]:
                        matchs.remove(match)
                        print("Match deleted.")
                        print(matchs)


        elif second_answer == "3":
            print("What do you want to change? \n1: Opponent's name \n2: Stadium name")
            change_function = input("--> ")
            if change_function == "1":
                change_match = input("Stadium name: ")
                for match in matchs:
                    if change_match == match["stadium"]:
                        match["opponent"] = input("New name: ")
                        print("Opponent's name changed.")
                        print(matchs)
            elif change_function == "2":
                change_match = input("Opponent's name: ")
                for match in matchs:
                    if change_match == match["opponent"]:
                        match["stadium"] = input("New stadium name: ")
                        print("Stadium name changed.")
                        print(matchs)

        elif second_answer == "4":
            print(matchs)
    #---------------------------


    #-------Quit--------
    elif first_answer == "0":
        break
    #---------------------------

    #-------Wrong Answer--------
    else:
        print("Invalid option.")
    #---------------------------
