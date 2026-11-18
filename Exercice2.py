class Document:
    """Document avec un titre et une année de publication."""

    def __init__(self, titre: str, annee: int) -> None:
        self.titre = titre
        self.annee = annee

    def afficher(self) -> None:
        print(f"{self.titre} ({self.annee})")


class Livre(Document):
    """Document écrit par un auteur."""

    def __init__(self, titre: str, annee: int, auteur: str) -> None:
        super().__init__(titre, annee)
        self.auteur = auteur

    def afficher(self) -> None:
        print(f"Livre: {self.titre} par {self.auteur} ({self.annee})")


class Magazine(Document):
    """Document identifié par un numéro d'édition."""

    def __init__(self, titre: str, annee: int, numero: int) -> None:
        super().__init__(titre, annee)
        self.numero = numero

    def afficher(self) -> None:
        print(f"Magazine: {self.titre} No. {self.numero} ({self.annee})")


def main() -> None:
    docs = [
        Livre("1984", 1949, "George Orwell"),
        Magazine("Science & Vie", 2023, 456),
        Livre("Le Petit Prince", 1943, "Antoine de Saint-Exupéry"),
    ]
    for doc in docs:
        doc.afficher()


if __name__ == "__main__":
    main()
