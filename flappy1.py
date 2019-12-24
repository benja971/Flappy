import pygame, time
from random import *
from pygame.locals import *

from ctypes import windll
windll.shcore.SetProcessDpiAwareness(3)

def images():
	bank={}
	bank["t1"] = pygame.image.load("Tunnel8.png")
	bank["t2"] = pygame.image.load("Tunnel7.png")
	bank["perso"] = pygame.image.load("Dragon1.png").convert_alpha()

	return bank


def NewTuyeaux(bank, rect, rect2):
	#x = randint(300 , 400)
	x= 250

	for i in range(4):
		rect.x = x
		rect.y = randint(-100 , 100)
		mesTuyeaux.append(rect)

		rect2.x = x
		rect2.y = randint(300 , 500)
		mesTuyeaux2.append(rect2)

		print("mesTuyeaux:" ,mesTuyeaux)
		print("mesTuyeaux2:" ,mesTuyeaux2)

	return mesTuyeaux; mesTuyeaux2


fenetre = pygame.display.set_mode((400,600))
bank = images()
horloge = pygame.time.Clock()
continuer = True
i = 0
mesTuyeaux = []
mesTuyeaux2 = []

rectPerso = bank["perso"].get_rect()
rectPerso.y = 300 - rectPerso.h

rect = bank["t1"].get_rect() 
rect2 = bank["t2"].get_rect() 

fond = pygame.image.load("bg2-bell.jpg").convert()

pygame.key.set_repeat(4, 4)

while continuer:
	touches = pygame.key.get_pressed()
	events = pygame.event.get()
	horloge.tick(60)	
	i += 1

	rect.x -= 3.5
	rect2.x -= 3.5

	if i%120 == 0:
		NewTuyeaux(bank, rect, rect2)

	if touches[pygame.K_ESCAPE]:
		continuer = False

	fenetre.blit(fond, (0 ,0))
	fenetre.blit(bank["perso"], rectPerso)

	for p in mesTuyeaux:
		fenetre.blit(bank["t1"], p)

	for o in mesTuyeaux2:
		fenetre.blit(bank["t2"], o)

	pygame.display.flip()