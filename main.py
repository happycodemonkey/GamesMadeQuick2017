import pygame, sys
from pygame.locals import *
import player, bullet, enemy
from constants.directions import *
from constants.colors import *
from constants.init import *

#pygame.init()
FPS = 30
fpsClock = pygame.time.Clock()

GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('AGDQ Game Jam!')

player = player.Player(DISPLAYSURF)
bullets = []	
enemies = []

start = False
while True:
	DISPLAYSURF.fill(BLACK)
	
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
	elif keys[K_RETURN]:
		start = True

	if start == False:
		# display the opening screen
		welcomeSurf = FONT.render('RNGESUS', True, WHITE)
		welcomeSurfRect = welcomeSurf.get_rect()
		welcomeSurfRect.center = (WIDTH/2, HEIGHT/2)

		controlsSurf = FONT.render('W-A-S-D to move, Arrows to shoot', True, WHITE)
		controlsSurfRect = controlsSurf.get_rect()
		controlsSurfRect.center = (WIDTH/2, (HEIGHT/2) + 50)

		enterSurf = FONT.render('Hit Enter', True, WHITE)
		enterSurfRect = enterSurf.get_rect()
		enterSurfRect.center = (WIDTH/2, (HEIGHT/2) + 100)

		DISPLAYSURF.blit(welcomeSurf, welcomeSurfRect)
		DISPLAYSURF.blit(controlsSurf, controlsSurfRect)
		DISPLAYSURF.blit(enterSurf, enterSurfRect)

	else:
		DISPLAYSURF.blit(player.playerSurfObj, player.playerRectObj)
		enemies.append(enemy.Enemy(DISPLAYSURF, player))
		
		for b in bullets:
			b.update()
			
			if b.remove:
				bullets.remove(b)
		
		for e in enemies:
			e.update()

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
