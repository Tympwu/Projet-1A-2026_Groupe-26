import matplotlib.pyplot as plt
from typing import Any
from .Graphique import Graphique


class Nuages_de_points(Graphique):

    def __init__(
        self,
        titre: str = "",
        data1: list[Any] = [],
        data2: list[Any] = [],
        format_image: tuple[int, int] = (12, 7),  # format du graphique
        couleur: str = "red",
        taille_point: int = 50,
        translucidite_point: float = 1,
        nom_axe1: str = "Axe 1",
        nom_axe2: str = "Axe 2"
    ) -> None:
        super().__init__(titre, data1, data2)
        if not all(isinstance(x, (int, float)) for x in self.data1):
            raise TypeError("Les valeurs de data1 doivent être numériques.")
        if not all(isinstance(x, (int, float)) for x in self.data2):
            raise TypeError("Les valeurs de data2 doivent être numériques.")
        if len(data1) != len(data2):
            raise ValueError("les listes data1 et data2 doivent avoir le même nombre d'éléments")
        self.format_image = format_image
        self.couleur = couleur
        self.nom_axe1 = nom_axe1
        self.nom_axe2 = nom_axe2
        self.taille_point = taille_point
        self.translucidite_point = translucidite_point

    def ajouter_point(self, point: list) -> None:
        if not isinstance(point, list):
            raise ValueError("l'attribut point doit être une liste")
        if len(point) != 2:
            raise ValueError("l'attribut point doit être une liste de longeur 2")
        if not isinstance(point[0], (float, int)) or not isinstance(point[1], (float, int)):
            raise TypeError("les éléments de point doivent être du type numérique")
        self.data1.append(point[0])
        self.data2.append(point[1])

    def changement_esthetique(
        self,
        translucidite: float | None = None,
        taille_point: float | None = None,
        nom_axe1: str | None = None,
        nom_axe2: str | None = None,
        titre: str | None = None,
        format_image: tuple[int, int] | None = None,
        couleur: str | None = None
    ) -> None:
        if (translucidite is not None) and (translucidite >= 0) and (translucidite <= 1):
            self.translucidite_point = translucidite
        if isinstance(taille_point, (float, int)) and taille_point > 0:
            self.taille_point = taille_point
        if isinstance(nom_axe1, str):
            self.nom_axe1 = nom_axe1
        if isinstance(nom_axe2, str):
            self.nom_axe1 = nom_axe2
        if isinstance(titre, str):
            self.titre = titre
        if isinstance(format_image, tuple) and (
            len(format_image) == 2
        ) and format_image[0] > 0 and format_image[1] > 0:
            self.format_image = format_image
        if isinstance(couleur, str):
            self.couleur = couleur

    def enregistrer_image(self, nom: str) -> None:
        if not isinstance(nom, str):
            raise TypeError("L'attribut nom doit être du type str")

        plt.figure(figsize=self.format_image)

        # Création du nuage de points
        plt.scatter(
            self.data1, self.data2, color=self.couleur, s=self.taille_point, marker='o',
            alpha=self.translucidite_point
        )

        # Titres et labels
        plt.title(self.titre)
        plt.xlabel(self.nom_axe1)
        plt.ylabel(self.nom_axe2)

        plt.grid(True, linestyle='--', alpha=1)
        plt.tight_layout()

        # CRITIQUE : On enregistre AVANT de montrer
        plt.savefig(f"{nom}.png")
        print(f"Image enregistrée sous : {nom}.png")

        # Affichage (pour Onyxia, utilise la fenêtre interactive si possible)
        plt.show()


"""
# Bloc test
if __name__ == "__main__":

    mon_graph = Nuages_de_points(
        titre="Test nuage de point",
        data1=[1, 2, 3, 4, 5],
        data2=[10, -20, 30.5, -40, 50],
        couleur="red",
        nom_axe1= "toto"
    )

    print("Données après init (axe 1 puis axe 2):\n", mon_graph.data1, mon_graph.data2)

    # 2. Test des méthodes d'ajout manuel
    mon_graph.ajouter_point([-10, -20])

    print("Données après ajouts manuels (axe 1 puis axe 2) :\n", mon_graph.data2, mon_graph.data2)


    # 3. Lancement de l'affichage
    mon_graph.enregistrer_image("test nuage de point")
"""
