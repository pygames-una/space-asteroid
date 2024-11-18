import pygame
import random

images = [
  "./assets/images/asteroid-1.png",
  "./assets/images/asteroid-2.png",
  "./assets/images/asteroid-3.png"
]

class Asteroid(pygame.sprite.Sprite):
  
  def __init__(self, position_x, position_y):
    pygame.sprite.Sprite.__init__(self)
    self.img_asteroid = pygame.image.load(self.get_random_image())
    self.img_asteroid_explotion = pygame.image.load("./assets/images/explosion-asteroid.png")
    self.rect = self.img_asteroid.get_rect()
    self.mask = pygame.mask.from_surface(self.img_asteroid)
    self.speed = 1
    self.alive = True
    self.rect.top = position_y
    self.rect.left = position_x
    self.explosion_start_time = None  
    
  
  def get_random_image(self):
    return random.choice(images)
  
  def trajectory(self):
    self.rect.top += self.speed
  
  def draw(self, layout):
      if self.alive:
          layout.blit(self.img_asteroid, self.rect)
      elif self.explosion_start_time:
          layout.blit(self.img_asteroid_explotion, self.rect)
  
  def increment_speed(self):
    self.speed += 0.5

  def explode(self):
      self.alive = False
      self.explosion_start_time = pygame.time.get_ticks()
      
  def is_explosion_finished(self):
      if self.explosion_start_time:
          # Duración de la explosión
          return pygame.time.get_ticks() - self.explosion_start_time > 500  
      return False
  
    