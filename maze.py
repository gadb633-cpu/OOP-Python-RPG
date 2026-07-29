from room import *
class Maze:
 
    def __init__(self,player):
        self.maze = [Room(player,Goblin(config)),Room(player,Orc(config)),Room(player,None),Room(player,None)]

    def get_room(self):
        for room in self.maze:
            room.create_battle()

    
   
    

