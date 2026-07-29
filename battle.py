from config import config
class Battle:
    def __init__(self,player,monster):
        self.player=player
        self.monster=monster

    def first_attacker(self):
        if self.player.agility + self.player.luck >= self.monster.agility + self.monster.luck:
            self.attacker=self.player
            self.defander=self.monster
        else:
            self.attacker=self.monster
            self.defander=self.player

    def start_attack(self,defander):
        defander.take_damage(config["DAMAGE"])

    
    def run(self):

        if self.player.is_alive() and self.monster.is_alive():
            self.first_attacker()
            print(f"Starting battle: Attacker: {self.attacker.name} | Defander: {self.defander.name}")

            while self.defander.is_alive():
                self.start_attack(self.defander)
                if self.defander.is_alive():
                    hold_defender=self.defander
                    self.defander=self.attacker
                    self.attacker=hold_defender
                
            print(f"Battle finished, {self.attacker.name} win!")



        
        
            
    

        
            
