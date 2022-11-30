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
            if inimigo.direcao == 0:
                inimigo.sprite_atual = inimigo.sprite_dano
        
            elif inimigo.direcao == 1:
                inimigo.sprite_atual = pg.transform.flip(inimigo.sprite_dano, True, False)
        
        # print(inimigo.vida)
    
        x = jogador.posicao[0]
        y = jogador.posicao[1]
        
        if jogador.direcao == 0:
            jogador.sprite_atual = jogador.sprite_ataque
        
        elif jogador.direcao == 1:
            jogador.sprite_atual = pg.transform.flip(jogador.sprite_ataque, True, False)
            

        pg.draw.circle(tela,
            (255, 220, 220), 
            (jogador.posicao[0]+41, jogador.posicao[1]+41),
            50,
            5)
        
        pg.display.flip()
        

    def reseta(self,jogador,inimigo):
        if jogador.direcao == 0 and jogador.sprite_atual == jogador.sprite_ataque:
            jogador.sprite_atual = jogador.sprite_direita
    
        elif jogador.direcao == 1 and jogador.sprite_atual == pg.transform.flip(jogador.sprite_ataque, True, False):
            jogador.sprite_atual = jogador.sprite_esquerda
        
        if inimigo.direcao == 0:
            inimigo.sprite_atual = inimigo.sprite_direita
        
        if inimigo.direcao == 1:
            inimigo.sprite_atual = inimigo.sprite_esquerda

    def tempo(self):
        if self.timer.tempo_passado() > 0.5:
            self.encerra = 1
            self.timer.reset()

class Cura:
    def __init__(self):
        self.timer = Cronometro()
        self.encerra = 0
        self.vida = 0
        
    def ataque_especial(self, tela, jogador, inimigo, mouse):
        
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

    def reseta(self,jogador,inimigo):
        if jogador.direcao == 0 and jogador.sprite_atual == jogador.sprite_especial:
            jogador.sprite_atual = jogador.sprite_direita
    
        elif jogador.direcao == 1 and jogador.sprite_atual == jogador.sprite_especial:
            jogador.sprite_atual = jogador.sprite_esquerda

    def tempo(self):
        if self.timer.tempo_passado() > 3:
            self.encerra = 1
            self.timer.reset()

class Stun:
    
    def __init__(self):
        self.timer = Cronometro()
        self.intervalo = Cronometro()
        self.encerra = 0

    def ataque_especial(self, tela, jogador, inimigo, mouse):
        pos1 = [jogador.posicao[0] + 41, jogador.posicao[1] + 41]
        pos2 = [inimigo.posicao[0] + 41, inimigo.posicao[1] + 41]
        d = (((pos1[0]-pos2[0])**2)+((pos1[1]-pos2[1])**2))**(1/2)

        x = jogador.posicao[0]
        y = jogador.posicao[1]


        if self.timer.tempo_passado() < 2.5:
            pg.draw.circle(tela,
        (238, 216, 106), 
        (jogador.posicao[0]+41, jogador.posicao[1]+41),
        10,
        5)

        if self.timer.tempo_passado() > 2.5 and self.timer.tempo_passado() < 2.75:
            pg.draw.circle(tela,
        (238, 216, 106), 
        (jogador.posicao[0]+41, jogador.posicao[1]+41),
        17.5,
        5)

        if self.timer.tempo_passado() > 2.75 and self.timer.tempo_passado() < 3:
            pg.draw.circle(tela,
        (238, 216, 106), 
        (jogador.posicao[0]+41, jogador.posicao[1]+41),
        25,
        5)

        if self.timer.tempo_passado() > 3 and self.timer.tempo_passado() < 3.25:
            pg.draw.circle(tela,
        (238, 216, 106), 
        (jogador.posicao[0]+41, jogador.posicao[1]+41),
        32.5,
        5)

        if self.timer.tempo_passado() > 3.25 and self.timer.tempo_passado() < 3.5:
            pg.draw.circle(tela,
        (238, 216, 106), 
        (jogador.posicao[0]+41, jogador.posicao[1]+41),
        40,
        5)

        if self.timer.tempo_passado() > 3.5 and self.timer.tempo_passado() < 4:
            pg.draw.circle(tela,
        (238, 216, 106), 
        (jogador.posicao[0]+41, jogador.posicao[1]+41),
        50,
        5)
            if d <= 50:
                inimigo.stun.reset()
            
                if jogador.direcao == 0:
                    if inimigo.posicao[0] + 102 <= ConfigJogo.LARGURA_TELA_PRINCIPAL:
                        inimigo.posicao=(inimigo.posicao[0]+20, inimigo.posicao[1] )

                if jogador.direcao == 1:
                    if inimigo.posicao[0] - 20 >= 0:
                        inimigo.posicao=(inimigo.posicao[0]-20, inimigo.posicao[1] )

            if jogador.direcao == 0:
                jogador.sprite_atual = jogador.sprite_ataque
            
            if jogador.direcao == 1:
                jogador.sprite_atual = pg.transform.flip(jogador.sprite_ataque, True, False)
        
        '''if inimigo.direcao == 0:
            pass
        
        if inimigo.direcao == 1:
            pass'''
    

    def reseta(self,jogador,inimigo):
        if jogador.direcao == 0 and jogador.sprite_atual == jogador.sprite_ataque:
            jogador.sprite_atual = jogador.sprite_direita
    
        elif jogador.direcao == 1 and jogador.sprite_atual == pg.transform.flip(jogador.sprite_ataque, True, False):
            jogador.sprite_atual = jogador.sprite_esquerda
        

    def tempo(self):
        if self.timer.tempo_passado() > 4:
            self.encerra = 1
            self.timer.reset()

        

