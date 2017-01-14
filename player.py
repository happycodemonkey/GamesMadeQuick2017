import pygame
from pygame.locals import *
from constants.colors import *
from constants.directions import *
from constants.init import *


class Player:

	def __init__(self, surface):
		self.x = 10
		self.y = 10

		self.surface = surface
		
		self.playerSurfObj = FONT.render('@', True, RED, BLACK)
		self.playerRectObj = self.playerSurfObj.get_rect()
		self.playerRectObj.center = (self.x, self.y)

	def move(self, direction):
		if direction == RIGHT and self.x < self.surface.get_width():
			self.x += 5
		elif direction == DOWN and self.y < self.surface.get_height():
			self.y += 5
		elif direction == LEFT and self.x > 10:
			self.x -= 5
		elif direction == UP and self.y > 10:
			self.y -= 5
		self.playerRectObj.center = (self.x, self.y)
		self.surface.blit(self.playerSurfObj, self.playerRectObj)

