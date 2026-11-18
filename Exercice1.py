class Employe:
    """Employé avec un nom et un salaire de base."""

    def __init__(self, nom: str, salaire_base: float) -> None:
        self.nom = nom
        self.salaire_base = salaire_base

    def salaire_total(self) -> float:
        """Retourne le salaire total de l'employé."""
        return self.salaire_base

    def __str__(self) -> str:
        return f"{self.nom} gagne {self.salaire_total()} €"


class Manager(Employe):
    """Employé qui perçoit une prime en plus de son salaire de base."""

    def __init__(self, nom: str, salaire_base: float, prime: float) -> None:
        super().__init__(nom, salaire_base)
        self.prime = prime

    def salaire_total(self) -> float:
        return self.salaire_base + self.prime


class Developpeur(Employe):
    """Employé dont le bonus dépend de la technologie maîtrisée."""

    BONUS_PYTHON = 500
    BONUS_AUTRE = 300

    def __init__(self, nom: str, salaire_base: float, technologie: str) -> None:
        super().__init__(nom, salaire_base)
        self.technologie = technologie

    def salaire_total(self) -> float:
        bonus = self.BONUS_PYTHON if self.technologie == "Python" else self.BONUS_AUTRE
        return self.salaire_base + bonus


def main() -> None:
    personnes = [
        Employe("Alice", 2000),
        Manager("Bob", 2500, 800),
        Developpeur("Charlie", 2200, "Python"),
    ]
    for personne in personnes:
        print(personne)


if __name__ == "__main__":
    main()
