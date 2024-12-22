class ml_hero():
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def describe(self):
        return f"{self.name} is a {self.role} hero."
    
ml1 = ml_hero("Luoyi", "Mage")
ml2 = ml_hero("Ixia", "Marksman")

print(ml1.describe())
print(ml2.describe())