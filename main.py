from room import Room
from player import User
from config import *
class Main:
    def __init__(self):
        self.player=User(PLAYER_NAME,PLAYER_LIFE,PLAYER_STRENGH,PLAYER_AGILITY,PLAYER_LUCK)
        self.room=Room(self.player)
    def create_room(self):
        self.room.create_battle()
   
game=Main()
game.create_room()
