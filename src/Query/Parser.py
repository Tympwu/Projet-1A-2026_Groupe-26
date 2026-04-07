from abc import abstractmethod, ABC
import pandas as pd

from ..Model.Player import Player

class Parser(ABC):
    def __init__(self, sport):
        self.sport = sport

    @abstractmethod
    def parse_players(self, data):
        pass

    @abstractmethod
    def parse_matches(self, data):
        pass

    @abstractmethod
    def parse_competition(self, data):
        pass

    @abstractmethod
    def parse_team(self, data):
        pass


class Tennis_Parser(Parser):
    def __init__(self):
        super().__init__("tennis")

    def parse_players(self, data: pd.DataFrame):
        self.list_player = {}
        for index, row in data.iterrows():
            player = Player(
                int(row["player_id"]),
                first_name=row["name_first"],
                last_name=row["name_last"],
                main_forte=row["hand"],
                age=2026 - int(row["dob"][:3]),
                nationalite=row["ioc"],
                taille=row["height"])
            self.list_player[int(row["player_id"])] = player
