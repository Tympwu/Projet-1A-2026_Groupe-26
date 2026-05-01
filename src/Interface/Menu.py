from typing import Callable
from abc import ABC

global glob_parser, glob_sport, glob_dao
glob_parser = None
glob_sport = None
glob_dao = None


class Menu(ABC):
    """
    Classe générique englobant les méthodes nécessaires pour chacun des
    menus intéragissant avec l'utilisateur
    """
    def __init__(self):
        self.admin: bool = False
        if glob_sport is not None:
            self.sport = glob_sport
        else:
            self.sport = None
        self._sports: dict[int, str] = {
            1: "basketball",
            2: "football_european_leagues",
            3: "tennis",
            4: "league_of_legends",
            5: "volleyball",
            6: "Badminton"}
        if glob_parser is not None:
            self.parser = glob_parser
            self.parser_match_name = {
                "joueurs": self.parser.dict_player,
                "matchs": self.parser.dict_matchs,
                "equipes": self.parser.dict_equipe,
                "coachs": self.parser.dict_coach
            }
            self.__search = glob_dao
        else:
            self.parser = None
        self.parameters_allowed = {
            "joueurs": [
                "id", "first_name", "last_name", "full_name", "sexe", "pseudo", "equipe", "taille",
                "nationalite", "continent", "numero_maillot", "main_forte", "poids", "role"
                ],
            "equipes": [
                "id", "nom_equipe", "nom_abrev", "nickname", "ville_equipe", "region_equipe",
                "pays_equipe", "continent_equipe", "ligue", "annee_fondation"
            ],
            "matchs": [
                "id_match", "tourney_id", "region", "match_num", "best_of",
                "date_match", "temps_match"  # , "stats_match"
            ]
        }
        self.numeric_parameters = {
            "id", "taille", "numero_maillot", "poids", "id_match",
            "tourney_id", "match_num", "best_of", "temps_match"
        }
        self.data_available = {
            "basketball": {
                "Équipes", "Joueurs", "Matchs"
            },
            "football_european_leagues": {
                "Équipes", "Joueurs", "Matchs"
            },
            "tennis": {
                "Joueurs", "Matchs"
            },
            "volleyball": {

            },
            "league_of_legends": {
                "Équipes", "Joueurs", "Coachs", "Matchs"
            }
        }

    @property
    def search(self):
        return self.__search

    def initialize_parser(self, parser, sport, dao):
        """
        Permet d'initialiser globalement le parser et d'autres paramètres relatifs à ce dernier
        """
        global glob_parser, glob_sport, glob_dao
        glob_parser = parser
        glob_sport = sport
        glob_dao = dao
        self.__search = dao
        self.parser = parser
        self.parser_match_name = {
            "joueurs": self.parser.dict_player,
            "matchs": self.parser.dict_matchs,
            "equipes": self.parser.dict_equipe,
            "coachs": self.parser.dict_coach
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
        result_match: dict[int, Callable | str] | None, break_on_call=False
    ):
        """
        Fonction permettant de créer et gérer une interface avec l'utilisateur pour une question
        précise

        Parameters
        ----------
        question : str
            Question à poser à l'utilisateur
        data : list[str]
            Liste contenant les éléments à afficher dans l'ordre voulu, cet ordre aura un impact
            pour result_match
        result_match : dict[int, Callable | str]
            Dictionnaire permettant de lier le résultat donné par l'utilisateur (1, 2, 3...) à
            la fonction voulu correspondante ou à la valeur voulu qui sera renvoyée.
            Le dictionnaire est de la forme : {1 : réponse_1, 2 : réponse_2, ...}.
            Si les valeurs sont des fonctions, ces dernières seront appelées directement,
            Si ce sont des strings ils seront renvoyées.

            Si ce paramètre est à None, un dictionnaire du type {1: 1, 2: 2, ...} sera crée
        break_on_call : bool = False
            Définit si la boucle while continue de tourner après l'appel au résultat i.e.
            Si c'est un menu "étape" donc si l'on doit proposer de nouveau ce choix si
            l'utilisateur décide de revenir en arrière

        Returns
        -------
        None | str
            Si le dictionnaire contient des fonctions, alors ces dernières sont appelés
            puis rien est renvoyé
            Sinon on renvoit le string correspondant à la réponse de l'utilisateur dans
            le dictionnaire
        """
        if result_match is None:
            result_match = {i: i for i in range(len(data)+1)}
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
