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
            chance_to_monster=random.randint(0,100)
            if chance_to_monster < 80:
                chance_to_goblin=random.randint(0,100)
                if chance_to_goblin<50:
                    self.rooms_in_maze.append(Room(self.player,Goblin(config)))
                else:
                    self.rooms_in_maze.append(Room(self.player,Orc(config)))
            else:
                self.rooms_in_maze.append(Room(self.player,None))

    




    
   
    
