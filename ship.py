import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	def __init__(self, ai_settings, screen):
		super(Ship, self).__init__()

		self.screen = screen
		self.ai_settings = ai_settings

		"""加载飞船图像并获取其外接矩阵"""
		image =  pygame.image.load('images/ship.png')
		self.image = pygame.transform.scale(image,(60,80))

		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		"""将每艘新飞船放在屏幕底部中央"""
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		"""在飞船的属性中存储小数值"""
		self.center = float(self.rect.centerx)
		self.bottom = float(self.rect.bottom)

		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor
		if self.moving_up and self.rect.top > self.screen_rect.bottom/2:
			self.bottom -= self.ai_settings.ship_speed_factor
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.bottom += self.ai_settings.ship_speed_factor

		self.rect.centerx = self.center
		self.rect.bottom = self.bottom

	def  blitme(self):
		"""在指定位置绘制飞船"""
		self.screen.blit(self.image, self.rect)

	def center_ship(self):
		self.center = self.screen_rect.centerx
		self.bottom = self.screen_rect.bottom
