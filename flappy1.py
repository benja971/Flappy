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

def NewTuyeaux():
	for i in range(1):
		rect = bank["t1"].get_rect()
		rect.x = randint(300 , 400)
		rect.y = randint(-100 , 100)
		mesTuyaux.append(rect)

		rect2 = bank["t2"].get_rect()
		rect2.x = randint(300 , 400)
		rect2.y = randint(300 , 500)
		mesTuyaux2.append(rect2)

		return mesTuyaux, mesTuyaux2, rect1, rect2

horloge = pygame.time.Clock()

fenetre = pygame.display.set_mode((400,600))
fond = pygame.image.load("bg2-bell.jpg").convert()

bank = images()

mesTuyaux=[]
mesTuyaux2=[]

rectPerso = bank["perso"].get_rect()
rectPerso.x = 150
rectPerso.y = 300- rectPerso.h

continuer = True
i = 0 
state = "menu"

pygame.key.set_repeat(4, 4)

while continuer:
	touches = pygame.key.get_pressed()
	events = pygame.event.get()

	if state == "menu":
		if touches[pygame.K_ESCAPE]:
			continuer = False

		if touches[pygame.K_SPACE]:
			state = "jeu "

		fenetre.blit(fond, (0,0))

	if state == "jeu":
		i += 1
		horloge.tick(60)	
		touch = False
		rectPerso.y += 3

		if i%100 == 0:
			NewTuyeaux()		

		if touches[pygame.K_ESCAPE]:
			state = "menu"

		if touches[pygame.K_SPACE]:
			rectPerso.y -= 10

		fenetre.blit(fond, (0 ,0))
		fenetre.blit(bank["perso"], rectPerso)

		for r in mesTuyaux:
			r.x -=5
			fenetre.blit(bank["t1"], r)

			if rectPerso.colliderect(rect1):
				touch = True

		for t in mesTuyaux2:
			t.x -=5
			fenetre.blit(bank["t2"], t)

			if rectPerso.colliderect(rect2):
				touch = True


	pygame.display.flip()
	