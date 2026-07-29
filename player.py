from config import config
class Player:
    def __init__(self):
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
        super().__init__()
        self.name=config["PLAYER NAME"]
        self.life=config["PLAYER LIFE"]
        self.strength=config["PLAYER STRENGH"]
        self.agility=config["PLAYER AGILITY"]
        self.luck=config["PLAYER LUCK"]
    
class Goblin(Player):
    def __init__(self,config):
        super().__init__()
        self.name=config["GOBLIN NAME"]
        self.life=config["GOBLIN LIFE"]
        self.strength=config["GOBLIN STRENGH"]
        self.agility=config["GOBLIN AGILITY"]
        self.luck=config["GOBLIN LUCK"]

class Orc(Player):
    def __init__(self, config):
        super().__init__()
        self.name=config["ORC NAME"]
        self.life=config["ORC LIFE"]
        self.strength=config["ORC STRENGH"]
        self.agility=config["ORC AGILITY"]
        self.luck=config["ORC LUCK"]

            


        
      
        