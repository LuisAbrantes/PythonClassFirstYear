string = "012345678901234567890123456789012345678901234567890123456789"
n = 10
contadores = [i for i in range(0, len(string), n)]
tuplas = [(i, i+n) for i in range(0, len(string), n)]
listas = [string[i:i+n] for i in range(0, len(string), n)]
raw = [f"string[{i}:{i+n}]" for i in range(0, len(string), n)]
retorno = [(i, i+n) for i in range(0, len(string), n)]
print(contadores)
print(tuplas)
print(raw)
print(listas)