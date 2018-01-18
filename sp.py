import random
import pygame
from main import * 



SCREEN_RECT = pygame.Rect (0,0,700,480)
CREATE_ENEMY_EVENT = pygame.USEREVENT
HERO_FIRE_EVENT = pygame.USEREVENT + 1 




class GameSprite(pygame.sprite.Sprite):
	def __init__(self,image_name,speed=1):
		super().__init__()
		self.image = pygame.image.load(image_name)
		self.rect = self.image.get_rect()
		self.speed = speed 

	def update(self):
		self.rect.x -= self.speed 


class Backgroup(GameSprite):
	def update(self):
		super().update()
		if self.rect.x <= -SCREEN_RECT.width:
			self.rect.x = SCREEN_RECT.width

class Enemy(GameSprite):
	def __init__(self):
		super().__init__('/home/zhangjiayi/桌面/答辩/tu/enemy1.png')
		self.bullets = pygame.sprite.Group()
		self.speed = random.randint(1,3)
		
		self.rect.x = SCREEN_RECT.width
		self.rect.y = random.randint(0,423)

	def update(self):
		super().update()
		if self.rect.x <= -43:
			self.kill()
	def __del__(self):
		print('消失了')


class Hero(GameSprite):
	def __init__(self):
		super().__init__('/home/zhangjiayi/桌面/答辩/tu/enemy2.png')
		self.rect.x = 0
		self.rect.y = 205

		self.bullets = pygame.sprite.Group()

	def update(self):
		self.rect.y += self.speed

		if self.rect.top < 0 :
			self.rect.top = 0 
		if self.rect.bottom > 480 :
			self.rect.bottom = 480 

	def fire(self):
		bullet = Bullet()
		bullet.rect.left = self.rect.x +100
		bullet.rect.centery = self.rect.centery

		
		bullet2 = Bullet()
		bullet2.rect.left = self.rect.x +100
		bullet2.rect.centery = self.rect.centery-5


		bullet3 = Bullet()
		bullet3.rect.left = self.rect.x +100
		bullet3.rect.centery = self.rect.centery + 5

		self.bullets.add(bullet,bullet2,bullet3)



class Hero2(GameSprite):
	def __init__(self):
		super().__init__('/home/zhangjiayi/桌面/答辩/tu/enemy2.png')
		self.rect.x = 0
		self.rect.y = 205

		self.bullets2 = pygame.sprite.Group()

	def update(self):
		self.rect.y += self.speed

		if self.rect.top < 0 :
			self.rect.top = 0 
		if self.rect.bottom > 480 :
			self.rect.bottom = 480 

	def fire2(self):
		bullet4 = Bullet()
		bullet4.rect.left = self.rect.x +100
		bullet4.rect.centery = self.rect.centery

		
		bullet5 = Bullet()
		bullet5.rect.left = self.rect.x +100
		bullet5.rect.centery = self.rect.centery-5


		bullet6 = Bullet()
		bullet6.rect.left = self.rect.x +100
		bullet6.rect.centery = self.rect.centery + 5

		self.bullets2.add(bullet4,bullet5,bullet6)


class Bullet(GameSprite):
	def __init__(self):
		super().__init__('/home/zhangjiayi/桌面/答辩/tu/bullet2.png',3)
	def __del__(self):
		pass
	def update(self):
		self.rect.x += self.speed
		if self.rect.left > 700 :
			self.kill()

class FHero1(GameSprite):
	def __init__(self):
		super().__init__('/home/zhangjiayi/桌面/答辩/tu/life.png',0)
		self.rect.x = 0
		self.rect.y = 170

		self.fbullets1 = pygame.sprite.Group()

	def update(self):
		self.rect.y += self.speed

		if self.rect.top < 0 :
			self.rect.top = 0 
		if self.rect.bottom > 480 :
			self.rect.bottom = 480 

	def ffire1(self):
		fbullet1 = Bullet()
		fbullet1.rect.left = self.rect.x +100
		fbullet1.rect.centery = self.rect.centery

		self.fbullets1.add(fbullet1)
class FHero2(GameSprite):
	def __init__(self):
		super().__init__('/home/zhangjiayi/桌面/答辩/tu/life.png',0)
		self.rect.x = 0
		self.rect.y = 260

		self.fbullets2 = pygame.sprite.Group()

	def update(self):
		self.rect.y += self.speed

		if self.rect.top < 0 :
			self.rect.top = 0 
		if self.rect.bottom > 480 :
			self.rect.bottom = 480 

	def ffire2(self):
		fbullet2 = Bullet()
		fbullet2.rect.left = self.rect.x +100
		fbullet2.rect.centery = self.rect.centery

		self.fbullets2.add(fbullet2)
		print('66')
class FHero3(GameSprite):
	def __init__(self):
		super().__init__('/home/zhangjiayi/桌面/答辩/tu/life.png',0)
		self.rect.x = 0
		self.rect.y = 170

		self.fbullets3 = pygame.sprite.Group()

	def update(self):
		self.rect.y += self.speed

		if self.rect.top < 0 :
			self.rect.top = 0 
		if self.rect.bottom > 480 :
			self.rect.bottom = 480 

	def ffire3(self):
		fbullet3 = Bullet()
		fbullet3.rect.left = self.rect.x +100
		fbullet3.rect.centery = self.rect.centery

		self.fbullets3.add(fbullet3)
class FHero4(GameSprite):
	def __init__(self):
		super().__init__('/home/zhangjiayi/桌面/答辩/tu/life.png',0)
		self.rect.x = 0
		self.rect.y = 260

		self.fbullets4 = pygame.sprite.Group()

	def update(self):
		self.rect.y += self.speed

		if self.rect.top < 0 :
			self.rect.top = 0 
		if self.rect.bottom > 480 :
			self.rect.bottom = 480 

	def ffire4(self):
		fbullet4 = Bullet()
		fbullet4.rect.left = self.rect.x +100
		fbullet4.rect.centery = self.rect.centery
		self.fbullets4.add(fbullet4)
