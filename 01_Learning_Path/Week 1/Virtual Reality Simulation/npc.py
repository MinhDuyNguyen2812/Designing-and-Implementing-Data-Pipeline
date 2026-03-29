from entity import Entity

class NPC(Entity):
    def __init__(self, name, position, role):
        super().__init__(name, position)
        self.role = role

    def interact(self):
        print(f"NPC {self.name} gives a quest.")