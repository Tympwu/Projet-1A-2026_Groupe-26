import pandas as pd

from ..Model.Coach import Coach
from ..Model.Equipe import Equipe
from ..Model.Match import Match
from ..Model.Player import Player
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
        else:
            dao_wanted = self.dao[self.dao_match_name[self.sport][result]]
            list_attr = list(self.dao[self.dao_match_name[self.sport][result]].data.columns)

        # Éléments initiaux pour la création du nouvel élément
        new_element: dict[str, str | None] = {"sport": self.sport}
        new_element[list_attr[0]] = max(
            self.parser_match_name[result].keys(), default=0) + 1
        
        # Liste de questions pour remplir les données
        for attribut in list_attr[1:]:
            parameter = input(f"Valeur pour {attribut} :")
            new_element[attribut] = [parameter] if parameter is not None else None
        dao_wanted.inserer(new_element)
        # Là !!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.parser_function_match[result](pd.DataFrame(new_element), other=men_women)

    def add_data_bis(self):

        sport_sans_equipe = {"tennis"}

        options = {
            1: self.parser.dict_player,
            2: self.parser.dict_equipe,
            3: self.parser.dict_matchs
        }

        classes = {
            1: Player,
            2: Equipe,
            3: Match
        }

        classes_print = {
            1: "Joueur",
            2: "Equipe",
            3: "Match"
        }

        while True:

            print("-------------------------------------------")
            print("Que voulez-vous faire désormais ?")

            print("1. Ajouter des joueurs")

            if self.sport.lower() not in sport_sans_equipe:
                print("2. Ajouter des équipes")

            print("3. Ajouter des matchs")
            print("0. Revenir au menu principal\n")

            result = self.answer_question({0, 1, 2, 3})

            if result == 0:
                return

            data_dict = options[result]
            cls = classes[result]

            new_data = self.collect_input_data(data_dict, cls)
            instance = cls(**new_data)

            # stockage dynamique
            key = getattr(instance, "id", None) or getattr(instance, "id_match", None)

            data_dict[key] = instance
            self.data_added[classes_print[result].lower() + "s"].append(instance)

            print("\n" + str(classes_print[result]) + " créé :")
            print(instance)

    def collect_input_data(self, data_dict, cls):

        def convert_value(value, expected_type):
            if value == "":
                return None
            try:
                if expected_type is int:
                    return int(value)
                if expected_type is float:
                    return round(float(value), 2)
                if expected_type is str:
                    return value
                return value
            except ValueError:
                print(f"Valeur invalide pour type {expected_type.__name__}")
                return None

        sample = next(iter(data_dict.values()))
        annotations = cls.__annotations__
        used_attr = {
            attr: attr_type
            for attr, attr_type in annotations.items()
            if any(getattr(obj, attr, None) is not None for obj in data_dict.values())
        }
        attributes = list(sample.__dict__.keys())
        new_data = {}
        max_id = max(data_dict.keys(), default=0)
        if "id" in attributes:
            new_data["id"] = max_id + 1
        elif "id_match" in attributes:
            new_data["id_match"] = max_id + 1
        if "sport" in attributes:
            new_data["sport"] = self.sport

        print("\n--- Saisie des données ---")
        for attr, attr_type in used_attr.items():
            if attr in {"id", "id_match", "sport"}:
                continue
            while True:
                value = input(f"{attr} ({attr_type.__name__}) : ")
                converted = convert_value(value, attr_type)
                if converted is not None or value == "":
                    new_data[attr] = converted
                    break
                print("Type invalide, recommencez")
        return new_data

    def supprimer_data(self):
        pass

    def modifier_data(self):
        pass

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
"""            
    def __export_data(self, categorie):
        
        Fonction permettant d'exporter les données voulues de la catégorie demandée
        
        result = []
        for element in self.data_added[categorie]:
            result.append(
                {key: value for key, value in element.__dict__.items() if value is not None}
            )
        if result == []:
            print("Pas de nouvelles données, la base de donnée initiale a été renvoyée")
            if self.sport not in {"tennis", "volleyball"}:
                self.dao[self.dao_match_name[self.sport][categorie]].sauvegarde()
            else:
                for element in self.dao_match_name[self.sport][categorie]:
                    self.dao[element].sauvegarde()
        else:
            if self.sport not in {"tennis", "volleyball"}:
                self.dao[self.dao_match_name[self.sport][categorie]].inserer(result)
                self.dao[self.dao_match_name[self.sport][categorie]].sauvegarde()
            else:
                fuse_dao = glob_fuse_dao
                if not fuse_dao:
                    print(
                        "Les données initiales étaient séparés en 2 fichiers distincts," +
                        " le fichier sortant est la fusion des deux et des ajouts manuels")
                    global glob_fuse_dao
                    glob_fuse_dao = True
                    self.dao[self.dao_match_name[self.sport][categorie][0]].inserer(
                        self.dao[self.dao_match_name[self.sport][categorie][1]]
                    )
                self.dao[self.dao_match_name[self.sport][categorie][0]].inserer(result)
                self.dao[self.dao_match_name[self.sport][categorie][0]].sauvegarde()
"""