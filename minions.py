import pygame as pg
from typing import Tuple
from config_jogo import *
import random

class Minions:

    pg.init()

    def __init__(self, vida: float, dano: float, velocidade: float,
    posicao: Tuple[float, float]):
        self.vida = vida
        self.dano = dano
        self.velocidade = velocidade
        self.posicao = posicao
        self.posicao_inicial = self.posicao
        self.colisao = False
    
    def movimento(self, inimigo):
        x, y = self.posicao
        x_inimigo = inimigo.posicao[0] + 41
        y_inimigo = inimigo.posicao[1] + 41

        vx = (x-x_inimigo)*(-1)
        vy = (y-y_inimigo)*(-1)

        d = ((vx**2)+(vy**2))**(1/2)

        vx /= d
        vy /= d

        vx *= self.velocidade
        vy *= self.velocidade

        novo_x = x
        novo_y = y

        novo_x += vx
        novo_y += vy

        if ((novo_y >= 0) and \
                ((novo_y + 20) <= ConfigJogo.ALTURA_TELA_PRINCIPAL)) and ((novo_x >= 0) \
                    and ((novo_x + 20) <= ConfigJogo.LARGURA_TELA_PRINCIPAL)): 
            self.posicao = (novo_x, novo_y)
    
    def desenha(self, tela, jogador, inimigo):
        x, y = self.posicao
        x_inimigo = inimigo.posicao[0] + 41
        y_inimigo = inimigo.posicao[1] + 41

        vx = (x-x_inimigo)*(-1)
        vy = (y-y_inimigo)*(-1)

        d = ((vx**2)+(vy**2))**(1/2)

        if d > 40:
            if jogador.direcao_inicial == 0:
                tela.blit(minionT, (self.posicao[0], self.posicao[1]))
            
            else:
                tela.blit(minionBR, (self.posicao[0], self.posicao[1]))

        elif d <= 40 and self.colisao == False:
            inimigo.vida -= jogador.dano*12
            if inimigo.direcao == 0:
                inimigo.sprite_atual = inimigo.sprite_dano
            if inimigo.direcao == 1:
                inimigo.sprite_atual = pg.transform.flip(inimigo.sprite_dano, True, False)
            self.posicao = self.posicao_inicial
            self.colisao = True
        
    def rodar(self,tela,jogador,inimigo):
        self.movimento(inimigo)
        self.desenha(tela, jogador, inimigo)


n1 = random.randint(0,50)
n2 = random.randint(0,95)
n3 = random.randint(0,110)

n4 = random.randint(0,70)
n5 = random.randint(0,115)
n6 = random.randint(0,120)

pos1 = [random.randint(0,100),random.randint(0,600)]
pos2 = [random.randint(0,70),random.randint(0,70)]
pos3 = [random.randint(0,150),random.randint(0,400)]


pos_minion1 = [pos1[0] + n1, pos1[1] + n1]
pos_minion2 = [pos2[0] + n2, pos2[1] + n2]
pos_minion3 = [pos3[0] + n3, pos3[1] + n3]

pos_minion4 = [pos1[0] + n4, pos1[1] + n4]
pos_minion5 = [pos2[0] + n5, pos2[1] + n5]
pos_minion6 = [pos3[0] + n6, pos3[1] + n6]


minion1 = Minions(50, 0.1, 0.8, pos_minion1)
minion2 = Minions(50, 0.1, 0.8, pos_minion2)
minion3 = Minions(50, 0.1, 0.8, pos_minion3)
minion4 = Minions(50, 0.1, 0.8, pos_minion4)
minion5 = Minions(50, 0.1, 0.8, pos_minion5)
minion6 = Minions(50, 0.1, 0.8, pos_minion6)