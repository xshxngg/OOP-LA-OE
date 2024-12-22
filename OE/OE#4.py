class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, target):
        target.health -= self.power
        print(f"{self.name} attacks {target.name} for {self.power} damage. {target.name}'s remaining health: {target.health}")

    def special_move(self):
        print(f"{self.name} doesn't have a unique special move.")

    def defend(self, attacker):
        reduced_damage = attacker.power // 2
        print(f"{self.name} defends! Damage reduced to {reduced_damage}. {self.name}'s remaining health: {self.health}")


class Warrior(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
        self.buff = False

    def special_move(self):
        print(f"{self.name} uses Shield Bash! Attack power doubled for the next attack.")
        self.power *= 2
        self.buff = True

class Mage(Character):
    def special_move(self, target=None):
        print(f"{self.name} casts Fireball! Target loses 100 health points.")
        if target:
            target.health -= 100
            print(f"{target.name}'s remaining health: {target.health}")

class Archer(Character):
    def special_move(self, target=None):
        print(f"{self.name} shoots a Piercing Arrow! Ignores the target's defense.")
        if target:
            target.health -= self.power
            print(f"{target.name}'s remaining health: {target.health}")

class Monster(Character):
    def special_move(self):
        print(f"{self.name} roars and gains extra health!")
        self.health += 20
        print(f"{self.name}'s health increased to {self.health}")

    def defend(self, attacker):
        reduced_damage = attacker.power // 2
        self.health -= reduced_damage
        print(f"{self.name} defends! Damage reduced to {reduced_damage}. {self.name}'s remaining health: {self.health}")


warrior = Warrior("Warrior", 100, 10)  
mage = Mage("Mage", 100, 20)
archer = Archer("Archer", 120, 25)
monster = Monster("Monster", 150, 50) 

print("\n--- Battle Begins ---")

warrior.special_move()
warrior.attack(monster)
warrior.defend(monster)
monster.attack(warrior)

mage.special_move(monster)
monster.special_move()
mage.defend(monster)
monster.attack(mage)

archer.defend(monster)
monster.attack(archer)
archer.special_move(monster)
archer.attack(monster)

print("\n--- Final Health States ---")
characters = [warrior, mage, archer, monster]
for character in characters:
    print(f"{character.name}'s remaining health: {character.health}")