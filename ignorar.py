
import pygame as pg
from config_jogo import ConfigJogo
from cronometro import Cronometro

class EstadoJogo:
    def __init__(self):
        self.font = pg.font.SysFont(None, 48)
        self.cronometro = Cronometro()

    def desenha_vidas(self, tela, vida1, vida2):
        img = self.font.render(f'{vida1} x {vida2}',
                                True, ConfigJogo.COR_ESTADO)
        px = ConfigJogo.LARGURA_TELA_PRINCIPAL // 2 - img.get_size()[0] // 2
        py = ConfigJogo.ALTURA_PLACAR
        tela.blit(img, (px, py))
    
    def desenha_tempo(self, tela):
        tempo = ConfigJogo.DURACAO_PARTIDA - self.cronometro.tempo_passado()
        img = self.font.render(f'{tempo:.0f}',
                                True, ConfigJogo.COR_ESTADO)
        px = ConfigJogo.LARGURA_TELA_PRINCIPAL // 2 - img.get_size()[0] // 2
        py = ConfigJogo.ALTURA_TEMPO
        tela.blit(img, (px, py))