import pygame
import sys
from pygame.locals import *
from random import randint

from utils.game_global_variables import GameGlobalVariables
from utils.sounds_game import SoundsGame

# entidades
from entities.spaceship import Spaceship
from entities.asteroid import Asteroid


#variables globales
list_asteroid = []
spaceship = Spaceship()
sound_game = SoundsGame()
variable_game = GameGlobalVariables()


def load_asteroid(x,y):
  asteroid = Asteroid(x, y)
  list_asteroid.append(asteroid)
  
def game_over():
  print("fin")
  pygame.mixer.init()
  pygame.time.delay(1500)
  sound_game.game_over()
  
  #global is_playing
  global list_asteroid
  #is_playing = False
  variable_game.is_playing_change()


# funcio principal
def game():
  
  pygame.init()

  last_asteroid_time = 0
  clock = pygame.time.Clock()
  
  # definir ventana
  window = pygame.display.set_mode((variable_game.window_width, variable_game.window_height))
  
  # fondo
  background = pygame.image.load("./assets/images/space.jpg")
  
  # titulo
  pygame.display.set_caption("Space Meteore")
  # sonido de fondo
  sound_game.background_sound()
  
  # tipografia para textos
  font_points = pygame.font.SysFont("Consolas", 18)
  color_font = (120, 200, 40)
  font_game_over = pygame.font.SysFont("Consolas", 50, bold=True)
  color_font_end = (245, 21, 61)

  # Ciclo del juego
  while True:

    # Manejar eventos de entrada
    for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
        elif event.type == pygame.KEYDOWN and spaceship.alive:
          if event.key == K_LEFT: 
              spaceship.rect.left -= spaceship.speed
          elif event.key == K_RIGHT:
              spaceship.rect.right += spaceship.speed
          elif event.key == K_SPACE:
              x, y = spaceship.rect.center
              spaceship.shoot(x, y)
  
    # Dibujar fondo
    window.blit(background, (0, 0))
    
    # marcador de puntos
    text_points = font_points.render(f"Points: {str(variable_game.points)}", 0, color_font)
    window.blit(text_points, (10,10))

    # Dibujar y mover la nave
    spaceship.draw(window)
    spaceship.move()

    # Generar asteroides en intervalos
    current_time = pygame.time.get_ticks()
    if current_time - last_asteroid_time > 1000 and variable_game.is_playing == True:  # Cada 1000 ms (1 segundo)
      last_asteroid_time = current_time
      position_x = randint(20, 780)
      load_asteroid(position_x, 0)

    # Actualizar y dibujar asteroides
    for asteroid in list_asteroid[:]:
      asteroid.draw(window)
      asteroid.trajectory()
      if asteroid.rect.top > variable_game.window_height:
        list_asteroid.remove(asteroid)
      else:
        # Verificar colisión con la nave
        if asteroid.rect.colliderect(spaceship.rect):
          list_asteroid.remove(asteroid)
          spaceship.alive = False
          sound_game.explotion_spaceship()
          game_over()
        elif asteroid.alive == False and asteroid.is_explosion_finished():
          # Eliminar el asteroide si su explosión ha terminado
          list_asteroid.remove(asteroid)
          

    # Actualizar y dibujar disparos
    for shoot in spaceship.list_shot[:]: 
      shoot.draw(window)
      shoot.trajectory()
      if shoot.rect.top < -10:
          spaceship.list_shot.remove(shoot)
      else:
        # Verificar colisión entre disparos y asteroides
        for asteroid in list_asteroid:
          if shoot.rect.colliderect(asteroid.rect) and asteroid.alive:
            asteroid.explode()  # Cambia el estado del asteroide a explotar
            spaceship.list_shot.remove(shoot)
            sound_game.explotion_asteroid()
            variable_game.increase_points(10)
              
    if variable_game.is_playing == False:
      # remover los asteroides de la ventana
      for asteroid in list_asteroid:
        list_asteroid.remove(asteroid)
    
      text_game_over = font_game_over.render("Game Over", True, color_font_end)
      window.blit(text_game_over, (250,250))
      pygame.mixer.music.fadeout(1500)
      

    # Actualizar pantalla y controlar FPS
    pygame.display.update()
    clock.tick(60)  # Limita a 60 FPS  

# Ejecutar funcion principal
game()
      
  
  
  