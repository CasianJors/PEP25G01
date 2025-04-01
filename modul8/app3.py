class Angajat:
    def __init__(self, nume, salariu, departament):
        self.departament = departament
        self.salariu = salariu
        self.nume = nume

    def crestere_salariu(self, procent):
        self.salariu = self.salariu * (100 + procent) / 100

    def __str__(self):
        return f"Nume: {self.nume}, Salariu: {self.salariu}, Departament: {self.departament}"

    def __repr__(self):
        return f"Nume: {self.nume}, Salariu: {self.salariu}, Departament: {self.departament}"

class Angajati:
    lista_angajati = []

    @classmethod
    def adauga_angajati(cls, *args):
        cls.lista_angajati.extend([x for x in args])

    def detalii(self):
        for angajat in self.lista_angajati:
            print(angajat)

    def departament(self, dep):
        return list(filter(lambda ang: ang.departament == dep, self.lista_angajati))

    def creste_sal(self, procent, dep):
        lista_ang_din_dep = self.departament(dep)
        list(map(lambda ang: ang.crestere_salariu(procent), lista_ang_din_dep))
        print([angajat for angajat in self.lista_angajati])

hr = Angajati()

hr.adauga_angajati(
    Angajat("George", 1000, "HR"),
    Angajat("Andreea", 1500, "HR"),
    Angajat("Alex", 2000, 'instalator'),
    Angajat("Ionel", 5000, 'bossu'),
)

# hr.departament("HR")
hr.creste_sal(10, 'HR')