# Exercițiul 1: Crearea clasei Animal
"""
# TODO Scrieți o clasă Python numită Animal cu următoarele specificații:

Atribute:
    name (șir de caractere)
    species (șir de caractere)
Metode:
    __init__: Inițializează atributele.
    speak: O metodă care afișează un mesaj generic, de exemplu "Animalul scoate un sunet."
Extindere:
    Creați o subclasă Dog care moștenește clasa Animal. Suprascrieți metoda speak pentru a afișa "Woof!" și adăugați o metodă suplimentară fetch care afișează "Adun mingea...".
"""


# Exercițiul 2: Crearea unei clase Car cu încapsulare

# TODO Scrieți o clasă Python numită Car care demonstrează încapsularea de bază:
"""
Atribute:
    make (șir de caractere)
    model (șir de caractere)
    _speed (număr întreg, atribut privat) - reprezintă viteza curentă (inițial 0)
Metode:
    __init__: Inițializează atributele și setează _speed la 0.
    accelerate: Crește viteza cu o valoare dată.
    brake: Scade viteza cu o valoare dată, asigurându-se că nu scade sub 0.
    get_speed: Returnează viteza curentă (metodă publică pentru accesarea atributului privat).
"""



# Exercițiul 3: Implementarea moștenirii cu o clasă Student

# TODO Creați o clasă de bază Student cu următoarele:
"""
Atribute:
    name (șir de caractere)
    student_id (număr întreg)
Metode:
    __init__: Inițializează atributele.
    get_details: Returnează un șir de caractere cu numele studentului și ID-ul.

Extindere:
    Creați o subclasă GraduateStudent care moștenește clasa Student și adaugă:
        thesis_topic (șir de caractere) - atribut suplimentar
        Suprascrieți metoda get_details pentru a include și tema tezei.
"""





# Exercițiul 4: Debugging - Găsește erorile din clasa următoare

# TODO Examinați codul de mai jos și identificați cel puțin trei erori. Corectați-le astfel încât codul să ruleze corect.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_info(self):
        print("Title: " + self.title)
        print("Author: " + self.author)

    def set_title(new_title):
        self.title = new_title

# Crează o instanță și încearcă să actualizezi titlul
my_book = Book("1984", "George Orwell")
my_book.set_title("Animal Farm")
my_book.get_info()

"""
Indicații:
    - Verificați parametrii metodelor (ex. lipsa lui self la set_title).
    - Observați modul corect de a defini metodele în interiorul unei clase.
    - Asigurați-vă că apelurile metodelor sunt efectuate pe obiectul corespunzător.
"""






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


#Boss Exercise

# TODO Scrieți o clasă Python numită Animal cu următoarele specificații:

"""
Cerințe:
1. Clasa Player:
    Atribute private:
        - _name: numele jucătorului (șir de caractere)
        - _health: sănătatea jucătorului (valoare între 0 și 100; inițial 100)
    Metode publice:
        - __init__(name): Inițializează atributele.
        - attack(boss): Execută un atac asupra obiectului boss. Alegeți o valoare de damage (de exemplu, 50) și reduce sănătatea bossului prin apelarea metodei take_damage a obiectului boss.
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
    print("Sănătatea bossului:", boss.health)  # Așteptat: 500 - damage_value

    # Verificați dacă bossul este învins după un atac
    if boss.is_defeated():
        print("Boss învins!")
    else:
        print("Bossul încă luptă!")


"""             HOMEWORK            """

# TODO   -Boss also takes player's damage each time he is attacked ( example: player damages boss -> boss takes damage -> boss damages back)
#        -Boss' damage is a random number between 1 and 10 (import random)
#        -Make the game run in a loop, until one of the players is defeated (for this, you will also need to implement player take damage and is defeated)