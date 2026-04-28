from typing import Any
from Gra
class Graphique():
    """
    Class qui regroupe les caractéristiques commune des graphiques

    attribut:
    titre: str = "" représente le titre du graphique
    data1: list[Any] = [] représente la 1ère série de donnée
    data2: list[Any] = [] représente la 2ème série de donnée
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

    def menu_graph(self):
        """
        Fonction permettant de savoir quelles données affichées entre joueurs, matchs et autre
        """
        while True:
            print("-------------------------------------------")
            print("Que voulez-vous voir ?")
            print("1. Les joueurs")
            print("2. Les équipes")
            print("3. Les matchs\n")
            print("0. Revenir en arrière\n\n")
            result = self.answer_question({0, 1, 2, 3})
            result_match = {
                1: self.menu_recherche_joueurs,
                2: self.menu_recherche_equipe,
                3: self.menu_recherche_match
            }
            if result == 0:
                return
            elif result != -1:
                if result == 2 and self.sport in {"tennis"}:
                    print("Il n'y a pas d'équipe dans ce sport")
                else:
                    result_match[result]()