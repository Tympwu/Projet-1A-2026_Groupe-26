from unidecode import unidecode
import pandas as pd


from ..Analysis.Diagramme_en_Barre import Diagramme_en_Barre
from ..Analysis.Nuage_de_points import Nuages_de_points
from .Menu import Menu


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
            ["Histogramme", "Nuage de points"],
            {1: self.menu_hist, 2: print}
        )

    def _menu_choix_var(
        self,
        constraint: tuple[set[str]] | list = [None, None, None, None]
    ) -> tuple[list, list]:
        """
        Fonction permettant de choisir des variables pour une représentation

        Parameters
        ----------
        constraint : tuple[set[str]] | list
            Tuple d'ensemble contenant de potentielles contraintes de
            paramètres pour le choix de l'utilisateur
        """
        # Première variable
        question0 = {"Joueurs", "Équipes", "Matchs", "Coachs"}
        if constraint[0] is None:
            constraint[0] = question0
        question0 = list(question0 & constraint[0])
        first_data = self.menu_question(
            "Quelles variables voulez-vous en ordonnée ?",
            question0,
            {i: unidecode(ele.lower()) for i, ele in enumerate(question0, 1)},
        )
        if first_data == 0:
            return 0, 0

        data1 = self.list_attr(
            self.parser_match_name[first_data],
            self.parameters_allowed[first_data])
        if constraint[1] is None:
            constraint[1] = data1
        question1 = list(set(data1) & constraint[1])
        data_dict1 = {i: ele for i, ele in enumerate(question1, 1)}
        var1 = self.menu_question(
            "Quelles variables voulez-vous en ordonnée ?",
            question1,
            data_dict1
        )
        if var1 == 0:
            return 0, 0

        # Deuxième variable
        question2 = {"Joueurs", "Équipes", "Matchs", "Coachs"}
        if constraint[2] is None:
            constraint[2] = question2
        question2 = list(question2 & constraint[2])
        second_data = self.menu_question(
            "Quelles variables voulez-vous en abscisse ?",
            question2,
            {i: unidecode(ele.lower()) for i, ele in enumerate(question2, 1)}
        )
        if second_data == 0:
            return 0, 0
        data2 = self.list_attr(
            self.parser_match_name[second_data],
            self.parameters_allowed[second_data])
        if constraint[3] is None:
            constraint[3] = set(data2)
        question3 = list(set(data2) & constraint[3])
        data_dict2 = {i: ele for i, ele in enumerate(question3, 1)}
        var2 = self.menu_question(
            "Quelles variables voulez-vous en abscisse ?",
            question3,
            data_dict2
        )
        if var2 == 0:
            return 0, 0

        value1 = []
        value2 = []
        for element1, element2 in zip(
            self.parser_match_name[first_data].values(),
            self.parser_match_name[second_data].values()
        ):
            value1.append(element1.__dict__[var1])
            value2.append(element2.__dict__[var2])
        return value1, value2

    def menu_hist(self):
        value1_temp, value2_temp = self._menu_choix_var([
            self.data_available[self.sport],
            self.numeric_parameters,
            self.data_available[self.sport],
            None
        ])
        if value1_temp == value2_temp == 0:
            return 0
        value = [[element1, element2] for element1, element2 in zip(value1_temp, value2_temp)]
        value = pd.DataFrame(value, columns=["first_value", "second_value"])
        value = value.groupby(['second_value']).mean()
        titre = input("Quelle titre voulez-vous donnez à votre histogramme ?\nRéponse: ")
        self.hist = Diagramme_en_Barre(
            data1=list(value["first_value"]), data2=list(value.index), titre=titre
        )
        self.hist.afficher_image()
        if self.menu_question(
            "Voulez-vous enregistrer ce graphique ?",
            ["oui", "non"],
            {1: True, 2: False}
        ):
            titre_fichier = input("Quelle titre voulez-vous donner au fichier ?\nRéponse: ")
            self.hist.enregistrer_image(titre_fichier)
