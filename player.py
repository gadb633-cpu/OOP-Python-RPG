from config import config
class Player:
    def __init__(self,config):
        self.name=""
        self.life=""
        self.strength=""
        self.agility=""
        self.luck=""
    
    def take_damage(self,damage):
        self.life-=damage
    
    def is_alive(self):
        if self.life>0:
            return True 

class User(Player):
    def __init__(self,config):
        super().__init__(config)
        self.name=config["PLAYER NAME"]
        self.life=config["PLAYER LIFE"]
        self.strength=config["PLAYER STRENGH"]
        self.agility=config["PLAYER AGILITY"]
        self.luck=config["PLAYER LUCK"]
    
class Monster(Player):
    def __init__(self,config):
        super().__init__(config)
        self.name=config["MONSTER NAME"]
        self.life=config["MONSTER LIFE"]
        self.strength=config["MONSTER STRENGH"]
        self.agility=config["MONSTER AGILITY"]
        self.luck=config["MONSTER LUCK"]
            


        
      
        