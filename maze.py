from room import *
import random
class Maze:
 
    def __init__(self,player):
        self.player=player
        self.maze = []

    def add_room(self):
        for i in range(4):
            chance_to_monster=random.randint(0,10)
            if chance_to_monster < 8:
                chance_to_goblin=random.randint(0,10)
                if chance_to_goblin<5:
                    self.maze.append(Room(self.player,Goblin(config)))
                else:
                    self.maze.append(Room(self.player,Orc(config)))
            else:
                self.maze.append(Room(self.player,None))

    def get_room(self):
        self.add_room()
        for i in range(len(self.maze)):
                enter=input(f"do you want to go into room {i+1}? ")
                if enter == "yes":
                    print(f"you are now in room {i+1}")
                    self.maze[i].create_battle()
                else:
                    break




    
   
    
