  #class Entity 
class Entity :
    def __init__(self, name: str, hp: int, attack: int, defense: int,):
        self.name = name
        self.hp = hp            
        self.maxHp = hp
        self.attack = attack
        self.defense = defense

    
def IsAlive():
     {
          
     }
     
def TakeDamage(self, amount: int):
        damage = max(0, amount - self.defense)
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

def Heal():{
     
}
     
def Attack():{
    
}

def PlayTurn():{
     
}
    