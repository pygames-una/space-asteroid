import pygame


class WindowGame():

  def __init__(self, width, heigth, image = "./assets/images/space.jpg"):
    # definir ventana
    self.window = pygame.display.set_mode((width, heigth))
    
    # fondo
    self.background = pygame.image.load(image)


      
  def add_title(self, title = "Space Meteore"):
    pygame.display.set_caption(title)
      
  def draw_background(self):
    self.window.blit(self.background, (0, 0))
        