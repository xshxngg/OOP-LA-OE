class Appliance:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def operate(self):
        print("Operating!") 

    def info(self):
        print(f"Brand: {self.brand}, Model: {self.model}") 

class WashingMachine(Appliance):
    def operate(self):
        print("Washing clothes!") 

class Refrigerator(Appliance):
    def operate(self):
        print("Keeping food cold!") 

class Microwave(Appliance):
    def operate(self):
        print("Heating food!")

wm = WashingMachine("LG", "TwinWash")
ref = Refrigerator("Samsung", "FamilyHub")
mw = Microwave("Panasonic", "Toaster")

appliances = [wm, ref, mw]

for appliance in appliances:
    appliance.info()  
    appliance.operate()  
    print("---")