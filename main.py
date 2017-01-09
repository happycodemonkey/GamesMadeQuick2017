import pygame, sys
from pygame.locals import *
import player
from constants.directions import *

pygame.init()
FPS = 30
fpsClock = pygame.time.Clock()

GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('AGDQ Game Jam!')

player = player.Player(400, 300)

while True:
	keys = pygame.key.get_pressed()
	if keys[K_UP] or keys[K_w]:
		player.move(UP)
	elif keys[K_DOWN] or keys[K_s]:
		player.move(DOWN)
	elif keys[K_LEFT] or keys[K_a]:
		player.move(LEFT)
	elif keys[K_RIGHT] or keys[K_d]:
		player.move(RIGHT)
	DISPLAYSURF.blit(player.playerSurfObj, player.playerRectObj)
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
