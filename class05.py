a, b, c = input|("Insira os coeficientes da equação do segundo grau: ").split()
a = int(a)
b = int(b)
c = int(c)

#sqrt() é uma função para calcular raiz quadrada de um número
delta = (b**2 - 4*a*c)**5

x1 = (-b + delta)/(2*add)
x2 = (-b - delta)/(2*add)

print("As raízes são x1 = {0} e x2 = {1}".format(x1, x2))