from battle import Battle
from player import Goblin,Orc

class Room:
    def __init__(self,player,monster):
        self.player=player
        self.monster=monster

    def create_battle(self):
        if isinstance(self.monster,(Goblin,Orc)):
            print(f"{self.monster.name} is in room. \n")
            battle=Battle(self.player,self.monster)
            battle.run_battle()
        else:
            print("Empty room, no battle!\n")


