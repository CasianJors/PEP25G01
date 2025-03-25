class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def attack(self, boss):
        boss.take_damage(500)

    def get_health(self):
        return self.health


class Boss:
    def __init__(self, name):
        self.name = name
        self.health = 500

    def take_damage(self, amount):
        self.health -= amount

    def is_defeated(self):
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