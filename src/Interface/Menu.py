from typing import Callable
from abc import ABC
from ..Query.Parser import Parser


class Menu(ABC):
    """
    Classe générique englobant les méthodes nécessaires pour chacun des
    menus intéragissant avec l'utilisateur
    """
    def __init__(self, parser: Parser | None = None, sport: str | None = None):
        self.__admin: bool = False
        self.sport = sport
        self.__parser = None
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

    def initialize_parser(self, parser):
        """
        Permet d'initialiser globalement le parser et d'autres paramètres relatifs à ce dernier
        """
        self.parser = parser
        self.parser_match_name = {
            "Joueurs": self.parser.dict_player,
            "Matchs": self.parser.dict_matchs,
            "Équipes": self.parser.dict_equipe,
            "Coachs": self.parser.dict_coach
        }

    def answer_question(self, autorise_value: list):
        """
        Fonction permettant de traiter une réponse et de trier les premiers cas de mauvaises 
        réponses
        """
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
        print("\n0. Revenir en arrière\n\n")

    def menu_question(
        self, question: str, data: list[str],
        result_match: dict[int, Callable | str], break_on_call=True
    ):
        """
        Fonction permettant de demander une réponse parmis une liste d'éléments données

        Parameters
        ----------
        data : list[str]
            Paramètre contenant la liste des éléments à afficher
        question : str
            Question à poser à l'utilisateur
        result_match : dict[int, Callable]
            Dictionnaire permettant de lier le résultat à la fonction voulu correspondante
        break_on_call : bool
            Paramètre indiquant la nécessité de reposer la question à l'avenir ou pas

        Returns
        -------
        None | str
            Si le dictionnaire contient des fonctions, alors ces dernières sont appelés
            puis rien est renvoyé
            Sinon on renvoit le string correspondant à la réponse de l'utilisateur dans
            le dictionnaire
        """
        while True:
            print("-------------------------------------------")
            print(question)
            self.print_list(data)
            result = self.answer_question(result_match.keys())
            if result == 0:
                return 0
            elif result != -1:
                if callable(result_match[result]):
                    result_match[result]()
                    if break_on_call:
                        return
                else:
                    return result_match[result]
