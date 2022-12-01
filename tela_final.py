import sys
import pygame as pg
from persona import scale
from persona import img
from cena_principal import *
from persona import *

from config_jogo import ConfigJogo

class CenaFinal:
    def __init__(self, tela):
        self.tela = tela
        self.encerra = False
        
        font_titulo = pg.font.SysFont(None, ConfigJogo.FONTE_TITULO)
        font_subtitulo = pg.font.SysFont(None, ConfigJogo.FONTE_SUBTITULO)

        if  ConfigJogo.VITORIOSO < 3:
            self.titulo = font_titulo.render(
                f'Player {ConfigJogo.VITORIOSO} ganhou!', True, ConfigJogo.COR_TITULO)

        else:
            self.titulo = font_titulo.render(
                f'Empate!', True, ConfigJogo.COR_TITULO)

        self.texto = font_subtitulo.render(
            f'Pressione ESC para sair.', True, ConfigJogo.COR_TEXTO)
        
    
    def tratamento_eventos(self):

        for event in pg.event.get():
            if (event.type == pg.QUIT) or \
                (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                sys.exit()

    
    def rodar(self):
        while not self.encerra:
            self.tratamento_eventos()
            self.desenha()
            

    def desenha(self):
        x = ConfigJogo.LARGURA_TELA_PRINCIPAL // 2 - 100
        y = ConfigJogo.ALTURA_TELA_PRINCIPAL // 2 + 50

        self.tela.fill((255,255,255))
        self.desenha_titulo(self.tela)
        self.desenha_texto(self.tela)
        if ConfigJogo.VITORIOSO == 1:
            self.tela.blit(scale(ConfigJogo.SPRITE_VITORIOSO1, (200,200)), (x-100,y))
            self.tela.blit(scale(ConfigJogo.SPRITE_VITORIOSO2, (200,200)), (x+100,y))
        elif ConfigJogo.VITORIOSO == 2:
            self.tela.blit(scale(ConfigJogo.SPRITE_VITORIOSO1, (200,200)), (x-100,y))
            self.tela.blit(scale(ConfigJogo.SPRITE_VITORIOSO2, (200,200)), (x+100,y))
        else:
            self.tela.blit(scale(ConfigJogo.SPRITE_VITORIOSO1, (200,200)), (x-100,y))
            self.tela.blit(scale(ConfigJogo.SPRITE_VITORIOSO2, (200,200)), (x+100,y))
        pg.display.flip()

    def desenha_titulo(self, tela):
        px = ConfigJogo.LARGURA_TELA_PRINCIPAL // 2 - self.titulo.get_size()[0] // 2
        py = (0.2 * ConfigJogo.ALTURA_TELA // 2)
        tela.blit(self.titulo, (px, py))
        
    def desenha_texto(self, tela):
        px = ConfigJogo.LARGURA_TELA_PRINCIPAL // 2 - \
            self.texto.get_size()[0] // 2
        py = (0.2 * ConfigJogo.ALTURA_TELA // 2) + \
            (self.texto.get_size()[1] * 6.5)
        tela.blit(self.texto, (px, py))