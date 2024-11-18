import pygame
import sys
from pygame.locals import *
import time
from random import randint

# entidades
from entities.spaceship import Spaceship
from entities.asteroid import Asteroid


#variables globales
points = 0
window_width = 800
window_height = 600
is_playing = True
list_asteroid = []
spaceship = Spaceship()


def load_asteroid(x,y):
  asteroid = Asteroid(x, y)
  list_asteroid.append(asteroid)
  
def game_over():
  print("fin")
  pygame.mixer.init()
  pygame.time.delay(1500)
  sound_game_over = pygame.mixer.Sound("./assets/sounds/music/game-over.wav")
  sound_game_over.play()
  global is_playing
  global list_asteroid
  is_playing = False


# funcio principal
def game():
  
  pygame.init()
  pygame.mixer.init()
  
  # variables 
  global points
  global is_playing
  last_asteroid_time = 0
  clock = pygame.time.Clock()
  
  # definir ventana
  window = pygame.display.set_mode((window_width, window_height))
  # fondo
  background = pygame.image.load("./assets/images/space.jpg")
  # titulo
  pygame.display.set_caption("Space Meteore")
  # sonido de fondo
  pygame.mixer.music.load("./assets/sounds/music/game.wav")
  pygame.mixer.music.play(3)
  # sonidos colisiones
  sound_explotion_asteroid = pygame.mixer.Sound("./assets/sounds/effects/explosion-asteroid.wav")
  sound_explotion_spaceship = pygame.mixer.Sound("./assets/sounds/effects/explosion-spaceship.aiff")
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
    text_points = font_points.render(f"Points: {str(points)}", 0, color_font)
    window.blit(text_points, (10,10))

    # Dibujar y mover la nave
    spaceship.draw(window)
    spaceship.move()

    # Generar asteroides en intervalos
    current_time = pygame.time.get_ticks()
    if current_time - last_asteroid_time > 1000 and is_playing == True:  # Cada 1000 ms (1 segundo)
      last_asteroid_time = current_time
      position_x = randint(20, 780)
      load_asteroid(position_x, 0)

    # Actualizar y dibujar asteroides
    for asteroid in list_asteroid[:]:
      asteroid.draw(window)
      asteroid.trajectory()
      if asteroid.rect.top > window_height:
        list_asteroid.remove(asteroid)
      else:
        # Verificar colisión con la nave
        if asteroid.rect.colliderect(spaceship.rect):
          list_asteroid.remove(asteroid)
          spaceship.alive = False
          sound_explotion_spaceship.play()
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
            sound_explotion_asteroid.play()
            points += 10
              
    if is_playing == False:
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
      
  
  
  