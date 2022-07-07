'''
1- Crie uma função que exibe uma saudação com os parâmetros saudação e nome.
'''
def saudacao(saudacao, nome):
    print(f"{saudacao} {nome}")

saudacao("Ola", "Joao")
saudacao("Oi", "Maria")
saudacao("Hey", "Eduarda")
print()


'''
2- Crie uma funcao que recebe 3 numeros como parametros e exiba a soma entre eles
'''
def soma(n1, n2, n3):
    print(n1+n2+n3)

soma(1,2,3)
print()


'''
3- Crie uma funcao que receba dois numeros. O primeiro eh um valor e o segundo eh um percentual.
Retorne(return) o valor do primeiro numero somado do aumento do percentual do mesmo.
'''
def aumento_percentual(valor, percentual):
    print(valor+(valor*percentual/100))

aumento_percentual(100, 10)


'''
4- Fizz Buzz - Se o parametro da funcao for divisivel por 3, retorne Fizz, e se o parametro
for divisivel por 5, retorne Buzz. Se o parametro for divisivel por 3 e 5, retorne FizzBuzz. 
Caso contrario, retorne o numero enviado.
'''
def fb(n):
    if n % 3 == 0:
        return "Fizz"
    elif n%5 == 0:
        return "Buzz"
    elif n%3 == 0 and n%5 == 0:
        return "FizzBuzz"
    else:
        return n

print(fb(15 ))    
