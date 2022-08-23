import json
filename = "NotesDb.txt"
key = "Titulo"
val = "Texto"

def saveData(data):
    file = open(filename, "w") # write
    json.dump(data, file)
    file.close()

def loadData():
    try:  # tratamento de erro
        file = open(filename, "r")
    except OSError: # retorna uma lista vazia se não tiver arquivo
        return []
    jsonText = file.read()
    file.close()
    return json.loads(jsonText)

def showMenu():
    print("\n")
    print("┌───────────────────┐")
    print("│ MENU DO NOTAS APP │")
    print("└───────────────────┘")
    print("\n- ESCOLHA UMA DAS OPÇÕES:")
    print("1 - Salvar nova anotação.")
    print("2 - Apresentar anotações.")
    print("3 - Editar uma anotação.")
    print("4 - Apagar uma anotação.")
    print("5 - Sair.")
    return int(input("Digite a opção: "))

notes = loadData()
opt = 0

while (opt != 5):
    opt = showMenu()

    if opt == 1: # Create
        note = {}
        note[key] = str(input("Digite o título: "))
        note[val] = str(input("Digite o texto : "))
        notes.append(note)
        saveData(notes)

    if opt == 2: # Read
        counter = 1
        for note in notes:
            print(f"\n──────── NOTA {counter} ────────")
            print(f"{key} = {note[key]}")
            print(f"{val}  = {note[val]}")
            counter += 1

    if opt == 3: # Update
        id = int(input("Digite o número da anotação para alterar: "))
        if id > len(notes):
            print("\n- Nota não existente!")
        else:
            note = notes[id-1]
            note[key] = str(input("Digite o título: "))
            note[val] = str(input("Digite o texto : "))
            saveData(notes)

    if opt == 4: # Delete
        id = int(input("Digite o número da anotação para alterar: "))
        if id > len(notes):
            print("\n- Nota não existente!")
        else:
            notes.pop(id-1)
            saveData(notes)
