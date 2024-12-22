class Toy():
    def __init__(self,name,price):
        self.name= name 
        self.price= price
    def toyDetails(self):
        print(f"Available: {self.name} for only ${self.price}")
        
class Car(Toy):
    def __init__(self, name, price):
        super().__init__(name, price)
        
carToy= Car("Hot wheels", "50")
carToy.toyDetails()