#Introdução de POO.

class Pokemon:
    def __init__(self):
        self.nome = ""
        self.tipo = ""
        self.hp = -1
        self.habilidades = []

    def usaHabilidade(self, posicao):
        print(f"{self.nome} usou {self.habilidades[posicao]}")

    def atribuiHabilidades(self, habilidade):
        self.habilidades.append(habilidade)

    def atribuiNome(self, n):
        self.nome = n

    def apresentaNome(self):
        print(self.nome)

    def obtemNome(self):
        return self.nome

    def atribuiTipo(self, tipo):
        self.tipo = tipo

pokemon1 = Pokemon()
pokemon1.atribuiNome("Pikachu")
pokemon1.apresentaNome()    
pokemon1.atribuiHabilidades("Choque do trovão")
pokemon1.usaHabilidade(0)
print(pokemon1)


pokemon2 = Pokemon()
pokemon2.atribuiNome("Charmander")
pokemon2.apresentaNome()
pokemon2.atribuiHabilidades("Brasa")
pokemon2.usaHabilidade(0)
print(pokemon2)