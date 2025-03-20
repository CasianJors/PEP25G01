# Boss Exercise

# TODO Scrieți o clasă Python numită Animal cu următoarele specificații:

"""
Cerințe:
1. Clasa Player:
    Atribute private:
        - _name: numele jucătorului (șir de caractere)
        - _health: sănătatea jucătorului (valoare între 0 și 100; inițial 100)
    Metode publice:
        - __init__(name): Inițializează atributele.
        - attack(boss): Execută un atac asupra obiectului boss. Alegeți o valoare de damage (de exemplu, 50) și reduce sănătatea bossului prin
        apelarea metodei take_damage a obiectului boss.
        - get_health(): Returnează valoarea curentă a _health.

2. Clasa Boss:
    Atribute private:
        - _name: numele bossului (șir de caractere)
        - _health: sănătatea bossului (valoare între 0 și 500; inițial 500)
    Metode publice:
        - __init__(name): Inițializează atributele.
        - take_damage(amount): Scade sănătatea bossului cu amount, asigurându-se că nu scade sub 0.
        - is_defeated(): Returnează True dacă _health este 0, altfel False.
"""


class Player:
    def __init__(self, name):
        # TODO: Inițializează atributele private _name și _health (100)
        self.name = name
        self.health = 100

    def attack(self, boss):
        # TODO: Alegeți o valoare de damage (ex: 50) și reduceți sănătatea bossului folosind metoda boss.take_damage(damage)
        boss.take_damage(500)

    def get_health(self):
        # TODO: Returnează valoarea actuală a _health
        return self.health


class Boss:
    def __init__(self, name):
        # TODO: Inițializează atributele private _name și _health (500)
        self.name = name
        self.health = 500

    def take_damage(self, amount):
        # TODO: Scade sănătatea bossului cu amount, asigurându-te că _health nu scade sub 0
        self.health -= amount

    def is_defeated(self):
        # TODO: Returnează True dacă _health este 0, altfel False
        if self.health <= 0:
            return True
        else:
            return False


# Exemplu de utilizare:
if __name__ == "__main__":
    player = Player("Hero")
    boss = Boss("Dark Lord")

    # Simularea unui atac
    player.attack(boss)
    print("Sănătatea bossului:", boss.health)  # Așteptat: 500 - damage_value

    # Verificați dacă bossul este învins după un atac
    if boss.is_defeated():
        print("Boss învins!")
    else:
        print("Bossul încă luptă!")