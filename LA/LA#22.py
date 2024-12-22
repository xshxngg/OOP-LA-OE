class BirthdayParty:
    def __init__(self, theme, foods, special_dish, secret_dish):
        self.theme = theme
        self.foods = foods
        self.special_dish = special_dish
        self.__secret_dish = secret_dish

    def show_foods(self):
        print(f"\nParty Theme: {self.theme}")
        print("Available Foods:")
        for food in self.foods:
            print(f"- {food}")
        print(f"Special Dish: {self.special_dish}")
        self.__reveal_secret_dish()
    def __reveal_secret_dish(self):
        print(f"Secret Dish: {self.__secret_dish}")

party1 = BirthdayParty(
    theme="Ihaw-ihaw",
    foods=["Barbecue", "Inasal", "Hotdog"],
    special_dish="Betamax",
    secret_dish="Adidas"
)

party2 = BirthdayParty(
    theme="Pasta",
    foods=["Spaghetti", "Carbonara", "Pesto"],
    special_dish="Lasagna",
    secret_dish="Sopas"
)

party3 = BirthdayParty(
    theme="Pinoy Ulams",
    foods=["Adobo", "Sinigang", "Kaldereta"],
    special_dish="Bicol Xpress",
    secret_dish="Tuyo"
)

party1.show_foods()
party2.show_foods()
party3.show_foods()