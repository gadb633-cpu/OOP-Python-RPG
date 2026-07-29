from config import config
class Battle:
    def __init__(self,player,monster):
        self.player=player
        self.monster=monster

    def choose_first_attacker(self):
        if self.player.agility + self.player.luck >= self.monster.agility + self.monster.luck:
            self.attacker=self.player
            self.defander=self.monster
        else:
            self.attacker=self.monster
            self.defander=self.player

    def attacking(self):
        
        self.defander.take_damage(config["DAMAGE"])
        print(f"{self.attacker.name} successfully attacked!\n{self.defander.name} life: {self.defander.life}\n")

    
    def run_battle(self):

        self.choose_first_attacker()
        print(f"Starting battle: Attacker: {self.attacker.name} | Defander: {self.defander.name}")
        print(f"{self.attacker.name} life: {self.attacker.life}\n{self.defander.name} life: {self.defander.life}\n")

        while self.defander.is_alive():
            self.attacking()
            if self.defander.is_alive():
                hold_defender=self.defander
                self.defander=self.attacker
                self.attacker=hold_defender
                
        print(f"Battle finished, {self.attacker.name} win!\n")
            


        
        
            
    

        
            
