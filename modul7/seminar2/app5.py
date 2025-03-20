# Exercițiul 5: Preziceți rezultatul codului

# TODO Analizați codul de mai jos și preziceți rezultatul afișat la rulare:

class Vehicle:
    def __init__(self, type):
        self.type = type

    def describe(self):
        return "This is a " + self.type

class Bicycle(Vehicle):
    def __init__(self, type, gears):
        super().__init__(type)
        self.gears = gears

    def describe(self):
        base_description = super().describe()
        return base_description + " with " + str(self.gears) + " gears"

bike = Bicycle("mountain bike", 18)
print(bike.describe())

"""
Instrucțiuni:
    - Scrieți predicția voastră pentru rezultatul codului.
    - Rulați codul în mediul Python pentru a verifica răspunsul.
"""

# This is a mountain bike with 18 gears