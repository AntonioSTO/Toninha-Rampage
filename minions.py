import pygame as pg
from typing import Tuple
from config_jogo import ConfigJogo

class Minions:

    pg.init()

    def __init__(self, vida: float, dano: float, velocidade: float,
    posicao: Tuple[float, float]):
        self.vida = vida
        self.dano = dano
        self.velocidade = velocidade
        self.posicao = posicao
        self.existencia = True
    
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
            pg.draw.circle(tela,
                    (0,0,0),
                    (self.posicao[0], self.posicao[1]),
                    10)

        else:
            inimigo.vida -= jogador.dano
        
    def rodar(self,tela,jogador,inimigo):
        self.movimento(inimigo)
        self.desenha(tela, jogador, inimigo)



minion1 = Minions(50, 0.1, 0.5, (100,100))
minion2 = Minions(50, 0.1, 0.5, (0,0))
minion3 = Minions(50, 0.1, 0.5, (0,0))
minion4 = Minions(50, 0.1, 0.5, (0,0))
minion5 = Minions(50, 0.1, 0.5, (0,0))
        