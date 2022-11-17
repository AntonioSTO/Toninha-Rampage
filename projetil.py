'''import pygame as pg
from typing import Tuple
from config_jogo import ConfigJogo
import random

class Projectile:

    pg.init()

    def __init__(self, velocidade: float,
    posicao: Tuple[float, float]):
        self.velocidade = velocidade
        self.posicao = posicao
        self.posicao_inicial = posicao
        self.existencia = True
    
    def movimento(self, jogador):
        x, y = self.posicao
        x_jogador = jogador.posicao[0] + 41
        y_jogador = jogador.posicao[1] + 41

        if jogador.direcao == 0:
            vx = self.velocidade

        elif jogador.direcao == 1:
            vx = -self.velocidade

        novo_x = x
        novo_x += vx


        if ((novo_x >= 0) \
                    and ((novo_x + 20) <= ConfigJogo.LARGURA_TELA_PRINCIPAL)): 
            self.posicao = (novo_x, y)

    
    def desenha(self, tela, jogador, inimigo):
        x, y = self.posicao
        x_inimigo = inimigo.posicao[0] + 41
        y_inimigo = inimigo.posicao[1] + 41

        vx = (x-x_inimigo)
        vy = (y-y_inimigo)

        d = ((vx**2)+(vy**2))**(1/2)

        if d > 40:
            pg.draw.circle(tela,
                    (0,0,0),
                    (self.posicao[0], self.posicao[1]),
                    10)

        else:
            inimigo.vida -= jogador.dano
            self.posicao = self.posicao_inicial
        
    def rodar(self,tela,jogador,inimigo):
        self.movimento(inimigo)
        self.desenha(tela, jogador, inimigo)
'''


