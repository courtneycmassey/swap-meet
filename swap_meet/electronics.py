from .item import Item

class Electronics(Item):

    def __init__(self, category="", condition=None, age=None):
        super().__init__(self, condition, age)
        self.category = "Electronics"
    
    def __str__(self):
        return "A gadget full of buttons and secrets."
    