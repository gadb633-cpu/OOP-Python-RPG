class Player:
    def __init__(self,name,life,strength,agility,luck):
        self.name=name
        self.life=life
        self.strength=strength
        self.agility=agility
        self.luck=luck
    
    def take_damage(self,damage):
        self.life-=damage
    
    def is_alive(self):
        if self.life>0:
            return True 

class User(Player):
    def __init__(self, name, life, strength, agility, luck):
        super().__init__(name, life, strength, agility, luck)
    

    
class Monster(Player):
    def __init__(self, name, life, strength, agility, luck):
        super().__init__(name, life, strength, agility, luck)


        
      
        