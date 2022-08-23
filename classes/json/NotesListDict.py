import json
filename = "DbListDict.txt"

def saveData(data):
    file = open(filename, "w") # write
    json.dump(data, file)
    file.close()

def loadData():
    file = open(filename, "r")
    jsonText = file.read()
    file.close()
    return json.loads(jsonText)

notes = []; note = {}
note["title"] = "T1"; note["text"] = "X1"

for i in range(4):
    notes.append(note.copy())

saveData(notes)
notes2 = loadData()

print(notes2)
