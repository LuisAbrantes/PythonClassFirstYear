#Vídeo 10 - Estudo de Tuplas.

t1 = (1, 2, 3, 4, 5)
t1 = list(t1)
t1[1] = 3000
t1 = tuple(t1)

t2 = (10, 20, "Andre")
a, c, _ = t2

print(t1)

def CalculaResultante(vetorEmX : float, vetorEmY:float) -> tuple(float, float):
    return 0.0