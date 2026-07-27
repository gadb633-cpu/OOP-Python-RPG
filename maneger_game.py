from player import *
from config import *
from room import *
from battle import *


class Main:
    
    player=Man(PLAYER_NAME,PLAYER_LIFE,PLAYER_STRENGH,PLAYER_AGILITY,PLAYER_LUCK)
    monster=Monster(MONSTER_NAME,MONSTER_LIFE,MONSTER_STRENGH,MONSTER_AGILITY,MONSTER_LUCK)
    battle=Battle(player,monster)
    battle.run()

Main()
