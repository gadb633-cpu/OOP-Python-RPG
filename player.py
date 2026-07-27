class Player:
    def __init__(self,name,life,strength,agility,luck):
        self.name=name
        self.life=life
        self.strength=strength
        self.agility=agility
        self.luck=luck
    def attacked(self):
        self.life-=self.life

class Man(Player):
    def __init__(self, name, life, strength, agility, luck):
        super().__init__(name, life, strength, agility, luck)

    
class Monster(Player):
    def __init__(self, name, life, strength, agility, luck):
        super().__init__(name, life, strength, agility, luck)


        
      
        