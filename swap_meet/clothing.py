from .item import Item

class Clothing(Item):

    def __init__(self, category="", condition=None, age=None):
        super().__init__(self, condition, age)
        self.category = "Clothing"
    
    def __str__(self):
        return "The finest clothing you could wear."
    
