import pygame, sys
from pygame.locals import *
import player, bullet
from constants.directions import *
from constants.colors import *

pygame.init()
FPS = 30
fpsClock = pygame.time.Clock()

GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('AGDQ Game Jam!')

player = player.Player(DISPLAYSURF)
bullets = []

# get player on the screen initially
DISPLAYSURF.blit(player.playerSurfObj, player.playerRectObj)

while True:
	keys = pygame.key.get_pressed()
	if keys[K_UP]:
		bullets.append(bullet.Bullet(DISPLAYSURF, player, UP))
	elif keys[K_w]:
		player.move(UP)
	elif keys[K_DOWN]:
		bullets.append(bullet.Bullet(DISPLAYSURF, player, DOWN))
	elif keys[K_s]:
		player.move(DOWN)
	elif keys[K_LEFT]:
		bullets.append(bullet.Bullet(DISPLAYSURF, player, LEFT))
	elif keys[K_a]:
		player.move(LEFT)
	elif keys[K_RIGHT]:
		bullets.append(bullet.Bullet(DISPLAYSURF, player, RIGHT))
	elif keys[K_d]:
		player.move(RIGHT)
	
	for b in bullets:
		b.update()
		
		if b.remove:
			bullets.remove(b)

	pygame.display.update()
	fpsClock.tick(FPS)
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE or event.key == K_q:
				pygame.quit()
				sys.exit()
