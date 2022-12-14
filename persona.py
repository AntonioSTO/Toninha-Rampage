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
sprite_maga_dano = scale(img(r'./sprites/maga_dano.png'), (82,82))
sprite_maga_agua = scale(img(r'./sprites/maga_agua.png'), (82,82))
sprite_maga_death = scale(img(r'./sprites/maga_death.png'), (82,82))

sprite_golem_d = scale(img(r'./sprites/toninha_golem.png'), (82, 82))
sprite_golem_e = pg.transform.flip(sprite_golem_d, True, False)
sprite_golem_ataque = scale(img(r'./sprites/golem_ataque.png'), (82, 82))
sprite_golem_dano = scale(img(r'./sprites/golem_dano.png'), (82,82))
sprite_golem_agua = scale(img(r'./sprites/golem_agua.png'), (82,82))
sprite_golem_death = scale(img(r'./sprites/golem_death.png'), (82,82))

sprite_rei_d = scale(img(r'./sprites/toninha_rei.png'), (82, 82))
sprite_rei_e = pg.transform.flip(sprite_rei_d, True, False)
sprite_rei_ataque = scale(img(r'./sprites/rei_ataque.png'), (110, 82))
sprite_rei_dano = scale(img(r'./sprites/rei_dano.png'), (82,82))
sprite_rei_agua = scale(img(r'./sprites/rei_agua.png'), (82,82))
sprite_rei_death = scale(img(r'./sprites/rei_death.png'), (82,82))

sprite_monge_d = scale(img(r'./sprites/toninha_monge.png'), (82, 82))
sprite_monge_e = pg.transform.flip(sprite_monge_d, True, False)
sprite_monge_ataque = scale(img(r'./sprites/monge_ataque.png'), (82, 82))
sprite_monge_cura = scale(img(r'./sprites/monge_cura.png'), (82, 82))
sprite_monge_dano = scale(img(r'./sprites/monge_dano.png'), (82,82))
sprite_monge_agua = scale(img(r'./sprites/monge_agua.png'), (82,82))
sprite_monge_death = scale(img(r'./sprites/monge_death.png'), (82,82))

##########################################################################
#                        Sprites Soldados                                #
##########################################################################

sprite_atirador_e = scale(img(r'./sprites/soldado_atirador.png'), (82, 82))
sprite_atirador_d = pg.transform.flip(sprite_atirador_e, True, False)
sprite_atirador_ataque = scale(img(r'./sprites/atirador_ataque.png'), (82, 82))
sprite_atirador_dano = pg.transform.flip(scale(img(r'./sprites/atirador_dano.png'), (82, 82)), True, False)
sprite_atirador_agua = pg.transform.flip(scale(img(r'./sprites/atirador_agua.png'), (82, 82)), True, False)
sprite_atirador_death = scale(img(r'./sprites/atirador_death.png'), (82,82))

sprite_parrudo_e = scale(img(r'./sprites/soldado_parrudo.png'), (82, 82))
sprite_parrudo_d = pg.transform.flip(sprite_parrudo_e, True, False)
sprite_parrudo_ataque = scale(img(r'./sprites/parrudo_ataque.png'), (82, 82))
sprite_parrudo_dano = scale(img(r'./sprites/parrudo_dano.png'), (82, 82))
sprite_parrudo_agua = pg.transform.flip(scale(img(r'./sprites/parrudo_agua.png'), (82, 82)), True, False)
sprite_parrudo_death = scale(img(r'./sprites/parrudo_death.png'), (82,82))

sprite_general_e = scale(img(r'./sprites/soldado_general.png'), (82, 82))
sprite_general_d = pg.transform.flip(sprite_general_e, True, False)
sprite_general_ataque = scale(img(r'./sprites/general_ataque.png'), (82, 82))
sprite_general_dano = pg.transform.flip(scale(img(r'./sprites/general_dano.png'), (82, 82)), True, False)
sprite_general_agua = pg.transform.flip(scale(img(r'./sprites/general_agua.png'), (82, 82)), True, False)
sprite_general_death = scale(img(r'./sprites/general_death.png'), (82,82))

sprite_medico_e = scale(img(r'./sprites/soldado_medico.png'), (82, 82))
sprite_medico_d = pg.transform.flip(sprite_medico_e, True, False)
sprite_medico_ataque = scale(img(r'./sprites/medico_ataque.png'), (82, 82))
sprite_medico_cura = scale(img(r'./sprites/medico_cura.png'), (82, 82))
sprite_medico_dano = pg.transform.flip(scale(img(r'./sprites/medico_dano.png'), (82, 82)), True, False)
sprite_medico_agua = pg.transform.flip(scale(img(r'./sprites/medico_agua.png'), (82, 82)), True, False)
sprite_medico_death = scale(img(r'./sprites/medico_death.png'), (82,82))


