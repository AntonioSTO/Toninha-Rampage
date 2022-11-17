#====================================================
#               definição dos ataques
#====================================================

import pygame as pg
from cronometro import Cronometro
from config_jogo import *
from minions import *

class AtaqueFisico:
    def __init__(self):
        self.timer = Cronometro()
        self.encerra = 0
        
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
        self.timer = Cronometro()
        self.encerra = 0
        
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
    
    def __init__(self):
        self.timer = Cronometro()
        self.encerra = 0

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

    def __init__(self):
        self.timer = Cronometro()
        self.encerra = 0

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

    def __init__(self):
        self.timer = Cronometro()
        self.encerra = 0

    def ataque_especial(self, tela, jogador, inimigo):
        pos1 = [jogador.posicao[0] + 41, jogador.posicao[1] + 41]
        pos2 = [inimigo.posicao[0] + 41, inimigo.posicao[1] + 41]

        minion1.rodar(tela,jogador, inimigo)
        minion2.rodar(tela,jogador, inimigo)
        minion3.rodar(tela,jogador, inimigo)


'''class Projectile:
    def __init__(self, p0_x, p0_y):
        self.px = p0_x
        self.py = p0_y
        self.v_x = 1
        self.raio = 10
        self.color = (0,0,0)

    def draw(self, screen):
        pg.draw.circle(screen, self.color, (self.px, self.py), self.raio)

    def update(self):
        self.px += self.v_x
        if self.px < 0:
            self.px = 0

        limit_x = (ConfigJogo.LARGURA_TELA_PRINCIPAL - self.r)
        if self.px > limit_x:
            self.px = limit_x

    def perform_shot(jogador, projectiles):
        (x, y) = jogador.posicao
        direcao = jogador.direcao
        new_projectile = Projectile(
            x, y, (0,0,0), 10)
        projectiles.append(new_projectile)

    def rodar(self, tela, jogador, projectiles):
        self.perform_shot(jogador, projectiles)
        self.draw(tela)
        self.update()'''

class Projectile:

    def __init__(self, velocidade: float,
    posicao: Tuple[float, float]):
        self.velocidade = velocidade
        self.posicao = posicao
        self.posicao_inicial = posicao
    
    def movimento(self, jogador):
        x, y = self.posicao
    
        vx = self.velocidade

        novo_x = x
        novo_x += vx


        
        self.posicao = (novo_x, y)

    
    def desenha(self, tela, jogador, inimigo):
        x, y = self.posicao
        x_inimigo = inimigo.posicao[0] + 41
        y_inimigo = inimigo.posicao[1] + 41

        vx = (x-x_inimigo)
        vy = (y-y_inimigo)

        d = ((vx**2)+(vy**2))**(1/2)

        if (d > 40) and ((x-10 > 0) \
                    and ((x + 20) < ConfigJogo.LARGURA_TELA_PRINCIPAL)):

            pg.draw.circle(tela,
                    (0,0,0),
                    (self.posicao[0], self.posicao[1]),
                    10)

        elif (d <= 40):
            inimigo.vida -= jogador.dano
            self.posicao = self.posicao_inicial
        
    def rodar(self,tela,jogador,inimigo):
        self.movimento(jogador)
        self.desenha(tela, jogador, inimigo)


        
class AtaqueDistancia:

    projeteis = []

    def __init__(self):
        self.timer = Cronometro()
        self.encerra = 0

    def ataque_normal(self, tela, jogador, inimigo):
        x = jogador.posicao[0] + 41
        y = jogador.posicao[1] + 41
        direcao = jogador.direcao
        if direcao == 0:
            new_projectile = Projectile(
                10, (x,y))

        elif direcao == 1:
            new_projectile = Projectile(
                -10, (x,y))

        AtaqueDistancia.projeteis.append(new_projectile)

        for p in AtaqueDistancia.projeteis:
            p.rodar(tela, jogador, inimigo)
    
    def reseta(self):
        AtaqueDistancia.projeteis = []
        '''for p in AtaqueDistancia.projeteis:
            p.posicao = p.posicao'''

    def tempo(self):
        if self.timer.tempo_passado() > 0.3:
            self.encerra = 1
            self.timer.reset()


    
        
        
        
        
        
        
