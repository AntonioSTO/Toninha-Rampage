from typing import Tuple
import pygame as pg
from cronometro import Cronometro
from config_jogo import ConfigJogo


class Personagem_batalha:

    pg.init()

    def __init__(self, nome: str, vida: float, dano: float,
    velocidade: float, posicao: Tuple[float, float], direcao: int, sprite_direita: any, sprite_esquerda: any, sprite_ataque: any,
    sprite_especial: any, sprite_dano: any, sprite_agua: any, sprite_death: any, classe1, classe2):
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
        self.sprite_dano = sprite_dano
        self.sprite_agua = sprite_agua
        self.sprite_death = sprite_death
        self.posicao_centro = (posicao[0] + 41, posicao[1] + 41)
        self.direcao = direcao
        self.direcao_inicial = direcao
        self.ataque_fisico_bool = False
        self.ataque_distancia_bool = False
        self.classe1 = classe1
        self.classe2 = classe2
        
        self.rect = pg.Rect(self.posicao[0], self.posicao[1], 60, 82)

        self.tempo1 = Cronometro()
        self.tempo2 = Cronometro()
        self.stun = Cronometro()
        self.tempo_area = Cronometro()

        if self.direcao == 0:
            self.sprite_inicial = self.sprite_direita

        elif self.direcao == 1:
            self.sprite_inicial = self.sprite_esquerda

        self.sprite_atual = self.sprite_inicial

    def mover_para_cima(self):
        if self.stun.tempo_passado() > 2:
            self.velocidade_y = -self.velocidade
            

    def mover_para_baixo(self):
        if self.stun.tempo_passado() > 2:
            self.velocidade_y = self.velocidade
            

    def mover_para_direita(self):
        if self.stun.tempo_passado() > 2:
            self.velocidade_x = self.velocidade
            self.sprite_atual = self.sprite_direita
            self.direcao = 0

    def mover_para_esquerda(self):
        if self.stun.tempo_passado() > 2:
            self.velocidade_x = -self.velocidade
            self.sprite_atual = self.sprite_esquerda
            self.direcao = 1

    def parar_x(self):
        self.velocidade_x = 0

    def parar_y(self):
        self.velocidade_y = 0

    def atualizar_posicao(self):
        x, y = self.posicao
        self.slow()
        novo_x = x + self.velocidade_x
        novo_y = y + self.velocidade_y
        self.rect = pg.Rect(novo_x, novo_y, 60, 82)

        #Limitação das bordas (blocos inquebráveis)

        if ((novo_y >= 32) and \
                ((novo_y + 82) <= ConfigJogo.ALTURA_TELA_PRINCIPAL - 32)) and ((novo_x >= 32) \
                    and ((novo_x + 82) <= ConfigJogo.LARGURA_TELA_PRINCIPAL - 32)):

            #Limitação da colisão com o bloco quebrável

            if ConfigJogo.B_BLOCK_VIDA1 > 0:
                if not self.rect.colliderect(ConfigJogo.B_BLOCK1):
                    self.posicao = (novo_x, novo_y)
            else:
                self.posicao = (novo_x, novo_y)

    def slow(self):         #atualização da velocidade e da sprite na água
        x, y = self.posicao

        if y < ConfigJogo.ALTURA_TELA_PRINCIPAL//2:
            if x > 384 and x < 544:
                self.velocidade= 0.5*self.velocidade_nominal
                if self.direcao == 0:
                    self.sprite_atual = self.sprite_agua
        
                if self.direcao == 1:
                    self.sprite_atual = pg.transform.flip(self.sprite_agua, True, False)
            
            else:
                self.velocidade = self.velocidade_nominal

        elif y >= ConfigJogo.ALTURA_TELA_PRINCIPAL//2:
            if x > 416 and x < 576:
                self.velocidade= 0.5*self.velocidade_nominal
                if self.direcao == 0:
                    self.sprite_atual = self.sprite_agua
        
                if self.direcao == 1:
                    self.sprite_atual = pg.transform.flip(self.sprite_agua, True, False)

            else:
                self.velocidade = self.velocidade_nominal

    def rect(self) -> Tuple[float, float, float, float]:
        """ retorna os dados da P como os retangulos sao representados 
            no pygame, i.e., como uma tupla do tipo (px, py, largura, altura).
        """
        return self.posicao + (ConfigJogo.LARGURA_P, ConfigJogo.ALTURA_P)

    def desenha(self, tela):
        x = self.posicao[0]
        y = self.posicao[1]
        
        # pg.draw.rect(tela, (0,0,0), self.rect, 3)

        tela.blit(self.sprite_atual, (x,y))

        if self.stun.tempo_passado() < 2:
            tela.blit(ConfigJogo.stunned, (self.posicao[0], self.posicao[1] - 30))
        
        if self.tempo_area.tempo_passado() < 2:
            pass