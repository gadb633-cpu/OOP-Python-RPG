from room import *
import random
from config import config

class Maze:
 
    def __init__(self,player):
        self.player=player
        self.rooms_in_maze= []
        self.visited_rooms=0

    def create_rooms(self):
        for i in range(4):
            chance_to_monster=random.randint(0,10)
            if chance_to_monster < 8:
                chance_to_goblin=random.randint(0,10)
                if chance_to_goblin<5:
                    self.rooms_in_maze.append(Room(self.player,Goblin(config)))
                else:
                    self.rooms_in_maze.append(Room(self.player,Orc(config)))
            else:
                self.rooms_in_maze.append(Room(self.player,None))

    




    
   
    
