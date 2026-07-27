from player import *
from config import *
from maze import *


class Game_manager:
    def __init__(self):
        self.player = None
        self.maze = None
    def create_player(self):
        self.player=Player(PLAYER_NAME,PLAYER_LIFE,PLAYER_STRENGH,PLAYER_AGILITY,PLAYER_LUCK)
        return self.player
    def create_maze(self):
        self.maze=Maze()
        return self.maze
    def Game_summary():
        
game=Game_manager()
