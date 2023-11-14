import pygame
from pygame.locals import *
from pygame import mixer

pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()
pygame.init()
 
clock = pygame.time.Clock()
FPS = 60

screen_width, screen_height = 1000, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('OneManProject')

tile_size = 50
game_over = 0
main_manu = True
level = 1
max_levels = 5

#load images
bg = pygame.image.load('assets/Background/Space.png')
restart_img = pygame.image.load('assets/Menu/Restart.png')
start_img = pygame.image.load('assets/Menu/Start.png')
leave_img = pygame.image.load('assets/Menu/Leave.png')

#load sounds
dead_fx = pygame.mixer.Sound('assets/Sound/Dead.mp3')
dead_fx.set_volume(0.5)
game_over_fx = pygame.mixer.Sound('assets/Sound/Gameover.mp3')
game_over_fx.set_volume(0.5)
win_fx = pygame.mixer.Sound('assets/Sound/Win.mp3')
win_fx.set_volume(0.5)
click_fx = pygame.mixer.Sound('assets/Sound/Click.mp3')
click_fx.set_volume(0.5)

#reset level/move to the next level
def reset_level(level):
    if level == 2:	
        world_data = [
        [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2], 
        [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
        [3, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
        [3, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
        [3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
        [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
        [3, 0, 1, 0, 1, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
        [3, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 5, 5, 1, 1, 0, 0, 2], 
        [3, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 2], 
        [3, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
        [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2], 
        [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 2], 
        [3, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 2], 
        [3, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 2], 
        [3, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2], 
        [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
        ]
		
	
        player.reset(100, screen_height - 140)
        imposter_group.empty()
        lava_group.empty()
        exit_group.empty()
        world = World(world_data)

        return world

    if level == 3:	
        world_data = [
        [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2], 
        [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
        [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
        [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
        [3, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 2], 
        [3, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 5, 1, 0, 0, 0, 0, 0, 2], 
        [3, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 2], 
        [3, 6, 0, 1, 5, 5, 5, 1, 5, 1, 5, 1, 0, 0, 0, 0, 0, 0, 0, 2], 
        [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 2], 
        [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
        [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2], 
        [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
        [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 2], 
        [3, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 2], 
        [3, 0, 0, 1, 0, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 2], 
        [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
        ]
		
	
        player.reset(100, screen_height - 140)
        imposter_group.empty()
        lava_group.empty()
        exit_group.empty()
        world = World(world_data)

        return world

    if level == 4:	
        world_data = [
        [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2], 
        [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
        [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
        [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
        [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
        [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
        [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2], 
        [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 2], 
        [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 6, 0, 2], 
        [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 2], 
        [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 5, 2], 
        [3, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 5, 1, 2], 
        [3, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 5, 5, 1, 1, 2], 
        [3, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 5, 5, 1, 1, 1, 1, 2], 
        [3, 0, 0, 0, 0, 4, 4, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 2], 
        [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
        ]
		
        player.reset(100, screen_height - 140)
        imposter_group.empty()
        lava_group.empty()
        exit_group.empty()
        world = World(world_data)

        return world

    if level == 5:	
        world_data = [
        [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2], 
        [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
        [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
        [3, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
        [3, 6, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
        [3, 1, 1, 1, 1, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
        [3, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 2], 
        [3, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 2], 
        [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2], 
        [3, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
        [3, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2], 
        [3, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2], 
        [3, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2], 
        [3, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 4, 0, 0, 0, 0, 2], 
        [3, 0, 0, 1, 5, 1, 5, 1, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2], 
        [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
        ]
        player.reset(100, screen_height - 140)
        imposter_group.empty()
        lava_group.empty()
        exit_group.empty()
        world = World(world_data)

        return world


class Button():
	def __init__(self, x, y, image):
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def draw(self):
		action = False

		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				action = True
				self.clicked = True
				click_fx.play()

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False
		
		#draw button
		screen.blit(self.image, self.rect)

		return action


class Player():
	def __init__(self, x, y):
		self.reset(x, y)


	def update(self, game_over):
		dx = 0
		dy = 0
		walk_cooldown = 3.5

		if game_over == 0:

			#get keypresses
			key = pygame.key.get_pressed()
			if key[pygame.K_w] and self.jumped == False and self.in_air == False:
				self.vel_y = -15
				self.jumped = True
			if key[pygame.K_w] == False:
				self.jumped = False
			if key[pygame.K_a]:
				dx -= 5
				self.counter += 1
				self.direction = -1
			if key[pygame.K_d]:
				dx += 5
				self.counter += 1
				self.direction = 1
			if key[pygame.K_a] == False and key[pygame.K_d] == False:
				self.counter = 0
				self.index = 0
				if self.direction == 1:
					self.image = self.images_right[self.index]
				if self.direction == -1:
					self.image = self.images_left[self.index]

			#animation
			if self.counter > walk_cooldown:
				self.counter = 0
				self.index += 1
				if self.index >= len(self.images_right):
					self.index = 0
				if self.direction == 1:
					self.image = self.images_right[self.index]
				if self.direction == -1:
					self.image = self.images_left[self.index]



			#add gravity
			self.vel_y += 1
			if self.vel_y > 10:
				self.vel_y = 10
			dy += self.vel_y

			#check for collision
			self.in_air = True
			for tile in world.tile_list:
				#check for collision in x direction
				if tile[1].colliderect(self.rect.x + dx, self.rect.y , self.width, self.height):
					dx = 0
				#check for collision in y direction
				if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
					#check if player is below the ground
					if self.vel_y < 0:
						dy = tile[1].bottom - self.rect.top
						self.vel_y = 0
					#check if player is above the ground
					elif self.vel_y >= 0:
						dy = tile[1].top - self.rect.bottom
						self.vel_y = 0
						self.in_air = False


			#check of collision with enemies
			if pygame.sprite.spritecollide(self, imposter_group, False):
					game_over = -1
					dead_fx.play()
					game_over_fx.play()
			#check of collision with lava
			if pygame.sprite.spritecollide(self, lava_group, False):
					game_over = -1
					dead_fx.play()
					game_over_fx.play()
			#check of collision with exit
			if pygame.sprite.spritecollide(self, exit_group, False):
					game_over = 1
					win_fx.play()

			#update player coordnates
			self.rect.x += dx
			self.rect.y += dy

		elif game_over == -1:
			self.image = self.dead_image
			self.image = pygame.transform.scale(self.image, (60, 60))

		#draw player onto screen
		screen.blit(self.image, self.rect)

		return game_over
	
	def reset(self, x, y):
		self.images_right = []
		self.images_left = []
		self.index = 0
		self.counter = 0
		for num in range(1, 5):
			img_right = pygame.image.load(f'assets/Characters/Red-Crewmate{num}.png')
			img_right = pygame.transform.scale(img_right, (40, 50))
			img_left = pygame.transform.flip(img_right, True, False)
			self.images_right.append(img_right)
			self.images_left.append(img_left)
		self.dead_image = pygame.image.load('assets/Characters/Dead-Crewmate.png')
		self.image = self.images_right[self.index]
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.vel_y = 0
		self.jumped = False
		self.direction = 0
		self.in_air = True

class World():
	def __init__(self, data):
		self.tile_list = []

		skeld_floor1 = pygame.image.load('assets/Terrain/skeldfloor.png')
		skeld_wall1 = pygame.image.load('assets/Terrain/skeldwall1.png')
		skeld_wall2 = pygame.image.load('assets/Terrain/skeldwall2.png')

		row_count = 0
		for row in data:
			col_count = 0
			for tile in row:
				if tile == 1:
					img = pygame.transform.scale(skeld_floor1, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 2:
					img = pygame.transform.scale(skeld_wall1, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 3:
					img = pygame.transform.scale(skeld_wall2, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 4:
					imposter = Enemy(col_count * tile_size, row_count * tile_size)
					imposter_group.add(imposter)
				if tile == 5:
					lava = Lava(col_count * tile_size, row_count * tile_size)
					lava_group.add(lava)
				if tile == 6:
					exit = Exit(col_count * tile_size, row_count * tile_size)
					exit_group.add(exit)
				col_count += 1
			row_count += 1
			
	def draw(self):
		for tile in self.tile_list:
			screen.blit(tile[0], tile[1])


class Enemy(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load('assets/Characters/Red-Imposter.png')
		self.image = pygame.transform.scale(img, (50, 50))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.move_direction = 1
		self.move_counter = 0
	
	def update(self):
		self.rect.x += self.move_direction
		self.move_counter +=1
		if abs(self.move_counter) > 100:
			self.move_direction *= -1
			self.move_counter *= -1
		
class Lava(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load('assets/Characters/Lava.png')
		self.image = pygame.transform.scale(img, (tile_size,tile_size))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

class Exit(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load('assets/Terrain/Exit.png')
		self.image = pygame.transform.scale(img, (tile_size,tile_size))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y


if level == 1:	
    world_data = [
    [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2], 
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
    [3, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 6, 0, 2], 
    [3, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 1, 1, 1, 1, 2], 
    [3, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 2], 
    [3, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
    [3, 1, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
    [3, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 2], 
    [3, 1, 1, 5, 5, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2], 
    [3, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2], 
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2], 
    [3, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 2], 
    [3, 0, 0, 0, 1, 1, 1, 1, 5, 5, 5, 5, 5, 5, 1, 1, 1, 1, 1, 2], 
    [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
    ]
	

player = Player(100, screen_height - 140)

imposter_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()
exit_group = pygame.sprite.Group()

world = World(world_data)

#create buttons
restart_button = Button(350, 400, restart_img)
start_button = Button(315, 325, start_img)
leave_button = Button(355, 485, leave_img)

run = True
while run:
	
    clock.tick(FPS)

    screen.blit(bg, (0, 0))

    if main_manu == True:
        if leave_button.draw():
           run = False
        if start_button.draw():
           main_manu = False

    else:
        world.draw()
        if game_over == 0:
            imposter_group.update()

        imposter_group.draw(screen)
        lava_group.draw(screen)
        exit_group.draw(screen)

        game_over = player.update(game_over)

		#if player died
        if game_over == -1:
            if restart_button.draw():
               player.reset(100, screen_height - 140)
               game_over = 0
		
		#if player completed a level
        if game_over == 1:
			#reset game and go to next level
            player.reset(100, screen_height - 140)
            level += 1
            world = reset_level(level)
            game_over = 0
			#reset to level 1
            if level > max_levels:
                level == 1
            world = reset_level(level)
            game_over = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
			
    pygame.display.update()

pygame.quit()