from item import Item

class Equipable(Item):
    def __init__(self, name : str, description : str, drop_rate : float, rarity : str, item_type : str, stats : dict):
        super().__init__(name, description, drop_rate, rarity)
        self.itemType = item_type
        self.stats = stats