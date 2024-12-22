class Player:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, target):
        if self.health <= 0:
            print(f"{self.name} cannot attack because they are defeated!")
            return
        
        target.health -= self.attack_power
        if target.health < 0:
            target.health = 0

        print(f"{self.name} attacked {target.name} for {self.attack_power} damage.")
        print(f"{target.name}'s remaining health: {target.health}")

    def heal(self, amount):
        if self.health <= 0:
            print(f"{self.name} cannot heal because they are defeated!")
            return

        self.health += amount
        print(f"{self.name} healed for {amount}. Current health: {self.health}")

player1 = Player("Alpha", 100, 15)
player2 = Player("Vexana", 80, 20)

while player1.health > 0 and player2.health > 0:
    player1.attack(player2) 
    if player2.health <= 0:
        print(f"{player2.name} is defeated! {player1.name} wins!")
        break

    player2.attack(player1)
    if player1.health <= 0:
        print(f"{player1.name} is defeated! {player2.name} wins!")
        break

    player1.heal(10)
    player2.heal(5)