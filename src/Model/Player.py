# from typing import Union
# from src.Common.utils import parse_boolean

# is_the_goat: Union[str, bool]


class Player:
    def __init__(self, id: int, full_name: str, sport: str, nb_jours_blesse: int, age: int, palmares: int = 0):
        self.id = id
        self.full_name = full_name
        # self.is_the_goat = parse_boolean(is_the_goat)
        self.palmares = palmares
        self.nb_jours_blesse = nb_jours_blesse
        self.age = age
        
    def __repr__(self):
        # display_string = self.full_name
        # if self.is_the_goat:
        # display_string += " (GOAT)"
        # return display_string
        return f"Nom:{self.full_name}, Id:{self.id}, Sport:{self.sport}"

    def __str__(self):
        return f"Le joueur {self.id} s'appelle {self.full_name} et se distingue en {self.sport}."

    def victoire_finale(self):
        self.palmares += 1