class AtaqueArea:

    def __init__(self):
        self.timer = Cronometro()
        self.encerra = 0

    def ataque_especial(self, tela, jogador, inimigo, mouse):
        pos1 = [jogador.posicao[0] + 41, jogador.posicao[1] + 41]
        pos2 = [inimigo.posicao[0] + 41, inimigo.posicao[1] + 41]

        position = mouse
        
        z = inimigo.posicao[0]
        w = inimigo.posicao[1]

        x_mouse = position[0]
        y_mouse= position[1]
        

        if (pos2[0] >= x_mouse - 75) and (pos2[0] <= x_mouse + 75):
            if (pos2[1] >= y_mouse - 75) and (pos2[1] <= y_mouse + 75):
                inimigo.vida -= 0.1*jogador.dano
                if inimigo.direcao == 0:
                    inimigo.sprite_atual = inimigo.sprite_dano
        
                if inimigo.direcao == 1:
                    inimigo.sprite_atual = pg.transform.flip(inimigo.sprite_dano, True, False)

        
        pg.draw.circle(tela,
        (255, 100, 80), 
        (x_mouse, y_mouse),
        75)

        if jogador.direcao == 0:
            jogador.sprite_atual = jogador.sprite_ataque
        
        if jogador.direcao == 1:
            jogador.sprite_atual = pg.transform.flip(jogador.sprite_ataque, True, False)

        if inimigo.direcao == 1:
            tela.blit(inimigo.sprite_atual, (z,w))
        
        if inimigo.direcao == 0:
            tela.blit(inimigo.sprite_atual, (z,w))

    def reseta(self,jogador,inimigo):
        if jogador.direcao == 0:
            jogador.sprite_atual = jogador.sprite_direita
        
        if jogador.direcao == 1:
            jogador.sprite_atual = pg.transform.flip(jogador.sprite_direita, True, False)

        if inimigo.direcao == 1:
            inimigo.sprite_atual = inimigo.sprite_esquerda
        
        if inimigo.direcao == 0:
            inimigo.sprite_atual = pg.transform.flip(inimigo.sprite_esquerda, True, False)  
              
    def tempo(self):
        if self.timer.tempo_passado() > 4:
            self.encerra = 1
            self.timer.reset()




