import pygame


class SoundsGame():
    def __init__(self):
        pygame.mixer.init()
        
    def fade_sound(self, time):
      pygame.mixer.music.fadeout(time)
      
    def background_sound(self):
      pygame.mixer.music.load("./assets/sounds/music/game.wav")
      pygame.mixer.music.play(3)

    def game_over(self):
      sound = pygame.mixer.Sound("./assets/sounds/music/game-over.wav")
      pygame.time.delay(1500)
      sound.play()

    def explotion_asteroid(self):
      sound = pygame.mixer.Sound("./assets/sounds/effects/explosion-asteroid.wav")
      sound.play()
    
    def explotion_spaceship(self):
      sound = pygame.mixer.Sound("./assets/sounds/effects/explosion-spaceship.aiff")
      sound.play()
