from typing import Any, Callable

from ..Analysis.Graphique import Graphique
from ..Analysis.Diagramme_en_Barre import Diagramme_en_Barre
from ..Interface.Menu import Menu


class Menu_Graphique(Menu):
    """
    Menu permettant de gérer l'affichage des graphiques et autre
    """
    def __init__(self):
        super().__init__()
        self.hist = Diagramme_en_Barre()
    
    def main_menu(self):
        """
        Fonction permettant de savoir quelles graphique présenter
        """
        self.menu_question(
            "Que voulez-vous voir ?",
            ["Histogramme", "", ""],
            {1: self._menu_hist, 2: print, 3: print}
        )

    def _menu_hist(self):
        """
        Fonction permettant de représenter des histogrammes
        """
        # Première variable
        first_data = self.menu_question(
            "Quelles variables voulez-vous en abscisse ?",
            ["Joueurs", "Équipes", "Matchs", "Coachs"],
            {1: "joueurs", 2: "equipes", 3: "matchs", 4: "coachs"},
        )
        data1 = self.list_attr(
            self.parser_match_name[first_data],
            self.parameters_allowed[first_data])
        data_dict1 = {i: ele for i, ele in enumerate(data1, 1)}
        var1 = self.menu_question(
            "Quelles variables voulez-vous en abscisse ?",
            data1,
            data_dict1
        )

        # Deuxième variable
        second_data = self.menu_question(
            "Quelles variables voulez-vous en ordonnée ?",
            ["Joueurs", "Équipes", "Matchs", "Coachs"],
            {1: "joueurs", 2: "equipes", 3: "matchs", 4: "coachs"},
        )
        data2 = self.list_attr(
            self.parser_match_name[second_data],
            self.parameters_allowed[second_data])
        data_dict2 = {i: ele for i, ele in enumerate(data2, 1)}
        var2 = self.menu_question(
            "Quelles variables voulez-vous en abscisse ?",
            data2,
            data_dict2
        )
        print(var1, var2)