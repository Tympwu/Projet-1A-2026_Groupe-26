from abc import abstractmethod, ABC
import pandas as pd
from typing import Any

from ..Model.Player import Player


class Parser(ABC):
    def __init__(self, sport):
        self.sport = sport
        self.dict_player: dict[int, Player] = {}
        self.dict_matches: dict[int, Player] = {}
        self.dict_player: dict[int, Player] = {}
        self.dict_player: dict[int, Player] = {}

    def fetch_safety_data(self, data: Any, convert_to: type):
        try:
            return convert_to(data)
        except ValueError:
            return None

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
            dob = str(self.fetch_safety_data(row["dob"], int))
            dob = dob[:4] + "-" + dob[4:6] + "-" + dob[6:8]
            print(dob)
            player = Player(
                id=self.fetch_safety_data(row["player_id"], int),
                sexe="H",
                first_name=self.fetch_safety_data(row["name_first"], str),
                last_name=self.fetch_safety_data(row["name_last"], str),
                main_forte=self.fetch_safety_data(row["hand"], str),
                dob=dob,
                nationalite=self.fetch_safety_data(row["ioc"], str),
                taille=self.fetch_safety_data(row["height"], int),
                sport="Tennis")
            self.list_player[player.id] = player

    def parse_competition(self, data: pd.DataFrame):
        pass

    def parse_matches(self, data: pd.DataFrame):
        pass

    def parse_team(self, data: pd.DataFrame):
        pass
