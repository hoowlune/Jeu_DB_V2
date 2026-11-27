from database import Database
from entity import Entity
from item import Item
from player import Player

class Character(Entity):
    def __init__(self, name : str, attack : int, defense : int, level : int):
        super().__init__(name, attack, defense)

def EquipItem(self, item):
        if item.itemType == "weapon":
            self.attack += item.stats["attack"]
        elif item.itemType == "armor":
            self.defense += item.stats["defense"]

def UnequipItem(self, item):
        if item.itemType == "weapon":
            self.attack -= item.stats["attack"]
        elif item.itemType == "armor":
            self.defense -= item.stats["defense"]

def IsSlotAvailable(self, itemType):
        if itemType == "weapon":
            return self.weaponSlot is None
        elif itemType == "armor":
            return self.armorSlot is None
        else:
            return False

def GetEquipment(self):
        equipment = {}
        if self.weaponSlot is not None:
            equipment["weapon"] = self.weaponSlot.name
        if self.armorSlot is not None:
            equipment["armor"] = self.armorSlot.name
        return equipment

def ProjectDamage(self, target):
        damage = max(0, self.attack - target.defense)
        return damage

def PlaTurn(self, target):
        self.Attack(target)