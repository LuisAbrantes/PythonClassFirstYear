'''
Faça um programa que cadastra dados de diversos 
alunos. Cada aluno tem:
* nome
* idade
* cursos
* média global

O programa deve ser capaz de cadastrar os dados
de cada aluno cadastrado e de listar os nomes
dos alunos cadastrados
'''

class Studant():
    def __init__(self):
        self.name = None 
        self.age = None 
        self.gpa = None
        self.courses = None

    def registerData(self):
        self.name = input("Name: ")
        self.age = int(input("Age: "))
        self.gpa = input("GPA: ")

        amount = int(input("\nHow many courses? "))
        counter = 1
        self.courses = []
        while not counter > amount:
            course = input(f"Course{counter}: ")
            self.courses.append(course)
            counter += 1
    
    def listData(self):
        print(f"\nName: {self.name}")
        print(f"Age: {self.age}")
        print(f"GPA: {self.gpa}")
        print(f"Courses:{self.courses}")

studant1 = Studant()
studant1.registerData()
studant1.listData()