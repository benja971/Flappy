import pygame
from random import *
from pygame.locals import *

def obst1():
	bank={}
	
	bank["t1"] = pygame.image.load("Tunnel8.png")
	bank["t2"] = pygame.image.load("Tunnel7.png")
	bank["perso"] = pygame.image.load("Dragon1.png").convert_alpha()

	return bank
	
def monter_perso(y):
    y-=3

    return y

def descendre_perso(y):
    y+=3
    return y


fenetre = pygame.display.set_mode((600,600))
fond = pygame.image.load("bg2-bell.jpg").convert()

bank = obst1()

mesTuyaux=[]

ranges = [(850 , 1050),(1250 , 1450)]

for i in range(10):
	rect = bank["t1"].get_rect()
	irange = i%2
	rect.x = randint(ranges[irange][0] , ranges[irange][1])
	rect.y = randint(-100 , 100)
	mesTuyaux.append(rect)

x1 = randint(850 , 1050)
x2 = randint(850 , 1050)
x3 = randint(1250 , 1450)
x4 = randint(1250 , 1450)
x5 = randint(1750 , 1950)
x6 = randint(1750 , 1950)
x7 = randint(2350 , 2550)
x8 = randint(2350 , 2550)
x9 = randint(2750 , 2950)
x10= randint(2750 , 2950)

y1 = randint(-100 , 100)
y2 = y1 + 250

y3 = randint(-100 , 100)
y4 = y3 + 250

y5 = randint(-100 , 100)
y6 = y5 + 250

y7 = randint(-100 , 100)
y8 = y7 + 250

y9 = randint(-100 , 100)
y10 = y9 + 250

rectPerso = bank["perso"].get_rect()
rectPerso.x = 200
rectPerso.y = 10
continuer = True
pygame.key.set_repeat(4, 4)

while continuer:

	for r in mesTuyaux:
		if r.x >0:
			r.x -=1

	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = False

		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
			    continuer = False
			if event.key == K_UP:
			    rectPerso.y = monter_perso(rectPerso.y)
			if event.key == K_DOWN:
			    rectPerso.y = descendre_perso(rectPerso.y)

	if x10 < -300:
		x1 = randint(850 , 1050)

	touch = False
	for r in mesTuyaux:
		if rectPerso.colliderect(r):
			print ("Je te touche")
			touch=True

	if touch == False:
		print ("je touche pas")

	fenetre.blit(fond, (0 ,0))

	for r in mesTuyaux:
		fenetre.blit(bank["t1"], r)

	fenetre.blit(bank["perso"], rectPerso)

	pygame.display.flip()
	