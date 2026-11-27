from item import Item

class Consommable(Item):
    def __init__(self, name: str, description: str, dropRate: float, rarity: str, item_type: str, stats : str):
        super().__init__(name, description, dropRate, rarity, item_type, stats)
