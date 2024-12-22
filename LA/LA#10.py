class Vehicle():
    def __init__(self, brand, model, fuel):
        self.brand= brand
        self. model= model
        self.fuel= fuel
    def describeVehicle(self):
        return print(f"brand: {self.brand}, model: {self.model}, fuel: {self.fuel}")
        
class Car(Vehicle):
    pass

class Motor(Vehicle):
    pass

car1= Car("Honda", "Civic", "Diesel")
motor1= Motor("Honda", "Click", "Unleaded")

car1.describeVehicle()
motor1.describeVehicle()