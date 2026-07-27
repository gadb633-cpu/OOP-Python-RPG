from config import *
class Battle:
    def __init__(self,player,monster):
        self.player=player
        self.monster=monster
        self.attacker=None
        self.defander=None

    def first_attacker(self):
        if self.player.agility + self.player.luck >= self.monster.agility + self.monster.luck:
            self.attacker=self.player
            self.defander=self.monster
        else:
            self.attacker=self.monster
            self.defander=self.player

    def attack(self,attacker,defander):
        self.attacker=attacker
        self.defander=defander
        self.defander.attacked(DAMAGE)

    
    def run(self):
        self.first_attacker()
        print(f"Start battle: Attacker: {self.attacker.name} | Defander: {self.defander.name}")
        self.attack(self.attacker,self.defander)
        if not self.defander.is_alive():
            print(f"{self.attacker.name} win!")

        while self.player.is_alive() and self.monster.is_alive():
            self.attack(self.defander,self.attacker)
            if not self.defander.is_alive():
                print(f"{self.attacker.name} win!")
                break
            self.attack(self.attacker,self.defander)
            if not self.defander.is_alive():
                print(f"{self.attacker.name} win!")
                break


        
        
            
    

        
            
