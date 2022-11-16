import pygame as pg
from cena_historia import CenaHistoria
from cena_inicial import CenaInicial
from cena_principal import CenaPrincipal
from cena_selecao1 import CenaSelection1
from cena_selecao2 import CenaSelection2
from config_jogo import ConfigJogo
from personagem_bat import Personagem_batalha
from persona import *

class Jogo_Toninha:
    def __init__(self):
        pg.init()
        '''pg.mixer.init()'''

        self.tela = pg.display.set_mode((
            ConfigJogo.LARGURA_TELA,
            ConfigJogo.ALTURA_TELA
        ))

        self.tela_PRINCIPAL = pg.display.set_mode((
            ConfigJogo.LARGURA_TELA_PRINCIPAL,
            ConfigJogo.ALTURA_TELA_PRINCIPAL
        ))

        pg.display.set_caption('Toninha Rampage')
        pg.display.set_icon(sprite_maga_ataque)

    def rodar(self):
        ConfigJogo.TELA = 1
        
        while True:
            if ConfigJogo.TELA == 1:
                self.tela = pg.display.set_mode((
            ConfigJogo.LARGURA_TELA,
            ConfigJogo.ALTURA_TELA
        ))
                cena = CenaInicial(self.tela)
                cena.rodar()
                
            if ConfigJogo.TELA == 2:
                self.tela = pg.display.set_mode((
            ConfigJogo.LARGURA_TELA,
            ConfigJogo.ALTURA_TELA
        ))
                cena = CenaHistoria(self.tela)
                cena.rodar()
            
            if ConfigJogo.TELA == 3:
                self.tela = pg.display.set_mode((
            ConfigJogo.LARGURA_TELA,
            ConfigJogo.ALTURA_TELA
        ))
                cena = CenaSelection1(self.tela)
                cena.rodar()
                id1 = cena.retorna_indice1()
        
            if ConfigJogo.TELA == 4:
                self.tela = pg.display.set_mode((
            ConfigJogo.LARGURA_TELA,
            ConfigJogo.ALTURA_TELA
        ))
                cena = CenaSelection2(self.tela)
                cena.rodar()
                id2 = cena.retorna_indice2()

            if ConfigJogo.TELA == 5:
                self.tela_PRINCIPAL = pg.display.set_mode((
                ConfigJogo.LARGURA_TELA_PRINCIPAL,
                ConfigJogo.ALTURA_TELA_PRINCIPAL))

                cena = CenaPrincipal(self.tela_PRINCIPAL, id1, id2)
                cena.rodar()