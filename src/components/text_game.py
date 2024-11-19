import pygame

class TextGame():
  text_es = ["Puntos:", "Juego Terminado"]
  text_en = ["Points:", "Game Over"]
  
  def __init__(self):
    pygame.init()
  
  def points(self, layout, points):
    font = pygame.font.SysFont("Consolas", 18)
    color = (120, 200, 40)
    text = font.render(f"{self.get_text(0)} {str(points)}", 0, color)
    layout.blit(text, (10,10))
    
    
  def game_over(self, layout):
    font = pygame.font.SysFont("Consolas", 50, bold=True)
    color = (245, 21, 61)
    text = font.render( self.get_text(1), True, color)
    layout.blit(text, (250,250))
    
  def get_text(self,text, lenguaje = "en"):
    
    if lenguaje == "es":
      return self.text_es[text]
    
    return self.text_en[text]