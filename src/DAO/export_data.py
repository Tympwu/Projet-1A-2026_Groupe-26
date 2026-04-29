# from ..Model.Coach import Coach
# from ..Model.Competition import Competition
from ..Model.Equipe import Equipe
from ..Model.match import Match
from ..Model.Player import Player
from ..Interface.Menu import Menu


class Export_data(Menu):
    def __init__(self):
        super().__init__()

    def add_data(self):

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

        print("\n--- Saisie des données ---")
        for attr, attr_type in used_attr.items():
            if attr in {"id", "id_match"}:
                continue
            while True:
                value = input(f"{attr} ({attr_type.__name__}) : ")
                converted = convert_value(value, attr_type)
                if converted is not None or value == "":
                    new_data[attr] = converted
                    break
                print("Type invalide, recommencez")

        print("\nDonnées créées :")
        print(new_data)
        return new_data

    def supprimer_data(self):
        pass

    def modifier_data(self):
        pass

    def export_data(self):
        pass
