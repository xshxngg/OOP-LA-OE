class Animal():
    def __init__(self, name, type):
        self.name = name
        self.type = type
        
    def describeAnimal(self):
        print(f"{self.name} is a {self.type}")
        
class Fish(Animal): 
    def __init__(self, name, type):
        super().__init__(name, type)
        self.can_swim= True
        
animal= Fish("Tilapia", "Fish")
print(animal.can_swim)