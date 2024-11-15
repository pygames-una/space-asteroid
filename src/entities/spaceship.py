import pygame
from .missile import Missile

class Spaceship(pygame.sprite.Sprite):
  
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    pygame.mixer.init()
    # imagenes del objeto
    self.img_spaceship = pygame.image.load("./assets/img/spaceship.png")
    self.img_spaceship_explotion = pygame.image.load("./assets/img/explosion-spaceship.png")
    # caja de colision
    self.rect = self.img_spaceship.get_rect()
    # Crear la máscara de colisión a partir de la imagen, no toma los pixeles transparentes
    self.mask = pygame.mask.from_surface(self.img_spaceship)
    # posicion inicial nave
    self.rect.centerx = 400 # ancho 800 / 2 
    self.rect.centery = 530 # alto 600 - 150
    self.speed = 10
    self.alive = True
    self.list_shot = []
    self.sound_shoot = pygame.mixer.Sound("./assets/sound/shoot.wav")
    
  def move(self):
    
    if self.alive == True:
      # desplazamiento horizontal
      if self.rect.left <= 0: # limite izquiedo
        self.rect.left = 0
      elif self.rect.right > 800: # limite derecho
        self.rect.right = 800
        
  def shoot(self, x, y):
    if self.alive == True:
      adjustment_x = x - 12 # ajuste para centrar la salida del proyectil
      missile = Missile(adjustment_x, y)
      self.list_shot.append(missile)
      self.sound_shoot.play()
      
    
  
  def draw(self, layout):
    
    if self.alive == True:
      layout.blit(self.img_spaceship, self.rect)
    else:
      layout.blit(self.img_spaceship_explotion, self.rect)
    
    