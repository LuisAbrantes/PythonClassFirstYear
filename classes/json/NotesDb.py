import json
filename = "NotesDb.txt"
key = "title"
val = "text"

def saveData(data):
    file = open(filename, "w") # write
    json.dump(data, file)
    file.close()

def loadData():
    try:  # tratamento de erro
        file = open(filename, "r")
    except OSError:
        return []
    jsonText = file.read()
    file.close()
    return json.loads(jsonText)

def showMenu():
    print("\nBEM-VINDO AO NOTAS APP.")
    print("\nESCOLHA UMA DAS OPÇÕES:")
    print("1 - Salvar nova alteração.")
    print("2 - Apresentar anotações.")
    print("3 - Editar uma anotação.")
    print("4 - Apagar uma anotação.")
    print("5 - Sair.")
    return int(input("Digite a opção: "))

notes = []
notes = loadData()
saveData(notes)

while (True):
    opt = showMenu()
    if opt == 1: # Create
        note = {}
        note[key] = str(input("Digite o título: "))
        note[val] = str(input("Digite o texto : "))
        notes.append(note)
        saveData(notes)

    if opt == 2: # Read
        for note in notes:
            print(f"{key} = {note[key]}")
            print(f"{val} = {note[val]}")

    if opt == 3: # Update
        id = int(input("Digite o número da anotação para alterar: "))
        note = notes[id]
        note[key] = str(input("Digite o título: "))
        note[val] = str(input("Digite o texto : "))
        saveData(notes)

    if opt == 4: # Delete
        id = int(input("Digite o número da anotação para alterar: "))
        notes.pop(id)
        saveData(notes)

    if opt == 5:
        exit()