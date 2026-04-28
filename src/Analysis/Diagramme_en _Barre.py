import matplotlib.pyplot as plt
from typing import Any, Optional
from Graphique import Graphique

class Diagramme_en_Barre(Graphique):


    def __init__(
        self,
        titre: str = "",
        data1: list[Any] = [],
        data2: list[Any] = [],
        format_image: tuple[int, int] = (12, 7),  # format du graphique
        couleur: str = "red",
        valeur_par_defaut: int = 0
    ) -> None:

        super().__init__(titre, data1, data2)

        if not all(isinstance(x, (int, float)) for x in self.data1):
            raise TypeError("Les valeurs de data1 doivent être numériques.")
            
        self.data2 = [str(label) for label in data2]
        self.format_image = format_image
        self.couleur = couleur
        self.valeur_par_defaut = valeur_par_defaut

        self._equilibrer_donnees()

    def _equilibrer_donnees(self) -> None:
        """Méthode interne pour ajuster la taille des listes."""
        len1, len2 = len(self.data1), len(self.data2)
        # 1er cas: trop de donnée et pas assez de noms de colonnes: on ajoute des noms fictifs ("Sans nom")
        if len1 > len2:
            nb_manquant = len1 - len2
            nouveaux_labels = ["Sans nom" for i in range(nb_manquant)]
            self.data2.extend(nouveaux_labels)
        # 2ème cas: trop de  noms de colonne et pas assez de donnée: on comble les données avec la valeur par défaut
        elif len2 > len1:
            nb_manquant = len2 - len1
            self.data1.extend([self.valeur_par_defaut] * nb_manquant)


    def ajouter_donnee(self, valeur: float | int) -> None:
        if not isinstance(valeur, (int, float)):
            raise TypeError("La donnée ajoutée doit être numérique.")

        # On cherche s'il existe une valeur par défaut à remplacer
        if self.valeur_par_defaut in self.data1:
            index = self.data1.index(self.valeur_par_defaut)
            self.data1[index] = valeur
        else:
            # Sinon, on ajoute à la fin et on équilibre pour créer une colonne "Sans nom"
            self.data1.append(valeur)
            self._equilibrer_donnees()

    def ajouter_nom_colonne(self, nom: Any) -> None:
        nom_str = str(nom)
        # On cherche s'il existe un "Sans nom" à remplacer
        if "Sans nom" in self.data2:
            index = self.data2.index("Sans nom")
            self.data2[index] = nom_str
        else:
            # Sinon, on ajoute à la fin et on équilibre pour créer un 0
            self.data2.append(nom_str)
            self._equilibrer_donnees()

    def ajouter_nom_et_valeur(self, nom: str, valeur: float) -> None:
        if not isinstance(nom, str):
            raise TypeError("le nom de la colonne à ajouter doit être du type str")
        if not isinstance(valeur, (float, int)):
            raise TypeError("le nom de la colonne à ajouter doit être numérique")
        self.data1.append(valeur)
        self.data2.append(nom)

    def afficher_image(self) -> None:
        largeur, hauteur = self.format_image[0], self.format_image[1]
        plt.figure(figsize=(largeur, hauteur))
        
        plt.bar(self.data2, self.data1, color=self.couleur)
        plt.title(self.titre)
        
        # inclinaison des labels s'ils sont trop longs
        plt.xticks(rotation=45, ha='right')
        
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()  # Évite que les labels soient coupés au bord de l'image
        plt.show()
    
    def enregistrer_image(self, nom) -> None:
        plt.savefig(nom)


"""
# Bloc test
if __name__ == "__main__":

    mon_graph = Diagramme_en_Barre(
        titre="Test de mon Projet",
        data1=[50, 12, 88],
        data2=["Janvier"],
        couleur="skyblue"
    )

    print("Données après init (équilibrage auto) :", mon_graph.data2)

    # 2. Test des méthodes d'ajout manuel
    mon_graph.ajouter_nom_colonne("Février") # Remplace le 1er "Sans nom"
    mon_graph.ajouter_donnee(55)             # Ajoute une barre et un nouveau "Sans nom"
    mon_graph.ajouter_nom_colonne("Mars")    # Remplace le nouveau "Sans nom"
    mon_graph.ajouter_nom_et_valeur("Avril", -5)

    print("Données après ajouts manuels :", mon_graph.data2)
    print("Valeurs finales :", mon_graph.data1)

    # 3. Lancement de l'affichage
    mon_graph.afficher()
"""
