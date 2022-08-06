#Dicionários - Curso

import copy

d1 = {1:"a", 2:"b", 3:"c", "d":["Luis", "Henrique"]}
# v = d1.copy()
v = copy.deepcopy(d1)

v[1] = "Luis"
v["d"] = ("Henrique", "Luis")

print(d1)
print(v)