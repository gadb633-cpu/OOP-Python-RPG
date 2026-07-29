from room import *
class Maze:
 
    def __init__(self,player):
        self.maze = [Room(player,Goblin(config)),Room(player,Orc(config)),Room(player,None),Room(player,None)]

    def get_room(self):
        for i in range(len(self.maze)):
                enter=input(f"do you want to go into room {i+1}? ")
                if enter == "yes":
                    print(f"you are now in room {i+1}")
                    self.maze[i].create_battle()
                else:
                    break



    
   
    

