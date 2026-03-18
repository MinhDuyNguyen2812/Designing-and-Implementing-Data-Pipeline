from entity import Entity

class Object(Entity):
    def __init__(self, name, position, objectType):
        super().__init__(name, position)
        self.objectType = objectType

    def interact(self):
        print(f"Object {self.name} can be used.")