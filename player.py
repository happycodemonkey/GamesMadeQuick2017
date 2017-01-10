import pygame
from pygame.locals import *
from constants.colors import *
from constants.directions import *


class Player:

	def __init__(self, surface):
		self.playerX = 10
		self.playerY = 10

		self.surface = surface
		
		playerObj = pygame.font.Font('freesansbold.ttf', 32)
		self.playerSurfObj = playerObj.render('@', True, RED, BLACK)
		self.playerRectObj = self.playerSurfObj.get_rect()
		self.playerRectObj.center = (self.playerX, self.playerY)

	def move(self, direction):
		if direction == RIGHT and self.playerX < self.surface.get_width():
			self.playerX += 5
		elif direction == DOWN and self.playerY < self.surface.get_height():
			self.playerY += 5
		elif direction == LEFT and self.playerX > 10:
			self.playerX -= 5
		elif direction == UP and self.playerY > 10:
			self.playerY -= 5
		self.playerRectObj.center = (self.playerX, self.playerY)
		self.surface.blit(self.playerSurfObj, self.playerRectObj)

