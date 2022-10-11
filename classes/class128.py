class Animal():

    def __init__(self):
        self.nome = None
        self.cor = None

    def cadastra(self):
        self.nome = input("Nome: ")
        self.cor = input("Cor: ")

    def apresenta(self):
        print(self.nome)
        print(self.cor)


class Gato(Animal):

    def interage(self):
        print("Meow!")


class Cachorro(Animal):

    def interage(self):
        print("Woof!")


gato = Gato()
cachorro = Cachorro()

gato.cadastra()
cachorro.cadastra()

gato.apresenta()
cachorro.apresenta()

gato.interage()
cachorro.interage()
