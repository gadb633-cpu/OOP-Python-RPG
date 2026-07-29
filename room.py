from battle import Battle
from player import Goblin,Orc
from config import config

class Room:
    def __init__(self,player,monster):
        self.player=player
        self.monster=monster

    def create_battle(self):
        if isinstance(self.monster,(Goblin,Orc)):
            battle=Battle(self.player,self.monster)
            battle.run()
        else:
            print("empty room, no battle!")


