import pygame
import random
from pygame.locals import *
from constants.directions import *
from constants.colors import *
from constants.init import *

class Enemy:

	def __init__(self, surface, player):
		self.x = random.randrange(0, surface.get_width())
		self.y = random.randrange(0, surface.get_height())
		self.deltaX = player.x - self.x
		self.deltaY = player.y -  self.y
		
		self.surface = surface
		self.player = player

		self.enemySurfObj = FONT.render('*', True, BLUE, BLACK)
		self.enemyRectObj = self.enemySurfObj.get_rect()
		self.enemyRectObj.center = (self.x, self.y)

	def update(self):
		self.x += self.deltaX
		self.y += self.deltaY
		self.enemyRectObj.center = (self.x, self.y)
		self.surface.blit(self.enemySurfObj, self.enemyRectObj)
