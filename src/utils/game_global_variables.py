from abc import ABC

class GameGlobalVariables(ABC):
    #variables globales
    points = 0
    window_width = 800
    window_height = 600
    is_playing = True
    end_game = False
    consumables = [None, None, None]
    
    def is_playing_change(self):
        self.is_playing = not self.is_playing
    
    def add_consumable(self, consumable):
        for i in range(3):
            if(self.consumables[i] == None):
                self.consumables[i] = consumable
            
    def spend_consumable(self, position):
        self.consumables[position] = None
        
    def increase_points(self, value):
        self.points += value