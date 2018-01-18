import pygame 
from sp import * 


class PlaneGame(object):
	
	def __init__(self):
		print('游戏初始化')
		self.init = pygame.init()
		self.screen = pygame.display.set_mode((SCREEN_RECT.size))
		self.clock = pygame.time.Clock()

		self.__create_sprites()


		pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)

		pygame.time.set_timer(HERO_FIRE_EVENT,500)
	def start_game(self):
		print('开始游戏')
		
		while True:
			
			self.clock.tick(60)
			self.__event_handler()
			self.__check_collide()
			self.__update_sprites()
			pygame.display.update()
	def __create_sprites(self):
		bg1 = Backgroup('/home/zhangjiayi/桌面/答辩/tu/background.png')
		bg2 = Backgroup('/home/zhangjiayi/桌面/答辩/tu/background.png')
		bg2.rect.x = bg2.rect.width
		self.back_group = pygame.sprite.Group(bg1,bg2)

		self.enemy_group = pygame.sprite.Group()

		self.hero = Hero()
		self.hero2 = Hero2()
		self.fhero1 = FHero1()
		self.fhero2 = FHero2()
		self.fhero3 = FHero3()
		self.fhero4 = FHero4()
		self.hero_group = pygame.sprite.Group(self.hero,self.hero2,self.fhero1,self.fhero2,self.fhero3,self.fhero4)

	def __event_handler(self):
		key_pressed = pygame.key.get_pressed()
		for event in pygame.event.get():
			print(event)
			if event.type == pygame.QUIT or key_pressed[113]:
				PlaneGame.__game_over()
			elif event.type == CREATE_ENEMY_EVENT:
				self.enemy = Enemy()
				self.enemy_group.add(self.enemy)
			elif event.type == HERO_FIRE_EVENT:
				self.hero.fire()
				self.hero2.fire2()
				self.fhero1.ffire1()
				self.fhero2.ffire2()
				self.fhero3.ffire3()
				self.fhero4.ffire4()
			if key_pressed[119]:
				self.hero.speed = -2
				self.fhero1.speed = -2
				self.fhero2.speed = -2
			elif key_pressed[115]:
				self.hero.speed = 2 
				self.fhero1.speed =2
				self.fhero2.speed = 2
			elif key_pressed[273]:
				self.hero2.speed = -2 
				self.fhero3.speed = -2
				self.fhero4.speed = -2

			elif key_pressed[274]:
				self.hero2.speed = 2
				self.fhero3.speed=2
				self.fhero4.speed = 2
			else :
				self.hero.speed = 0 
				self.hero2.speed = 0 
				self.fhero1.speed = 0
				self.fhero2.speed = 0
				self.fhero3.speed = 0
				self.fhero4.speed = 0



	def __check_collide(self):
			pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)
			pygame.sprite.groupcollide(self.hero2.bullets2,self.enemy_group,True,True)
			pygame.sprite.groupcollide(self.fhero1.fbullets1,self.enemy_group,True,True)
			pygame.sprite.groupcollide(self.fhero2.fbullets2,self.enemy_group,True,True)
			pygame.sprite.groupcollide(self.fhero3.fbullets3,self.enemy_group,True,True)
			pygame.sprite.groupcollide(self.fhero4.fbullets4,self.enemy_group,True,True)



			enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
			enemies2 = pygame.sprite.spritecollide(self.hero2,self.enemy_group,True)
			fenemies1 = pygame.sprite.spritecollide(self.fhero1,self.enemy_group,True)
			fenemies2 = pygame.sprite.spritecollide(self.fhero2,self.enemy_group,True)
			fenemies3 = pygame.sprite.spritecollide(self.fhero3,self.enemy_group,True)
			fenemies4 = pygame.sprite.spritecollide(self.fhero4,self.enemy_group,True)

			if len(enemies) > 0 :
				self.hero.kill()
				PlaneGame.__game_over()
			if len(enemies2) >0 :
				self.hero2.kill()
				PlaneGame.__game_over()

			if len(fenemies1) >0 :
				self.fhero1.kill()
				PlaneGame.__game_over()

			if len(fenemies2) >0 :
				self.fhero2.kill()
				PlaneGame.__game_over()
			if len(fenemies3) >0 :
				self.fhero3.kill()
				PlaneGame.__game_over()
			if len(fenemies4) >0 :
				self.fhero4.kill()
				PlaneGame.__game_over()
	def __update_sprites(self):
		for group in [self.back_group,self.enemy_group,self.hero_group,self.hero.bullets,self.hero2.bullets2,self.fhero1.fbullets1,self.fhero2.fbullets2,self.fhero3.fbullets3,self.fhero4.fbullets4]:
			group.update()
			group.draw(self.screen)

	@staticmethod
	def __game_over():
		print('游戏结束')
		pygame.quit()
		exit()

if __name__ =='__main__' :
	game = PlaneGame()
	game.start_game()






