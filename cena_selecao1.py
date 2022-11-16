import sys
import pygame as pg
from persona import *
from config_jogo import ConfigJogo

class CenaSelection1:
    def __init__(self, tela):
        self.tela = tela
        self.encerra = False
        self.rect_sel = (ConfigJogo.ALTURA_TELA//2) - 0.28*ConfigJogo.ALTURA_TELA
        self.lista1 = Lista1
        self.indice1 = 0
        
        font_titulo = pg.font.SysFont(None, ConfigJogo.FONTE_SUBTITULO)
        font_selections = pg.font.SysFont(None, ConfigJogo.FONTE_SUBTITULO)
        self.titulo = font_titulo.render(
            f'Player 1: Selecione seu lutador.', True, ConfigJogo.COR_TITULO)

        self.selection1 = font_selections.render(
            f'{self.lista1[0].nome}', True, ConfigJogo.COR_TEXTO)
        self.selection2 = font_selections.render(
            f'{self.lista1[1].nome}', True, ConfigJogo.COR_TEXTO)
        self.selection3 = font_selections.render(
            f'{self.lista1[2].nome}', True, ConfigJogo.COR_TEXTO)
        self.selection4 = font_selections.render(
            f'{self.lista1[3].nome}', True, ConfigJogo.COR_TEXTO)
        
    def tratamento_eventos(self):
        for event in pg.event.get():
            if (event.type == pg.QUIT):
                sys.exit()
                
            if (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                ConfigJogo.TELA -= 1
                self.encerra = True

            if (event.type == pg.KEYDOWN and event.key == pg.K_SPACE):
                ConfigJogo.TELA += 1
                self.encerra = True

            if pg.key.get_pressed()[pg.K_a]:
                if (event.type == pg.KEYDOWN and event.key == pg.K_m):
                    ConfigJogo.TELA += 1
                    self.indice1 = 4
                    ConfigJogo.amogus_sound.play()
                    self.encerra = True
                
            if (event.type == pg.KEYDOWN and event.key == pg.K_w):
                if self.rect_sel - 75 > (ConfigJogo.ALTURA_TELA//2) - 0.28*ConfigJogo.ALTURA_TELA:
                    self.rect_sel -= 75
                    self.indice1 -= 1            #para escolher o personagem na lista1
                    ConfigJogo.switch_sound.play()
            elif (event.type == pg.KEYDOWN and event.key == pg.K_s):
                if self.rect_sel < (ConfigJogo.ALTURA_TELA//2) - 0.28*ConfigJogo.ALTURA_TELA + 210:
                    self.rect_sel += 75
                    self.indice1 += 1            #para escolher o personagem na lista1
                    ConfigJogo.switch_sound.play()

            
    def retorna_indice1(self):  #função para retornar um valor para a variável id1 em jogo.py
        return self.indice1
    
    def rodar(self):
        while not self.encerra:
            self.tratamento_eventos()
            self.desenha()
            

    def desenha(self):
        x = (ConfigJogo.LARGURA_TELA//2) - 0.17*ConfigJogo.LARGURA_TELA
        y = (ConfigJogo.ALTURA_TELA//2) - 0.30*ConfigJogo.ALTURA_TELA
        l = 0.34*ConfigJogo.LARGURA_TELA
        a = 0.7*ConfigJogo.ALTURA_TELA
        self.tela.fill((69,69,69))
        self.desenha_titulo(self.tela)
        self.desenha_selection1(self.tela)
        self.desenha_selection2(self.tela)
        self.desenha_selection3(self.tela)
        self.desenha_selection4(self.tela)
        pg.draw.rect(
            self.tela,
            ConfigJogo.COR_CAIXA,
            (x,y,l,a),
            5
        )
        
        x_selectbox = (ConfigJogo.LARGURA_TELA//2) - 0.15*ConfigJogo.LARGURA_TELA
        y_selectbox = self.rect_sel
        l_selectbox = 0.3*ConfigJogo.LARGURA_TELA
        a_selectbox = 0.10*ConfigJogo.ALTURA_TELA
        
        pg.draw.rect(
            self.tela,
            (255,0,0),
            (x_selectbox,y_selectbox,l_selectbox,a_selectbox),
            4
        )
        
        x_img = (ConfigJogo.LARGURA_TELA//2) - 0.45*ConfigJogo.LARGURA_TELA
        y_img = (ConfigJogo.ALTURA_TELA//2) - 0.15*ConfigJogo.ALTURA_TELA
        
        for i in range(len(Lista1)):
            if self.indice1 == i:
                self.tela.blit(scale(Lista1[i].sprite_direita, (150,150)), (x_img,y_img))
        
        pg.display.flip()

    def desenha_titulo(self,tela):
        px = ConfigJogo.LARGURA_TELA // 2 - self.titulo.get_size()[0] // 2
        py = (0.15 * ConfigJogo.ALTURA_TELA // 2)
        tela.blit(self.titulo, (px, py))
        
    def desenha_selection1(self,tela):
        px = ConfigJogo.LARGURA_TELA // 2 - \
            self.selection1.get_size()[0] // 2
        py = (0.29 * ConfigJogo.ALTURA_TELA // 2) + \
            (self.titulo.get_size()[1] * 1.5)
        tela.blit(self.selection1, (px, py))
        
    def desenha_selection2(self,tela):
        px = ConfigJogo.LARGURA_TELA // 2 - \
            self.selection1.get_size()[0] // 2
        py = (0.29 * ConfigJogo.ALTURA_TELA // 2) + \
            (self.titulo.get_size()[1] * 4.5)
        tela.blit(self.selection2, (px, py))
    
    def desenha_selection3(self,tela):
        px = ConfigJogo.LARGURA_TELA // 2 - \
            self.selection1.get_size()[0] // 2
        py = (0.29 * ConfigJogo.ALTURA_TELA // 2) + \
            (self.titulo.get_size()[1] * 7.5)
        tela.blit(self.selection3, (px, py))
    
    def desenha_selection4(self,tela):
        px = ConfigJogo.LARGURA_TELA // 2 - \
            self.selection1.get_size()[0] // 2
        py = (0.29 * ConfigJogo.ALTURA_TELA // 2) + \
            (self.titulo.get_size()[1] * 10.5)
        tela.blit(self.selection4, (px, py))
