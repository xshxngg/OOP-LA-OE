class Hero:
    def __init__(self, name, role, damage_type):
        self.name = name
        self.role = role
        self.damage_type = damage_type

    def __str__(self):
        return f"{self.name} ({self.role} - {self.damage_type})"

    def description(self):
        return f"{self.name} is a {self.role} hero with {self.damage_type} damage."


class DreamTeam:
    def __init__(self, heroes):
        self.heroes = heroes

    def print_team_description(self):
        for hero in self.heroes:
            print(f"- {hero.description()}")


hero1 = Hero(name="Chou", role="Fighter", damage_type="Physical")
hero2 = Hero(name="Kagura", role="Mage", damage_type="Magic")
hero3 = Hero(name="Gusion", role="Assassin", damage_type="Magic")
hero4 = Hero(name="Tigreal", role="Tank", damage_type="Physical")
hero5 = Hero(name="Miya", role="Marksman", damage_type="Physical")

dream_team = DreamTeam(heroes=[hero1, hero2, hero3, hero4, hero5])
dream_team.print_team_description()