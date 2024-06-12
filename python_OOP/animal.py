class Animal:
    def __init__(self, name):
        self.name = name
        self.health = 100
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def display_health(self):
        print(self.health)
        return self
    
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.health = 150
    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.health = 170
    def fly(self):
        self.health -= 10
        return self
    def display_health(self):
        print("I am a dragon")
        return self

draco = Dragon("Draco")

draco.display_health()

