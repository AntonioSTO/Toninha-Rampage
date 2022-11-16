import sys
import pygame as pg
from cena_inicial import CenaInicial

from config_jogo import ConfigJogo

class CenaHistoria:
    def __init__(self, tela):
        self.tela = tela
        self.encerra = False
        
        font_subtitulo = pg.font.SysFont(None, ConfigJogo.FONTE_SUBTITULO)
        font_historia = pg.font.SysFont(None, ConfigJogo.FONTE_HISTORIA)
        self.titulo = font_subtitulo.render(
            f'A GUERRA:', True, ConfigJogo.COR_TITULO)
        self.historia1 = font_historia.render(
            f'Em um mundo paralelo, pós primeira guerra, as toninhas se rebelaram,', True, ConfigJogo.COR_TEXTO)
        self.historia2 = font_historia.render(
            f'e agora buscam vingança pelo massacre feito pelo exército brasileiro.', True, ConfigJogo.COR_TEXTO)
        self.historia3 = font_historia.render(
            f'Elas tem poderes e carisma, eles tem armamento e força bruta.', True, ConfigJogo.COR_TEXTO)
        self.historia4 = font_subtitulo.render(
            f'QUEM VENCERÁ?!', True, ConfigJogo.COR_TITULO)
        
        
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
                
    def rodar(self):
        while not self.encerra:
            self.tratamento_eventos()
            self.desenha()

    def desenha(self):
        self.tela.fill((255, 255, 255))
        self.desenha_titulo(self.tela)
        self.desenha_historia1(self.tela)
        self.desenha_historia2(self.tela)
        self.desenha_historia3(self.tela)
        self.desenha_historia4(self.tela)
        pg.display.flip()

    def desenha_titulo(self, tela):
        px = ConfigJogo.LARGURA_TELA // 2 - self.titulo.get_size()[0] // 2
        py = (0.2 * ConfigJogo.ALTURA_TELA // 2)
        tela.blit(self.titulo, (px, py))

    def desenha_historia1(self, tela):
        px = ConfigJogo.LARGURA_TELA // 2 - \
            self.historia1.get_size()[0] // 2
        py = (0.2 * ConfigJogo.ALTURA_TELA // 2) + \
            (self.titulo.get_size()[1] * 2.5)
        tela.blit(self.historia1, (px, py))
        
    def desenha_historia2(self, tela):
        px = ConfigJogo.LARGURA_TELA // 2 - \
            self.historia1.get_size()[0] // 2
        py = (0.2 * ConfigJogo.ALTURA_TELA // 2) + \
            (self.titulo.get_size()[1] * 4.0)
        tela.blit(self.historia2, (px, py))
        
    def desenha_historia3(self, tela):
        px = ConfigJogo.LARGURA_TELA // 2 - \
            self.historia1.get_size()[0] // 2
        py = (0.2 * ConfigJogo.ALTURA_TELA // 2) + \
            (self.titulo.get_size()[1] * 5.5)
        tela.blit(self.historia3, (px, py))
        
    def desenha_historia4(self, tela):
        px = ConfigJogo.LARGURA_TELA // 2 - \
            self.historia4.get_size()[0] // 2
        py = (0.2 * ConfigJogo.ALTURA_TELA // 2) + \
            (self.titulo.get_size()[1] * 8.0)
        tela.blit(self.historia4, (px, py))
        
        
    
        
        