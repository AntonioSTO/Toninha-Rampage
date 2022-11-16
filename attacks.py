#====================================================
#               definição dos ataques
#====================================================

import pygame as pg
from cronometro import Cronometro
from config_jogo import *
from minions import *

class AtaqueFisico:
    def __init__(self):
        self.cronometro = Cronometro()
        
    def ataque_normal(self, tela, jogador, inimigo):
        pos1 = (jogador.posicao[0] + 41, jogador.posicao[1] + 41)
        pos2 = (inimigo.posicao[0] + 41, inimigo.posicao[1] + 41)
        d = (((pos1[0]-pos2[0])**2)+((pos1[1]-pos2[1])**2))**(1/2)

        if d <= 50:
            inimigo.vida = inimigo.vida - jogador.dano
            inimigo.velocidade = inimigo.velocidade_nominal
        
        # print(inimigo.vida)
    
        x = jogador.posicao[0]
        y = jogador.posicao[1]
        
        if jogador.direcao == 0:
            jogador.sprite_atual = jogador.sprite_ataque
        
        elif jogador.direcao == 1:
            jogador.sprite_atual = pg.transform.flip(jogador.sprite_ataque, True, False)
            
        if inimigo.direcao == 0:
            pass
        
        elif inimigo.direcao == 1:
            pass

        pg.draw.circle(tela,
            (255, 220, 220), 
            (jogador.posicao[0]+41, jogador.posicao[1]+41),
            50,
            5)
        
        pg.display.flip()
        

class Cura:
    def __init__(self):
        self.cronometro = Cronometro()
        
    def ataque_especial(self, tela, jogador, inimigo):
        
        x = jogador.posicao[0]
        y = jogador.posicao[1]
        
        if jogador.vida + jogador.dano <= 600:
            jogador.vida = jogador.vida + jogador.dano/5
        
        
        pg.draw.circle(tela,
            (188, 246, 160), 
            (jogador.posicao[0]+41, jogador.posicao[1]+41),
            50,
            5)
        
        jogador.sprite_atual = jogador.sprite_especial


class Stun:
    
    def ataque_especial(self, tela, jogador, inimigo):
        pos1 = [jogador.posicao[0] + 41, jogador.posicao[1] + 41]
        pos2 = [inimigo.posicao[0] + 41, inimigo.posicao[1] + 41]
        d = (((pos1[0]-pos2[0])**2)+((pos1[1]-pos2[1])**2))**(1/2)

        x = jogador.posicao[0]
        y = jogador.posicao[1]

        if d <= 50:
            inimigo.velocidade = inimigo.velocidade_stunned
        
            if jogador.direcao == 0:
                if inimigo.posicao[0] + 102 <= ConfigJogo.LARGURA_TELA_PRINCIPAL:
                    inimigo.posicao=(inimigo.posicao[0]+20, inimigo.posicao[1] )

            if jogador.direcao == 1:
                if inimigo.posicao[0] - 20 >= 0:
                    inimigo.posicao=(inimigo.posicao[0]-20, inimigo.posicao[1] )

        pg.draw.circle(tela,
        (238, 216, 106), 
        (jogador.posicao[0]+41, jogador.posicao[1]+41),
        50,
        5)

        if jogador.direcao == 0:
            jogador.sprite_atual = jogador.sprite_ataque
        
        elif jogador.direcao == 1:
            jogador.sprite_atual = pg.transform.flip(jogador.sprite_ataque, True, False)
            
        if inimigo.direcao == 0:
            pass
        
        elif inimigo.direcao == 1:
            pass
    
        pg.display.flip()
        

class AtaqueArea:

    def ataque_especial(self, tela, jogador, inimigo):
        pos1 = [jogador.posicao[0] + 41, jogador.posicao[1] + 41]
        pos2 = [inimigo.posicao[0] + 41, inimigo.posicao[1] + 41]

        contador = Cronometro()
        
        x = jogador.posicao[0]
        y = jogador.posicao[1]
        z = inimigo.posicao[0]
        w = inimigo.posicao[1]

        pg.event.get()  
        mouse_position = pg.mouse.get_pos()
        x_mouse = mouse_position[0]
        y_mouse= mouse_position[1]


        if (pos2[0] >= x_mouse - 100) and (pos2[0] <= x_mouse + 100):
            if (pos2[1] >= y_mouse - 100) and (pos2[1] <= y_mouse + 100):
                inimigo.vida -= jogador.dano

        
        pg.draw.circle(tela,
        (255, 100, 80), 
        (x_mouse, y_mouse),
        100)

        if jogador.direcao == 0:
            jogador.sprite_atual = jogador.sprite_ataque
        
        if jogador.direcao == 1:
            jogador.sprite_atual = pg.transform.flip(jogador.sprite_ataque, True, False)

        if inimigo.direcao == 1:
            tela.blit(inimigo.sprite_atual, (z,w))
        
        if inimigo.direcao == 0:
            tela.blit(inimigo.sprite_atual, (z,w))



class Invoca:

    def ataque_especial(self, tela, jogador, inimigo):
        pos1 = [jogador.posicao[0] + 41, jogador.posicao[1] + 41]
        pos2 = [inimigo.posicao[0] + 41, inimigo.posicao[1] + 41]

        minion1.rodar(tela,jogador, inimigo)
        minion2.rodar(tela,jogador, inimigo)
        minion3.rodar(tela,jogador, inimigo)
        

    
        
        
        
        
        
        
