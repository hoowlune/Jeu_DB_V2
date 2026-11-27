#class Entity 
class Entity :
    def __init__(self, name: str, hp: int, maxHp: int, attack: int, defense: int):
        self.name = name
        self.hp = hp            
        self.maxHp = maxHp
        self.attack = attack
        self.defense = defense

    
    def IsAlive(self):
        return self.hp > 0
 
        
    def TakeDamage(self, amount: int):
            damage = max(0, amount - self.defense)
            self.hp -= damage
            if self.hp < 0:
                self.hp = 0

    def Heal(self, amount: int):
            self.hp += amount
            if self.hp > self.maxHp:
                self.hp = self.maxHp
        

        
    def Attack(self, target):
            damage = max(0, self.attack - target.defense)
            target.TakeDamage(damage)
        


    def PlayTurn(self, target):
            self.Attack(target)
        

        