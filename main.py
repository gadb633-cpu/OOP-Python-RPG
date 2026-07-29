from player import User
from config import config
from maze import *
class Main:
    def __init__(self):
        self.player=User(config)
        self.maze=Maze(self.player)
    def enter_room(self):
        self.maze.get_room()
   
game=Main()
game.enter_room()

