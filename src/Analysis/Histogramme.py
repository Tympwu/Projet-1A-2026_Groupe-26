import matplotlib.pyplot as plt
from typing import Any
from .Graphique import Graphique


class Histogramme(Graphique):


    def __init__(
        self, 
        titre: str = "",
        data1: list[Any] = [],
        data2: list[Any] = []
    ) -> None:
        if not all(isinstance(x, (int, float)) for x in self.data1):
            raise TypeError("Les valeurs de data1 doivent être numériques.")
            
        self.data2 = [str(label) for label in data2]

        # Vérification de la cohérence des tailles, chaque élément de data1 étant relier à un élément de data2
        if len(self.data1) != len(self.data2):
            raise ValueError("data1 (valeurs) et data2 (noms) doivent avoir la même longueur.")
        super().__init__(titre, data1, data2)

    def afficher(self) -> None:
        plt.figure(figsize=(12, 7))
        plt.bar(self.data2, self.data1, color='#4285F4')
        plt.title(self.titre)
        plt.grid(axis='y', linestyle='-', alpha=0.3)
        plt.show()