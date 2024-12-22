class ml_hero():
    def __init__(self, name, role):
        self.name = name
        self.role = role

ml1 = ml_hero("Luoyi", "Mage")
ml2 = ml_hero("Ixia", "Marksman")

print(ml1.name)
print(ml1.role)
print(ml2.name)
print(ml2.role)