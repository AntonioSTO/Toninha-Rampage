from typing import Tuple
import pygame as pg
from config_jogo import ConfigJogo


class Personagem_batalha:

    pg.init()

    def __init__(self, nome: str, vida: float, dano: float,
    velocidade: float, posicao: Tuple[float, float], direcao: int, sprite_direita: any, sprite_esquerda: any, sprite_ataque: any,
    sprite_especial: any, classe1, classe2):
        self.nome = nome
        self.vida = vida
        self.dano = dano

        self.velocidade = velocidade
        self.velocidade_nominal = velocidade
        self.velocidade_stunned = 0

        self.posicao = posicao
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.sprite_direita = sprite_direita
        self.sprite_esquerda = sprite_esquerda
        self.sprite_ataque = sprite_ataque
        self.sprite_especial = sprite_especial
        '''self.sprite_dano = sprite_dano'''
        self.posicao_centro = (posicao[0] + 41, posicao[1] + 41)
        self.direcao = direcao
        self.ataque_fisico_bool = False
        self.ataque_distancia_bool = False
        self.classe1 = classe1
        self.classe2 = classe2

        if self.direcao == 0:
            self.sprite_inicial = self.sprite_direita

        elif self.direcao == 1:
            self.sprite_inicial = self.sprite_esquerda

        self.sprite_atual = self.sprite_inicial

    def mover_para_cima(self):
        self.velocidade_y = -self.velocidade

    def mover_para_baixo(self):
        self.velocidade_y = self.velocidade

    def mover_para_direita(self):
        self.velocidade_x = self.velocidade
        self.sprite_atual = self.sprite_direita
        self.direcao = 0

    def mover_para_esquerda(self):
        self.velocidade_x = -self.velocidade
        self.sprite_atual = self.sprite_esquerda
        self.direcao = 1

    def parar_x(self):
        self.velocidade_x = 0
    def parar_y(self):
        self.velocidade_y = 0

    def atualizar_posicao(self):
        x, y = self.posicao
        novo_x = x + self.velocidade_x
        novo_y = y + self.velocidade_y

        if ((novo_y >= 0) and \
                ((novo_y + 82) <= ConfigJogo.ALTURA_TELA_PRINCIPAL)) and ((novo_x >= 0) \
                    and ((novo_x + 82) <= ConfigJogo.LARGURA_TELA_PRINCIPAL)): 
            self.posicao = (novo_x, novo_y)

    def rect(self) -> Tuple[float, float, float, float]:
        """ retorna os dados da P como os retangulos sao representados 
            no pygame, i.e., como uma tupla do tipo (px, py, largura, altura).
        """
        return self.posicao + (ConfigJogo.LARGURA_P, ConfigJogo.ALTURA_P)

    def desenha(self, tela):
        x = self.posicao[0]
        y = self.posicao[1]

        tela.blit(self.sprite_atual, (x,y))


        '''if self.direcao == 0:
            if self.ataque_fisico_bool:
                pg.draw.circle(tela,
                        (255, 220, 220), 
                        (self.posicao[0]+41, self.posicao[1]+41),
                        50)
                tela.blit(self.sprite_ataque, (x,y))
            
            elif self.ataque_distancia_bool:
                tela.blit(self.sprite_ataque, (x,y))

            else:
                tela.blit(self.sprite_direita, (x,y))

        if self.direcao == 1:
            if self.ataque_fisico_bool:
                pg.draw.circle(tela,
                        (255, 220, 220), 
                        (self.posicao[0]+41, self.posicao[1]+41),
                        50)
                tela.blit(pg.transform.flip(self.sprite_ataque, True, False), (x,y))

            elif self.ataque_distancia_bool:
                tela.blit(pg.transform.flip(self.sprite_ataque, True, False), (x,y))

            else:
                tela.blit(self.sprite_esquerda, (x,y))'''

    
    '''def ataque(self):
        if self.nome == 'Toninha Maga' or self.nome == "Soldado Atirador":
            self.ataque_distancia_bool = True
        else:
            self.ataque_fisico_bool = True'''

    '''def parar_ataque(self):
        self.ataque_fisico_bool = False
        self.ataque_distancia_bool = False'''

    '''def ataque_fisico(self, inimigo):
        pos1 = (self.posicao[0] + 41, self.posicao[1] + 41)
        pos2 = (inimigo.posicao[0] + 41, inimigo.posicao[1] + 41)
        d = (((pos1[0]-pos2[0])**2)+((pos1[1]-pos2[1])**2))**(1/2)

        if (self.nome != 'Toninha Maga' and self.nome != "Soldado Atirador") and d <= 50:
            inimigo.vida = inimigo.vida - self.dano
        
        print(inimigo.vida)

    def cura(self):
        if (self.nome == 'Toninha Monge' or self.nome == 'Soldado Medico'):
            self.vida += self.dano'''
            
