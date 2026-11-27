from entity import Entity

class Enemy(Entity):
    def __init__(self, name, attack, defense, level):
        super().__init__(name, attack, defense)
        self.dropables = []

    def DropLoot(self):
        return 

    def Playturn(self,target):
        self.Attack(target)
        