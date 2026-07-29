from player import User
from config import config
from maze import *
class Main:
    def __init__(self):
        self.player=User(config)
        self.maze=Maze(self.player)
    def print_starting_massage(self):
        print("\n=== Wellcome to Battle Maze game! ===\n")
    def enter_room(self):
        self.maze.get_room()
   
game=Main()
game.print_starting_massage()
game.enter_room()

