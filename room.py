from battle import Battle
from player import Goblin,Orc
from config import config


class Room:
    def __init__(self,player):
        self.player=player
        self.goblin=Goblin(config)
        self.orc=Orc(config) 

    def create_battle(self):
        if isinstance(self.monster,Monster):
            battle=Battle(self.player,self.monster)
            battle.run()


