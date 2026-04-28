from typing import Any, Callable

from ..Analysis.Graphique import Graphique
from ..Analysis.Diagramme_en_Barre import Diagramme_en_Barre


class Menu_Graphique():
    """
    Menu permettant de gérer l'affichage des graphiques et autre
    """
    def __init__(self, parser, sport):
        self.parser = parser
        self.sport = sport
        self.hist = Diagramme_en_Barre()

        # A mettre dans une classe générique pour les menus
        self.parser_match_name = {
            "Joueurs": self.parser.dict_player,
            "Matchs": self.parser.dict_matchs,
            "Équipes": self.parser.dict_equipe,
            "Coachs": self.parser.dict_coach
        }
        self.person_parameters_allowed_match = {
            "Joueurs": [
                "id", "first_name", "last_name", "full_name", "sexe", "pseudo", "equipe", "taille",
                "nationalite", "continent", "numero_maillot", "main_forte", "poids", "role"
                ],
            "Équipes": [
                "id", "nom_equipe", "nom_abrev", "nickname", "ville_equipe", "region_equipe",
                "pays_equipe", "continent_equipe", "ligue", "annee_fondation"
            ],
            "Matchs": [
                "id_match", "tourney_id", "region", "match_num", "best_of",
                "date_match", "temps_match", "stats_match"
            ]
        }

    def answer_question(self, autorise_value: list):
        result: str = input("Réponse : ")
        if result == "0":
            return 0
        elif not result.isnumeric():
            print("La valeur renseignée n'est pas valide")
            result = -1
        elif int(result) not in autorise_value:
            print("La valeur renseignée n'est pas correct")
            result = -1
        else:
            result = int(result)
        return result
    
    def list_attr(self, data: dict[str, classmethod], allowed_data: list[str]) -> list[str]:
        """
        Fonction permettant d'extraire l'entièreté des arguments d'une classe du dictionnaire
        Ces arguments doivent aussi être dans allowed_data
        """
        sample_data = next(iter(data.values()))
        filtered_attr = [
            k for k, v in sample_data.__dict__.items()
            if v is not None and k in allowed_data
        ]
        return filtered_attr
    
    def print_list(self, donnee: list[str]):
        """
        Fonction permettant d'afficher des suites d'éléments numérotées
        """
        for i, ele in enumerate(donnee, 1):
            print(f"{i}. {ele}")
        print("0. Revenir en arrière\n\n")

    def choose_data(self, question: str, data: list[str], result_match: dict[int, Callable], break_on_call = True):
        """
        Fonction permettant de demander une réponse parmis une liste d'éléments données

        Parameters
        ----------
        data: list[str]
            Paramètre contenant la liste des éléments à afficher
        question : str
            Question à poser à l'utilisateur
        result_match : dict[int, Callable]
            Dictionnaire permettant de lier le résultat à la fonction voulu correspondante
        break_on_call : bool
            Paramètre indiquant la nécessité de reposer la question à l'avenir ou pas
        """
        while True:
            print("-------------------------------------------")
            print(question)
            self.print_list(data)
            result = self.answer_question(result_match.keys())
            if result == 0:
                return
            elif result != -1:
                if callable(result_match[result]):
                    result_match[result]()
                    if break_on_call:
                        return
                else:
                    return result_match[result]




    
    def main_menu(self):
        """
        Fonction permettant de savoir quelles graphique présenter
        """
        while True:
            print("-------------------------------------------")
            print("Que voulez-vous voir ?")
            print("1. Histogramme")
            print("2. ")
            print("3. \n")
            print("0. Revenir en arrière\n\n")
            result = self.answer_question({0, 1, 2, 3})
            result_match = {
                1: self._menu_hist,
                2: print,
                3: print
            }
            if result == 0:
                return
            elif result != -1:
                result_match[result]()

    def _menu_hist(self):
        """
        Fonction permettant de représenter des histogrammes
        """
        first_data = self.choose_data(
            "Quelles variables voulez-vous en abscisse ?",
            ["Joueurs", "Équipes", "Matchs", "Coachs"],
            {1: "Joueurs", 2: "Équipes", 3: "Matchs", 4: "Coachs"},
        )
        data1 = self.list_attr(
            self.parser_match_name[first_data],
            self.person_parameters_allowed_match[first_data])
        data_dict1 = {i: ele for i, ele in enumerate(data1.keys(), 1)}
        first_data = self.choose_data(
            "Quelles variables voulez-vous en abscisse ?",
            data1,
            data_dict1
        )