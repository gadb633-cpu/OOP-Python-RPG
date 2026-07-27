from player import *
from config import * 
class Room:
    def __init__(self):
        self.monster=None
    def create_monster(self):
        self.monster=Monster(MONSTER_NAME,MONSTER_LIFE,MONSTER_STRENGH,MONSTER_AGILITY,MONSTER_LUCK)
        return self.monster


