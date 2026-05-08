import pandas as pd

from ..Menus.Menu import Menu
from .Interaction import DAO

global glob_fuse_dao
glob_fuse_dao = False


class Export_data(Menu):
    def __init__(self, loader):
        super().__init__()
        self.dao: dict[str, DAO] = loader.dao
        self.data_added: dict[classmethod, list[classmethod]] = {
            "joueurs": [],
            "equipes": [],
            "matchs": [],
            "coachs": []
        }
        self.dao_match_name = {
            "basketball": {
                "equipes": "team", "joueurs": "player", "matchs": "game"
            },
            "football_european_leagues": {
                "matchs": "match", "joueurs": "player", "equipes": "equipe"
                # "pays": "country", "league": "competition"
            },
            "league_of_legends": {
                "equipes": "team", "joueurs": "player", "matchs": "match", "coach": "coach"
            },
            "tennis": {
                "matchs": ["atp_matches_2024", "wta_matches_2024"],
                "joueurs": ["atp_players_2024", "wta_players_2024"]
            },
            "volleyball": {
                # "pays": "country",
                "coachs": ["coach_men", "coach_women"],
                "matchs": ["match_men", "match_women"],
                "joueurs": ["player_men", "player_women"]
            }
        }
        self.parser_function_match = {
            "joueurs": self.parser.parse_players,
            "equipes": self.parser.parse_equipes,
            "matchs": self.parser.parse_matchs,
            "coachs": self.parser.parse_coachs
        }

    def add_data(self):
        """
        Fonction permettant d'ajouter des données dans la base de données
        """
        # Première question pour déterminer dans quelle catégorie ajouter des informations
        possible_answer = [
            "Ajouter des " + element.lower() for element in self.data_available[self.sport]
        ]
        dict_answer = {
            i: element.lower() for i, element in enumerate(self.data_available[self.sport], 1)
        }
        result = self.menu_question(
            "Quelle donnée voulez-vous ajouter ?",
            possible_answer,
            dict_answer
        )
        if result == 0:
            return

        # Disjonction de cas afin de prévoir les sports séparés en fonction du sexe
        men_women = None
        if isinstance(self.dao_match_name[self.sport][result], list):
            men_women = self.menu_question(
                f"Le {self.sport} est divisé en catégorie femme et homme\n" +
                "Dans laquelle voulez-vous ajouter des données ?",
                ["Homme", "Femme"],
                {1: 1, 2: 2},
                break_on_call=True
            )
            if men_women == 0:
                return 0
            else:
                men_women -= 1
                dao_wanted = self.dao[self.dao_match_name[self.sport][result][men_women]]
                list_attr = list(
                    self.dao[self.dao_match_name[self.sport][result][men_women]].data.columns)
                # Changement pour correspondre dans la suite
                men_women = "H" if men_women == 0 else "F"
        else:
            dao_wanted = self.dao[self.dao_match_name[self.sport][result]]
            list_attr = list(self.dao[self.dao_match_name[self.sport][result]].data.columns)

        # Éléments initiaux pour la création du nouvel élément
        new_element: dict[str, str | None] = {}
        if "id" in list_attr[0]:
            new_element[list_attr[0]] = max(
                self.parser_match_name[result].keys(), default=0) + 1
            list_attr = list_attr[1:]

        # Liste de questions pour remplir les données
        for attribut in list_attr:
            parameter = input(f"Valeur pour {attribut} (Exemple : {dao_wanted.data[attribut][0]}):")
            new_element[attribut] = [parameter] if parameter is not None else None
        try:
            self.parser_function_match[result](pd.DataFrame(new_element), other=men_women)
            dao_wanted.inserer(new_element)
            print("Élément crée avec succès")
        except (ValueError, IndexError):
            print(
                "Certains valeurs renseignées n'étaient pas du bon type ou format," +
                " l'ajout n'as pas pu se faire")
        except KeyError:
            print(
                "L'une des id renseigné n'est pas valide, merci de renseigner une id déjà" +
                " existante ou de créer l'élement voulu d'abord")

    def menu_export_data(self):
        """
        Menu initial pour choisir quelle donnée exporter
        """
        # Création des paramètres permettant de poser la question correspondante au sport choisi
        possibility_answer = ["Les " + element for element in self.data_available[self.sport]]
        possibility_answer.append("Tout")
        dict_answer = {i: ele.lower() for i, ele in enumerate(self.data_available[self.sport], 1)}
        dict_answer[len(dict_answer)+1] = "Tout"

        result = self.menu_question(
            "Quelles données voulez-vous exporter ?",
            possibility_answer,
            dict_answer
        )
        if result == 0:
            return 0
        elif result == "Tout":
            for ele in self.data_available[self.sport]:
                print("-------------------------------------------")
                print(f"Fichier {ele} :")
                self.__export_data(ele.lower())
        else:
            self.__export_data(result)

    def __export_data(self, categorie):
        """
        Fonction permettant d'exporter les données voulues de la catégorie demandée
        """
        # Cas d'un sport séparé en fonction du sexe
        if isinstance(self.dao_match_name[self.sport][categorie], list):
            men_women = self.menu_question(
                f"Le {self.sport} est divisé en catégorie femme et homme\n" +
                "Dans laquelle voulez-vous ajouter des données ?",
                ["Homme", "Femme"],
                {1: 1, 2: 2},
                break_on_call=True
            )
            if men_women == 0:
                return 0
            else:
                men_women -= 1
                # Exportation des données
                self.dao[self.dao_match_name[self.sport][categorie][men_women]].sauvegarde()
        else:
            # Exportation des données
            self.dao[self.dao_match_name[self.sport][categorie]].sauvegarde()
        print("Exportation effectuée !\n\n")
