import pygame as pg
from pygame import font

pg.font.init()

class ConfigJogo:
    ALTURA_TELA = 400
    LARGURA_TELA = 700
    ALTURA_TELA_PRINCIPAL = 640
    LARGURA_TELA_PRINCIPAL = 1024
    COR_TITULO = (255, 0, 0)
    COR_TEXTO = (0, 0, 0)
    COR_CAIXA = (0, 0, 0)
    COR_SELECTION = (255, 0, 0)
    COR_ESTADO = (0, 0, 255)
    FONTE_TITULO = 72
    FONTE_SUBTITULO = 36
    FONTE_HISTORIA = 24
    FONTE_DESCRICAO = 12
    TELA = 0
    VELOCIDADE_P = 1
    ALTURA_P = (0.11 * ALTURA_TELA_PRINCIPAL)
    LARGURA_P = (0.05 * LARGURA_TELA_PRINCIPAL)
    ALTURA_PLACAR = 0.9 * ALTURA_TELA_PRINCIPAL
    ALTURA_TEMPO = 0.1 * ALTURA_TELA_PRINCIPAL
    POS_X1 = (0.05 * LARGURA_TELA_PRINCIPAL)
    POS_X2 = (0.95 * LARGURA_TELA_PRINCIPAL - LARGURA_P)
    DURACAO_PARTIDA = 120
    VITORIOSO = 0
    SPRITE_VITORIOSO1 = None
    SPRITE_VITORIOSO1 = None
    
    B_BLOCK_COR1 = (0,0,0)
    B_BLOCK_COR2 = (51,25,0)
    B_BLOCK_COR3 = (102,0,0)
    
    B_BLOCK1 = pg.Rect(160, 416, 64, 64)
    B_BLOCK_VIDA1 = 150

    font_stun = pg.font.SysFont(None, FONTE_HISTORIA)
    stunned = font_stun.render(
            f'Stunned!', True, COR_TEXTO)

    ##########################################################
    ################# CONFIG DE AUDIOS #######################
    ##########################################################                              

    pg.mixer.init()
    amogus_sound = pg.mixer.Sound(r'./sound/amogus.wav')
    pg.mixer.Sound.set_volume(amogus_sound, .1)

    switch_sound = pg.mixer.Sound(r'./sound/menu_sound.wav')
    pg.mixer.Sound.set_volume(switch_sound, .1)

def img(diretorio):
    return pg.image.load(diretorio)

def scale(imagem, resolucao):
    return pg.transform.scale(imagem, resolucao)

minionT = scale(img(r'./sprites/minion.png'), (32, 32))
minionBR = scale(img(r'./sprites/minion2.png'), (20, 20))
    


def load_image(name, colorkey=None, scale=1.0):

    image = pg.image.load(name)

    size = image.get_size()
    size = (int(size[0] * scale), int(size[1] * scale))
    image = pg.transform.scale(image, size)

    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pg.RLEACCEL)
    return image

