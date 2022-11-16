import sys
import pygame as pg
from persona import scale
from persona import img

from config_jogo import ConfigJogo

class CenaInicial:
    def __init__(self, tela):
        self.tela = tela
        self.encerra = False
        
        font_titulo = pg.font.SysFont(None, ConfigJogo.FONTE_TITULO)
        font_subtitulo = pg.font.SysFont(None, ConfigJogo.FONTE_SUBTITULO)
        self.titulo = font_titulo.render(
            f'TONINHA RAMPAGE!', True, ConfigJogo.COR_TITULO)
        self.integrantes = font_subtitulo.render(
            f'Antônio Sant Ana e Arthur Bandeira', True, ConfigJogo.COR_TEXTO)
        self.subtitulo = font_subtitulo.render(
            f'Pressione Espaço para Iniciar', True, ConfigJogo.COR_TEXTO)
        
        self.fundo = None 
    
    def tratamento_eventos(self):

        for event in pg.event.get():
            if (event.type == pg.QUIT) or \
                (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                sys.exit()

            if (event.type == pg.KEYDOWN and event.key == pg.K_SPACE):
                ConfigJogo.TELA += 1
                self.encerra = True
    
    def rodar(self):
        while not self.encerra:
            self.tratamento_eventos()
            self.desenha()
            

    def desenha(self):
        self.fundo = scale(img(r'./sprites/fundo_inicial.png'), (ConfigJogo.LARGURA_TELA,ConfigJogo.ALTURA_TELA ))
        self.tela.blit(self.fundo,(0,0))
        self.desenha_titulo(self.tela)
        self.desenha_subtitulo(self.tela)
        self.desenha_integrantes(self.tela)
        pg.display.flip()

    def desenha_titulo(self, tela):
        px = ConfigJogo.LARGURA_TELA // 2 - self.titulo.get_size()[0] // 2
        py = (0.2 * ConfigJogo.ALTURA_TELA // 2)
        tela.blit(self.titulo, (px, py))
        
    def desenha_integrantes(self,tela):
        px = ConfigJogo.LARGURA_TELA // 2 - self.integrantes.get_size()[0] // 2
        py = (0.2 * ConfigJogo.ALTURA_TELA // 2) + (0.15 * ConfigJogo.ALTURA_TELA)
        tela.blit(self.integrantes, (px,py))

    def desenha_subtitulo(self, tela):
        px = ConfigJogo.LARGURA_TELA // 2 - \
            self.subtitulo.get_size()[0] // 2
        py = (0.2 * ConfigJogo.ALTURA_TELA // 2) + \
            (self.titulo.get_size()[1] * 5.5)
        tela.blit(self.subtitulo, (px, py))
        