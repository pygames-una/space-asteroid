import pygame

class Missile(pygame.sprite.Sprite):
  
  def __init__(self, position_x, position_y):
    pygame.sprite.Sprite.__init__(self)
    self.img_missile = pygame.image.load("./assets/images/missile-2.png")
    self.rect = self.img_missile.get_rect()
    self.speed = 10
    
    self.rect.top = position_y
    self.rect.left = position_x

    
  def trajectory(self):
    self.rect.top -= self.speed
    
  def draw(self, layout):
    layout.blit(self.img_missile, self.rect)

    
    