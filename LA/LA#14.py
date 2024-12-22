class Spiderman:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describeSpiderman(self):
        print(f"{self.name} played Spiderman when he was {self.age} years old.")

class Tobey(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle

class Andrew(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age) 
        self.movieTitle = movieTitle
class Tom(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle

tobey = Tobey("tobey mcquirre", 26, "Spider-Man") 
andrew = Andrew("andrew garfield", 27, "The Amazing Spider-Man")
tom = Tom("tom holland", 18, "Spider-Man: Homecoming")

print(tobey.name.upper(), "-", tobey.movieTitle)
print(andrew.name.upper(), "-", andrew.movieTitle)
print(tom.name.upper(), "-", tom.movieTitle)

tobey.describeSpiderman()
andrew.describeSpiderman()
tom.describeSpiderman() 