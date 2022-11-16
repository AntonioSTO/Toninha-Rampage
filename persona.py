import pygame as pg
from personagem_bat import Personagem_batalha
from config_jogo import load_image
from cronometro import Cronometro
from attacks import *
from minions import Minions

#====================================================
#           definição dos personagens
#====================================================

#TODO: como identificar o movimento especial do personagem?
#TODO: colocar as sprites nos personagens 

def img(diretorio):
    return pg.image.load(diretorio)

def scale(imagem, resolucao):
    return pg.transform.scale(imagem, resolucao)

##########################################################################
#                        Sprites Toninha                                 #
##########################################################################

sprite_maga_d = scale(img(r'./sprites/Toninha_maga.png'), (82, 82))
sprite_maga_e = pg.transform.flip(sprite_maga_d, True, False)
sprite_maga_ataque = scale(img(r'./sprites/maga_ataque.png'), (82, 82))

sprite_golem_d = scale(img(r'./sprites/toninha_golem.png'), (82, 82))
sprite_golem_e = pg.transform.flip(sprite_golem_d, True, False)
sprite_golem_ataque = scale(img(r'./sprites/golem_ataque.png'), (82, 82))

sprite_rei_d = scale(img(r'./sprites/toninha_rei.png'), (82, 82))
sprite_rei_e = pg.transform.flip(sprite_rei_d, True, False)
sprite_rei_ataque = scale(img(r'./sprites/rei_ataque.png'), (110, 82))

sprite_monge_d = scale(img(r'./sprites/toninha_monge.png'), (82, 82))
sprite_monge_e = pg.transform.flip(sprite_monge_d, True, False)
sprite_monge_ataque = scale(img(r'./sprites/monge_ataque.png'), (82, 82))
sprite_monge_cura = scale(img(r'./sprites/monge_cura.png'), (82, 82))

##########################################################################
#                        Sprites Soldados                                #
##########################################################################

sprite_atirador_e = scale(img(r'./sprites/soldado_atirador.png'), (82, 82))
sprite_atirador_d = pg.transform.flip(sprite_atirador_e, True, False)
sprite_atirador_ataque = scale(img(r'./sprites/atirador_ataque.png'), (82, 82))

sprite_parrudo_e = scale(img(r'./sprites/soldado_parrudo.png'), (82, 82))
sprite_parrudo_d = pg.transform.flip(sprite_parrudo_e, True, False)
sprite_parrudo_ataque = scale(img(r'./sprites/parrudo_ataque.png'), (82, 82))

sprite_general_e = scale(img(r'./sprites/soldado_general.png'), (82, 82))
sprite_general_d = pg.transform.flip(sprite_general_e, True, False)
sprite_general_ataque = scale(img(r'./sprites/general_ataque.png'), (82, 82))

sprite_medico_e = scale(img(r'./sprites/soldado_medico.png'), (82, 82))
sprite_medico_d = pg.transform.flip(sprite_medico_e, True, False)
sprite_medico_ataque = scale(img(r'./sprites/medico_ataque.png'), (82, 82))
sprite_medico_cura = scale(img(r'./sprites/medico_cura.png'), (82, 82))

#################################################################

sprite_amogus1 = scale(img(r'./sprites/amogus_walk1.png'), (82, 82))
sprite_amogus2 = scale(img(r'./sprites/amogus_walk2.png'), (82, 82))

sprite_amogus_ataque = scale(img(r'./sprites/amogus_ataque1.png'), (82, 82))


#====================================================
#               definição dos ataques
#====================================================

fisico = AtaqueFisico()
cura = Cura()
stun = Stun()
area = AtaqueArea()
evoque = Invoca()

#################################################################

toninha_maga = Personagem_batalha("Toninha Maga", 500, 1, 1, (0, 0),0, sprite_maga_d, sprite_maga_e, sprite_maga_ataque, sprite_maga_ataque, None, area)
toninha_golem = Personagem_batalha("Toninha Golen", 1200, 2, 0.5, (0, 0),0, sprite_golem_d, sprite_golem_e, sprite_golem_ataque,None, fisico, stun)
toninha_rei = Personagem_batalha("Toninha Rei", 800, 1, 1.5, (0, 0),0, sprite_rei_d, sprite_rei_e, sprite_rei_ataque,None, fisico, evoque)        #gerador de minions
toninha_monge = Personagem_batalha("Toninha Monge", 600, 1, 2, (0, 0),0, sprite_monge_d, sprite_monge_e, sprite_monge_ataque, sprite_monge_cura, fisico, cura)

soldado_atirador = Personagem_batalha("Soldado Atirador", 500, 1, 1, (0, 0),1, sprite_atirador_d, sprite_atirador_e, sprite_atirador_ataque, sprite_atirador_ataque, None, area)
soldado_parrudo = Personagem_batalha("Soldado Parrudo", 1100, 2, 0.5, (0, 0),1, sprite_parrudo_d, sprite_parrudo_e, sprite_parrudo_ataque, None, fisico, stun)
soldado_general = Personagem_batalha("General", 800, 1, 1.5, (0, 0),1, sprite_general_d, sprite_general_e, sprite_general_ataque, None, fisico,evoque)        #gerador de minions
soldado_medico = Personagem_batalha("Soldado Medico", 600, 1, 2, (0, 0),1, sprite_medico_d, sprite_medico_e,sprite_medico_ataque, sprite_medico_cura, fisico, cura)

amogus1 = Personagem_batalha("AMOGUS", 700, 1, 1.5, (0, 0),0, sprite_amogus1, sprite_amogus2, sprite_amogus_ataque, None, fisico, None)
amogus2 = Personagem_batalha("AMOGUS", 700, 1, 1.5, (0, 0),0, sprite_amogus1, sprite_amogus2, sprite_amogus_ataque, None, fisico, None)

minion1 = Minions(50, 0.1, 0.5, (0,0))
minion2 = Minions(50, 0.1, 0.5, (0,0))
minion3 = Minions(50, 0.1, 0.5, (0,0))
minion4 = Minions(50, 0.1, 0.5, (0,0))
minion5 = Minions(50, 0.1, 0.5, (0,0))

Lista1 = [toninha_maga, toninha_golem, toninha_rei, toninha_monge, amogus1]
Lista2 = [soldado_atirador, soldado_parrudo, soldado_general, soldado_medico, amogus2]
minions = [minion1, minion2, minion3, minion4, minion5]

