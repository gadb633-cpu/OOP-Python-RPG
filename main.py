from room import Room
from player import User
from config import config
class Main:
    def __init__(self):
        self.player=User(config)
        self.room=Room(self.player)
    def create_room(self):
        self.room.create_battle()
   
game=Main()
game.create_room()
