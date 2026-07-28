from config import *
from player import *

class Battle:
    def __init__(self):
        self.player=User(PLAYER_NAME,PLAYER_LIFE,PLAYER_STRENGH,PLAYER_AGILITY,PLAYER_LUCK)
        self.monster=Monster(MONSTER_NAME,MONSTER_LIFE,MONSTER_STRENGH,MONSTER_AGILITY,MONSTER_LUCK)

    def first_attacker(self):
        if self.player.agility + self.player.luck >= self.monster.agility + self.monster.luck:
            self.attacker=self.player
            self.defander=self.monster
        else:
            self.attacker=self.monster
            self.defander=self.player

    def start_attack(self,attacker,defander):
        self.attacker=attacker
        self.defander=defander
        self.defander.take_damage(DAMAGE)

    
    def run(self):

        self.first_attacker()
        print(f"Start battle: Attacker: {self.attacker.name} | Defander: {self.defander.name}")
        self.start_attack(self.attacker,self.defander)
        if not self.defander.is_alive():
            print(f"{self.attacker.name} win!")

        while self.player.is_alive() and self.monster.is_alive():
            self.start_attack(self.defander,self.attacker)
            if not self.defander.is_alive():
                print(f"{self.attacker.name} win!")
                break
            self.start_attack(self.attacker,self.defander)
            if not self.defander.is_alive():
                print(f"{self.attacker.name} win!")
                break


        
        
            
    

        
            
