import pygame
import random
from pygame.locals import *
from constants.directions import *
from constants.colors import *

class Enemy:

	def __init__(self, surface, player):
		self.x = random.randrange(0, surface.get_width())
		self.y = random.randrange(0, surface.get_height())
		self.surface = surface
		self.player = player

		self.enemyObj = pygame.font.Font('freesansbold.ttf', 32)
		self.enemySurfObj = self.enemyObj.render('*', True, BLUE, BLACK)
		self.enemyRectObj = self.enemySurfObj.get_rect()
		self.enemyRectObj.center = (self.x, self.y)

	def update(self):
		newX = self.player.x - self.x
		newY = self.player.y -  self.y
		self.enemyRectObj.center = (newX, newY)
		self.surface.blit(self.enemySurfObj, self.enemyRectObj)
