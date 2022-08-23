import json
filename = "DbOnlyDict.txt"

def saveData(data):
    file = open(filename, "w") # append
    json.dump(data, file)
    file.close()

def loadData():
    file = open(filename, "r")
    jsonText = file.read()
    file.close()
    return json.loads(jsonText)

note = {}
note["T1"] = "X1";
note["T2"] = "X2";
note["T3"] = "X3";
note["T4"] = "X4";
note["T5"] = "X5";

#for i in range(4):
saveData(note)

notes2 = {}
#for i in range(3):
notes2 = loadData()
print(notes2)


#