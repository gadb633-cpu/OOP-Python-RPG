
class Battle:
    def __init__(self,player,monster):
        self.player=player
        self.monster=monster
        self.attacker=None
        self.defender=None
        self.winner=None

    def choose_attacker(self):
        if self.player.agility + self.player.luck >= self.monster.agility + self.monster.luck:
            self.attacker=self.player and self.defender=self.monster
        else:
            self.attacker=self.monster and self.defender=self.player

    def attack(self):
        return self.defender.life - self.defender.life

    def check_winner(self):
        if self.attack()<=0:
            self.winner = self.attacker.name
            return self.winner

        
            
    

        
            
