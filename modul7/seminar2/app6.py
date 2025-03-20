class Player:
    def __init__(self, name):
        # TODO: Inițializează atributele private _name și _health (100)
        pass

    def attack(self, boss):
        # TODO: Alegeți o valoare de damage (ex: 50) și reduceți sănătatea bossului folosind metoda boss.take_damage(damage)
        pass

    def get_health(self):
        # TODO: Returnează valoarea actuală a _health
        pass


class Boss:
    def __init__(self, name):
        # TODO: Inițializează atributele private _name și _health (500)
        pass

    def take_damage(self, amount):
        # TODO: Scade sănătatea bossului cu amount, asigurându-te că _health nu scade sub 0
        pass

    def is_defeated(self):
        # TODO: Returnează True dacă _health este 0, altfel False
        pass


# Exemplu de utilizare:
if __name__ == "__main__":
    player = Player("Hero")
    boss = Boss("Dark Lord")

    # Simularea unui atac
    player.attack(boss)
    print("Sănătatea bossului:", boss._health)  # Așteptat: 500 - damage_value

    # Verificați dacă bossul este învins după un atac
    if boss.is_defeated():
        print("Boss învins!")
    else:
        print("Bossul încă luptă!")


"""             HOMEWORK            """

# TODO   -Boss also takes player's damage each time he is attacked ( example: player damages boss -> boss takes damage -> boss damages back)
#        -Boss' damage is a random number between 1 and 10 (import random)
#        -Make the game run in a loop, until one of the players is defeated (for this, you will also need to implement player take damage and is defeated)