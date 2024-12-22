class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

suzuki = Car("suzuki", "orange")
print(suzuki.brand)
suzuki.brand = "ford"
print(suzuki.brand)