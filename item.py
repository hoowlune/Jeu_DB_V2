class Item:
    def __init__(self, name : str, description : str, dropRate : int, rarity : int, itemType : str, stats):

        self.name = name
        self.description = description
        self.dropRate = dropRate
        self.rarity = rarity
        self.itemType = itemType
        self.stats = stats