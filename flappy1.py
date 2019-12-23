import pygame, time
from random import *
from pygame.locals import *

from ctypes import windll
windll.shcore.SetProcessDpiAwareness(5)

def images():
	bank={}
	bank["t1"] = pygame.image.load("Tunnel8.png")
	bank["t2"] = pygame.image.load("Tunnel7.png")
	bank["perso"] = pygame.image.load("Dragon1.png").convert_alpha()

	return bank


def monter_perso(y):
    y-=10

    return y


def NewTuyeaux(rect, rect2):
	for i in range(2):
		rect.x = randint(300 , 400)
		rect.y = randint(-100 , 100)
		mesTuyaux.append(rect)

		rect2.x = randint(300 , 400)
		rect2.y = randint(300 , 500)
		mesTuyaux2.append(rect2)

	return mesTuyaux, mesTuyaux2


fenetre = pygame.display.set_mode((400,600))
horloge = pygame.time.Clock()

bank = images()
fond = pygame.image.load("bg2-bell.jpg").convert()

rectPerso = bank["perso"].get_rect()
rectPerso.x = 150
rectPerso.y = 300- rectPerso.h

rect = bank["t1"].get_rect()
rect2 = bank["t2"].get_rect()

mesTuyaux=[]
mesTuyaux2=[]
continuer = True
state = "jeu"
i = 0

pygame.key.set_repeat(4, 4)

while continuer:
	touches = pygame.key.get_pressed()
	events = pygame.event.get()
	horloge.tick(60)	

	if state == "jeu":
		i += 1
		touch = False
		#rectPerso.y += 4

		if i%60 == 0:
			NewTuyeaux(rect, rect2)		

		if touches[pygame.K_ESCAPE]:
			#state = "menu"
			continuer = 0 

		if touches[pygame.K_SPACE]:
			rectPerso.y -= 10

		fenetre.blit(fond, (0 ,0))
		fenetre.blit(bank["perso"], rectPerso)

		for r in mesTuyaux:
			r.x -=2
			fenetre.blit(bank["t1"], r)

			if rectPerso.colliderect(r):
				#state = "menu"
				print("Touché")

		for t in mesTuyaux2:
			t.x -=2
			fenetre.blit(bank["t2"], t)

			if rectPerso.colliderect(t):
				#state = "menu"
				print("Touché")
		print(horloge)
				


	pygame.display.flip()