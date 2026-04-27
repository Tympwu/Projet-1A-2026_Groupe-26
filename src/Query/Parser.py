from abc import abstractmethod, ABC
from typing import Any

from ..Model.Player import Player
from ..Model.match import Match
from ..Model.Equipe import Equipe
from ..Model.Coach import Coach
from ..Model.Competition import Competition

class Parser(ABC):
    def __init__(self, sport):
        self.sport = sport
        self.dict_player: dict[int, Player] = {}
        self.dict_matchs: dict[int, Match] = {}
        self.dict_equipe: dict[int|str, Equipe] = {}
        self.dict_coach: dict[int, Coach] = {}
        self.dict_competition: dict[int, Competition] = {}
        self.nan_find = False

    def fetch_safety_data(self, data: Any, convert_to: type):
        try:
            return convert_to(data)
        except ValueError:
            if not self.nan_find and data != "nan":
                self.nan_find = True
                print("Erreur de conversion de type, celui voulu est " + str(convert_to) + " et celui donné est " +str(type(data)))
                print("Des valeurs manquent à la table de données, certaines erreurs peuvent donc apparaître par la suite")
            return None

    @abstractmethod
    def parse_players(self, data, other: Any):
        pass

    @abstractmethod
    def parse_matchs(self, data, other: Any):
        pass

    @abstractmethod
    def parse_competition(self, data, other: Any):
        pass

    @abstractmethod
    def parse_equipes(self, data, other: Any):
        """
        Fonction permettant de récupérer les éléments des bases de données et de créer les classes
        correspondantes. Cette dernière est spécifique aux Équipes de Tennis
        """
        pass
