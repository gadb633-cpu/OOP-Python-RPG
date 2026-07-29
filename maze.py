from room import *
class Maze:

    def __init__(self,player):
        self.maze = [(Room(player,Monster(config))),Room(player,Monster(config))]

    def get_room(self):
        for room in self.maze:
            room.create_battle()

    
   
    

