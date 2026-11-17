class Employe:
    def __init__(self, nom, salaire_base):
        self.nom = nom
        self.salaire_base = salaire_base

    def salaire_total(self):
        return self.salaire_base

    def __str__(self):
        return "{} gagne {} €".format(self.nom, self.salaire_total())


class Manager(Employe):
    def __init__(self, nom, salaire_base, prime):
        Employe.__init__(self, nom, salaire_base)
        self.prime = prime

    def salaire_total(self):
        return sum((self.salaire_base, self.prime))


class Developpeur(Employe):
    BONUS = {'Python': 500}
    BONUS_DEFAUT = 300

    def __init__(self, nom, salaire_base, technologie):
        Employe.__init__(self, nom, salaire_base)
        self.technologie = technologie

    def salaire_total(self):
        supplement = self.BONUS.get(self.technologie, self.BONUS_DEFAUT)
        return self.salaire_base + supplement


def main():
    equipe = [
        Employe("Alice", 2000),
        Manager("Bob", 2500, 800),
        Developpeur("Charlie", 2200, "Python"),
    ]
    for membre in equipe:
        print(membre)


if __name__ == '__main__':
    main()
