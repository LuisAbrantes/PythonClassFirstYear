def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return 0
    return a / b

x = 10
y = 20
print(add(x, y))
print(sub(x, y))
print(mul(x, y))
print(div(x, y))