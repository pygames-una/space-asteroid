from abc import ABC

class GameGlobalVariables(ABC):
    end_game = False
    points = 0
    consumables = [None, None, None]
    
    def end_game_change(self):
        self.end_game = not self.end_game
    
    def add_consumable(self, consumable):
        for i in range(3):
            if(self.consumables[i] == None):
                self.consumables[i] = consumable
            
    def spend_consumable(self, position):
        self.consumables[position] = None
        
    def increase_points(self, value):
        self.points += value