'''
4. Faça um programa que tem uma função que armazena o cadastro de 
estudantes de um curso em arquivo. 
Cada estudante tem: nome, endereço, idade e telefone. 

O programa deve ter também uma função que leia cada cadastro e armazene-o 
em uma lista de dicionários.
'''
import json
chave = "Aluno"
valor = "Informações"

def salvar(data):
    arquivo = open("json11.txt", "w") # write
    json.dump(data, arquivo)
    arquivo.close()

def carregar():
    try:  
        arquivo = open("json11.txt", "r")
    except OSError: 
        return []
    jsonText = arquivo.read()
    arquivo.close()
    return json.loads(jsonText)

def menu():
    print("\nBEM-VINDO AO MENU! INSIRA UMA DAS OPÇÕES:")
    print("1. Inserir um novo aluno;\n2. Apresentar os alunos; e \n3. Sair.")
    return int(input("--> "))



notas = carregar()
opt = 0

while opt!=3:
    opt = menu()

    if opt==1:
        nota = {}
        nota[chave] = str(input("\nInsira o nome do aluno: "))
        nota[valor] = str(input("Insira o endereço, idade e telefone. Todos separados por vírgula: "))
        notas.append(nota)
        salvar(notas)
    
    if opt==2: 
        contador = 1
        for nota in notas:
            print(f"~~~ NOTA {contador} ~~~")
            print(f"{chave} = {nota[chave]}")
            print(f"{valor} = {nota[valor]}")
            contador += 1

    else:
        print("Opção inválida!")