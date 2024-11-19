import pygame

class RoomLevel:
    
    def __init__(self, state, layer):
        self.state = state
        self.layer = layer
        
    def draw(self, asteroids):
        pass
    
    #Aqui se debe hacer el llamado de la creacion de los asteroides
    #Este metodo es el que debe ser llamado por el main
    def steps(self):
        self.draw() #Primero llamamos a los elementos a dibujar 
        pass