from entity import Entity

class Player(Entity):
    def __init__(self, name, position, level):
        super().__init__(name, position)
        self.level = level

    def interact(self):
        print(f"Player {self.name} attacks an enemy.")