from abc import ABC, abstractmethod

class GameCharacter(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def defend(self):
        pass