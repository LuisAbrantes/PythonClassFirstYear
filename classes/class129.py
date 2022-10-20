import pygame, sys


class Jogador():
    def __init__(self):
        self.jogadorImg = None
        self.jogadorX = None
        self.jogadorY = None
        self.alteraJogadorX = None 

    def apresentaJogador(self, screen, x, y):
        #Coloca uma imagem jogador  sobre a tela
        screen.blit(self.jogadorImg, (x, y))
        


class Jogo():

    def __init__(self):

        self.jogador = None

        #Inicia o game
        pygame.init()

        #Define a quantidade de frames por segundo e inicia o relógio
        self.FPS = 60 
        self.fpsClock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((800, 600))

        self.fundo = pygame.image.load('fundo.jpg')
    
    def inicializaJogador(self):
        self.jogador = Jogador()

        self.jogador.jogadorImg = pygame.image.load('jogador.png')
        self.jogador.jogadorX = 370 
        self.jogador.jogadorY = 480

    def executa(self):
        self.inicializaJogador()

        executando = True
        while executando == True:
            #RGB = Red, Green, Blue
            self.screen.fill((255, 255, 255))
            self.screen.blit(self.fundo, (0,0))

jogo = Jogo()
