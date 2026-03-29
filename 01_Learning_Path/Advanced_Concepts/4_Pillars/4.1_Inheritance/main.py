class Animal:
    sound: str
    def __init__(self,sound, color):
        self.__sound = sound
        self.__color = color
    def make_sound(self):
        print(self.__sound)
    def showColor(self):
        print(self.__color)

class Cat(Animal):
    def __init__(self):
        super().__init__("Meow", "Black")

cat1 = Cat()
cat1.make_sound()
cat1.showColor()