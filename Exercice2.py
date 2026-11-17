class Document:
    def __init__(self, titre, annee):
        self.titre = titre
        self.annee = annee

    def afficher(self):
        print("{} ({})".format(self.titre, self.annee))


class Livre(Document):
    def __init__(self, titre, annee, auteur):
        Document.__init__(self, titre, annee)
        self.auteur = auteur

    def afficher(self):
        print("Livre: " + self.titre + " par " + self.auteur + " (" + str(self.annee) + ")")


class Magazine(Document):
    def __init__(self, titre, annee, numero):
        Document.__init__(self, titre, annee)
        self.numero = numero

    def afficher(self):
        print("Magazine: %s No. %s (%s)" % (self.titre, self.numero, self.annee))


def main():
    docs = [
        Livre("1984", 1949, "George Orwell"),
        Magazine("Science & Vie", 2023, 456),
        Livre("Le Petit Prince", 1943, "Antoine de Saint-Exupéry"),
    ]
    for d in docs:
        d.afficher()


main()
