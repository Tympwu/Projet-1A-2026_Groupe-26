import matplotlib.pyplot as plt

from typing import Any
from abc import ABC


class Graphique(ABC):
    """
    Class qui regroupe les caractéristiques commune des graphiques

    Parameters
    ----------
    titre : str = ""
        Représente le titre du graphique
    data1 : list[Any] = []
        Représente la 1ère série de donnée
    data2 : list[Any] = []
        Représente la 2ème série de donnée
    """

    def __init__(
        self,
        titre: str = "",
        data1: list[Any] = [],
        data2: list[Any] = []
    ) -> None:
        if not isinstance(titre, str):
            raise TypeError("l'attribut titre doit être du type str")
        if not isinstance(data1, list):
            raise TypeError("l'attribut data1 doit être du type liste")
        if not isinstance(data2, list):
            raise TypeError("l'attribut data2 doit être du type liste")
        self.titre = titre
        self.data1 = data1
        self.data2 = data2

    def enregistrer_image(self, nom):
        """
        Fonction permettant d'enregristrer un graphique
        """
        plt.savefig(f"{nom}.png")
        print(f"Image enregistrée sous : {nom}.png")
