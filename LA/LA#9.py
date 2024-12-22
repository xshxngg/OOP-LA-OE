class Car:
    def __init__(self, brand):
        self.brand = brand
        def __str__(self):
            return f"This car is a {self.brand}"
        
Kotse = Car("Toyota")
print(Kotse)
print(Kotse)
del Kotse
print(Kotse)