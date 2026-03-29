class Entity:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def interact(self):
        print(f"{self.name} interacts in the world.")