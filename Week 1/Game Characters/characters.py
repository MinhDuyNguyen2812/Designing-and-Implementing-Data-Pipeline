from game_character import GameCharacter

class Warrior(GameCharacter):
    def attack(self):
        print(f"{self.name} swings a sword!")

    def defend(self):
        print(f"{self.name} blocks with a shield!")

class Mage(GameCharacter):
    def attack(self):
        print(f"{self.name} casts a fireball!")

    def defend(self):
        print(f"{self.name} conjures a magical barrier!")

class Archer(GameCharacter):
    def attack(self):
        print(f"{self.name} shoots an arrow!")

    def defend(self):
        print(f"{self.name} dodges quickly!")