from battle import Battle
from player import Monster
from config import *


class Room:
    def __init__(self,player):
        self.player=player
        self.monster=Monster(MONSTER_NAME,MONSTER_LIFE,MONSTER_STRENGH,MONSTER_AGILITY,MONSTER_LUCK)

    def create_battle(self):
        if isinstance(self.monster,Monster):
            battle=Battle(self.player,self.monster)
            battle.run()

