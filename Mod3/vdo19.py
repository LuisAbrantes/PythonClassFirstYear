# lista = [1, 2, 3, 4, 5]
# lista = 12345
# print(hasattr(lista, "__iter__"))


import sys
import time

l1 = [x for x in range(100000)]
l2 = [x for x in range(100000)]

for v in l2:
    print(v)

# def gera():
#     r = []
#     for n in range(100):
#         r.append(n)
#         time.sleep(0.1)
#     return r

# g = gera()

# for v in g:
#     print(v)