#################################################################

sprite_amogus1 = scale(img(r'./sprites/amogus_walk1.png'), (82, 82))
sprite_amogus2 = scale(img(r'./sprites/amogus_walk2.png'), (82, 82))

sprite_amogus_ataque = scale(img(r'./sprites/amogus_ataque1.png'), (82, 82))
sprite_amogus_dano = scale(img(r'./sprites/amogus_dano.png'), (82, 82))
sprite_amogus_agua = scale(img(r'./sprites/amogus_agua.png'), (82, 82))
sprite_amogus_death = scale(img(r'./sprites/amogus_death1.png'), (82,82))


#====================================================
#               definição dos ataques
#====================================================

fisico = AtaqueFisico()
cura = Cura()
stun = Stun()
area = AtaqueArea()
evoque1 = Invoca()
evoque2 = Invoca()
dist1 = AtaqueDistancia()
dist2 = AtaqueDistancia()
tp = Teleport()

#################################################################

toninha_maga = Personagem_batalha("Toninha Maga", 500, 1, 1, (0, 0),0, sprite_maga_d, sprite_maga_e, sprite_maga_ataque, sprite_maga_ataque, sprite_maga_dano, sprite_maga_agua, sprite_maga_death, dist1, area)
toninha_golem = Personagem_batalha("Toninha Golen", 1200, 2, 0.5, (0, 0),0, sprite_golem_d, sprite_golem_e, sprite_golem_ataque,sprite_golem_ataque, sprite_golem_dano, sprite_golem_agua, sprite_golem_death, fisico, stun)
toninha_rei = Personagem_batalha("Toninha Rei", 800, 1, 1.5, (0, 0),0, sprite_rei_d, sprite_rei_e, sprite_rei_ataque,sprite_rei_ataque, sprite_rei_dano, sprite_rei_agua, sprite_rei_death, fisico, evoque1)        #gerador de minions
toninha_monge = Personagem_batalha("Toninha Monge", 600, 1, 2, (0, 0),0, sprite_monge_d, sprite_monge_e, sprite_monge_ataque, sprite_monge_cura, sprite_monge_dano, sprite_monge_agua, sprite_monge_death, fisico, cura)

soldado_atirador = Personagem_batalha("Soldado Atirador", 500, 1, 1, (0, 0),1, sprite_atirador_d, sprite_atirador_e, sprite_atirador_ataque, sprite_atirador_ataque, sprite_atirador_dano, sprite_atirador_agua, sprite_atirador_death, dist2, area)
soldado_parrudo = Personagem_batalha("Soldado Parrudo", 1100, 2, 0.5, (0, 0),1, sprite_parrudo_d, sprite_parrudo_e, sprite_parrudo_ataque, sprite_parrudo_ataque, sprite_parrudo_dano, sprite_parrudo_agua, sprite_parrudo_death, fisico, stun)
soldado_general = Personagem_batalha("General", 800, 1, 1.5, (0, 0),1, sprite_general_d, sprite_general_e, sprite_general_ataque, sprite_general_ataque, sprite_general_dano, sprite_general_agua, sprite_general_death, fisico,evoque2)        #gerador de minions
soldado_medico = Personagem_batalha("Soldado Medico", 600, 1, 2, (0, 0),1, sprite_medico_d, sprite_medico_e,sprite_medico_ataque, sprite_medico_cura, sprite_medico_dano, sprite_medico_agua, sprite_medico_death, fisico, cura)

amogus1 = Personagem_batalha("AMOGUS", 700, 1, 1.5, (0, 0),0, sprite_amogus1, sprite_amogus2, sprite_amogus_ataque, sprite_amogus_ataque, sprite_amogus_dano, sprite_amogus_agua, sprite_amogus_death, fisico, tp)
amogus2 = Personagem_batalha("AMOGUS", 700, 1, 1.5, (0, 0),0, sprite_amogus1, sprite_amogus2, sprite_amogus_ataque, sprite_amogus_ataque, sprite_amogus_dano, sprite_amogus_agua, sprite_amogus_death, fisico, tp)

minion1 = Minions(50, 0.1, 0.5, (0,0))
minion2 = Minions(50, 0.1, 0.5, (0,0))
minion3 = Minions(50, 0.1, 0.5, (0,0))
minion4 = Minions(50, 0.1, 0.5, (0,0))
minion5 = Minions(50, 0.1, 0.5, (0,0))
minion6 = Minions(50, 0.1, 0.5, (0,0))


Lista1 = [toninha_maga, toninha_golem, toninha_rei, toninha_monge, amogus1]
Lista2 = [soldado_atirador, soldado_parrudo, soldado_general, soldado_medico, amogus2]
minions = [minion1, minion2, minion3, minion4, minion5, minion6]