class Invoca:

    def __init__(self):
        self.timer = Cronometro()
        self.encerra = 0

    def ataque_especial(self, tela, jogador, inimigo, mouse):
        pos1 = [jogador.posicao[0] + 41, jogador.posicao[1] + 41]
        pos2 = [inimigo.posicao[0] + 41, inimigo.posicao[1] + 41]

        minion1.rodar(tela,jogador, inimigo)
        minion2.rodar(tela,jogador, inimigo)
        minion3.rodar(tela,jogador, inimigo)

    def reseta(self,jogador,inimigo):
        minion1.posicao = (pos1[0] + random.randint(0,100), pos1[1] + random.randint(0,100))
        minion2.posicao = (pos1[0] + random.randint(0,100), pos1[1] + random.randint(0,100))
        minion3.posicao = (pos1[0] + random.randint(0,100), pos1[1] + random.randint(0,100))
        if inimigo.direcao == 0:
            inimigo.sprite_atual = inimigo.sprite_direita
        
        if inimigo.direcao == 1:
            inimigo.sprite_atual = inimigo.sprite_esquerda
            
        minion1.colisao = False
        minion2.colisao = False
        minion3.colisao = False

    def tempo(self):
        if self.timer.tempo_passado() > 8 or (minion1.colisao == True and minion2.colisao == True and minion3.colisao == True):
            self.encerra = 1
            minion1.colisao = False
            minion2.colisao = False
            minion3.colisao = False
            self.timer.reset()



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
    posicao: Tuple[float, float], cor):
        self.velocidade = velocidade
        self.posicao = posicao
        self.posicao_inicial = posicao
        self.cor = cor
    
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

        dx = (x-x_inimigo)
        dy = (y-y_inimigo)

        d = ((dx**2)+(dy**2))**(1/2)

        if (d > 40) and ((x-10 > 0) \
                    and ((x + 20) < ConfigJogo.LARGURA_TELA_PRINCIPAL)):

            pg.draw.circle(tela,
                    self.cor,
                    (self.posicao[0], self.posicao[1]),
                    10)

        elif (d <= 40):
            inimigo.vida -= 6*jogador.dano
            if inimigo.direcao == 0:
                inimigo.sprite_atual = inimigo.sprite_dano
        
            if inimigo.direcao == 1:
                inimigo.sprite_atual = pg.transform.flip(inimigo.sprite_dano, True, False)
            
            self.posicao = self.posicao_inicial
        
    def rodar(self,tela,jogador,inimigo):
        self.movimento(jogador)
        self.desenha(tela, jogador, inimigo)


        
class AtaqueDistancia:

    def __init__(self):
        self.timer = Cronometro()
        self.intervalo = Cronometro()
        self.encerra = 0
        self.projeteis = []

    def ataque_normal(self, tela, jogador, inimigo):
        x = jogador.posicao[0] + 41
        y = jogador.posicao[1] + 41
        direcao = jogador.direcao

        if jogador.direcao_inicial == 0:
            
            jogador.sprite_atual = jogador.sprite_ataque


            if direcao == 0:
                new_projectile = Projectile(
                    5, (x,y), (255,0,0))

            elif direcao == 1:
                new_projectile = Projectile(
                    -5, (x,y), (255,0,0))

        if jogador.direcao_inicial == 1:
            
            jogador.sprite_atual = pg.transform.flip(jogador.sprite_ataque, True, False)

            if direcao == 0:
                new_projectile = Projectile(
                    5, (x,y), (0,0,0))

            elif direcao == 1:
                new_projectile = Projectile(
                    -5, (x,y), (0,0,0))


        if len(self.projeteis) <= 1:
            self.projeteis.append(new_projectile)

        for p in self.projeteis:
            p.rodar(tela, jogador, inimigo)


    
    def reseta(self,jogador,inimigo):
        self.projeteis = []
        '''for p in AtaqueDistancia.projeteis:
            p.posicao = p.posicao'''

        if inimigo.direcao == 0:
            inimigo.sprite_atual = inimigo.sprite_direita
        
        if inimigo.direcao == 1:
            inimigo.sprite_atual = inimigo.sprite_esquerda
            
    def tempo(self):
        if self.timer.tempo_passado() > 0.6:
            self.encerra = 1
            self.timer.reset()


    
class Teleport:

    def __init__(self):
        self.timer = Cronometro()
        self.encerra = 0

    def ataque_especial(self, tela, jogador, inimigo, mouse):

        position = mouse

        if (position[0] > 41 and position[0] < ConfigJogo.LARGURA_TELA_PRINCIPAL - 41) and (position[1] > 41 and position[1] < ConfigJogo.ALTURA_TELA_PRINCIPAL - 41):

            jogador.posicao = (position[0] - 41, position[1] - 41)

    def reseta(self,jogador,inimigo):
        pass
    
    def tempo(self):
        if self.timer.tempo_passado() > 2.1:
            self.encerra = 1
            self.timer.reset()
        
        
