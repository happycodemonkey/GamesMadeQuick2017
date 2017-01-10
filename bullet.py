import pygame
from constants.directions import *
from constants.colors import *

class Bullet:

	def __init__(self, surface, player, direction):
		self.bulletX = player.playerX
		self.bulletY = player.playerY
		
		self.surface = surface

		self.bullet = pygame.Rect((self.bulletX, self.bulletY), (5,5))

		self.direction = direction
		self.remove = False

	def update(self):
		if self.direction == RIGHT: 
			self.bullet = self.bullet.move(5, 0)
		elif self.direction == DOWN:
			self.bullet = self.bullet.move(0, 5)
		elif self.direction == LEFT:
			self.bullet = self.bullet.move(-5, 0)
		elif self.direction == UP:
			self.bullet = self.bullet.move(0, -5)

		pygame.draw.rect(self.surface, WHITE, self.bullet)

		if self.bulletX > self.surface.get_width() or self.bulletY > self.surface.get_height() or self.bulletX < 10 or self.bulletY < 10:
			self.remove = True
