from abc import abstractmethod, ABC
import pandas as pd
from typing import Any

from ..Model.Player import Player
from ..Model.match import Match
from ..Model.Equipe import Equipe
from ..Model.Coach import Coach


class Parser(ABC):
    def __init__(self, sport):
        self.sport = sport
        self.dict_player: dict[int, Player] = {}
        self.dict_matches: dict[int, Match] = {}
        self.dict_equipe: dict[int, Equipe] = {}
        self.dict_coach: dict[int, Coach] = {}

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

    def parse_players(self, data: pd.DataFrame, sexe: str):
        """
        Fonction permettant de récupérer les éléments des bases de données et de créer les classes correspondantes

        """
        for index, row in data.iterrows():
            dob = str(self.fetch_safety_data(row["dob"], int))
            dob = dob[:4] + "-" + dob[4:6] + "-" + dob[6:8]
            print(dob)
            player = Player(
                id=self.fetch_safety_data(row["player_id"], int),
                sexe=sexe,
                first_name=self.fetch_safety_data(row["name_first"], str),
                last_name=self.fetch_safety_data(row["name_last"], str),
                main_forte=self.fetch_safety_data(row["hand"], str),
                dob=dob,
                nationalite=self.fetch_safety_data(row["ioc"], str),
                taille=self.fetch_safety_data(row["height"], int),
                sport="Tennis")
            self.dict_player[player.id] = player

    def parse_competition(self, data: pd.DataFrame):
        pass

    def parse_matches(self, data: pd.DataFrame):
        pass

    def parse_team(self, data: pd.DataFrame):
        pass


class Badminton_Parser(Parser):
    def __init__(self):
        super().__init__("badminton")
    
    def parse_players(self, data: pd.DataFrame):
        self.list_player = {}
        # --- Fetch full name and continent ---
        full_name = self.fetch_safety_data(row["name_full"], str).strip()
        continent = self.fetch_safety_data(row["continent"], str).strip()

        # --- Split the name into parts ---
        parts = full_name.split()

        # --- Determine first_name and last_name according to continent ---
        if continent.lower() == "africa":
            first_name = parts[0]
            last_name = " ".join(parts[1:])  # everything else
        else:
            first_name = " ".join(parts[:-1])  # all but last
            last_name = parts[-1]              # last word
        for index, row in data.iterrows():
            player = Player(
                id=index,
                first_name=first_name,
                last_name=last_name,
                nationalite=self.fetch_safety_data(row["country"], str),
                continent = self.fetch_safety_data(row["continent"], str),
                sport="badminton")
            self.list_player[player.id] = player

    def parse_competition(self, data: pd.DataFrame):
        pass

    def parse_matches(self, data: pd.DataFrame):
        pass


    



class Volleyball_Parser(Parser):

class League_of_legend_Parser(Parser):

class Basketball_Parser(Parser):


class Football_Parser(Parser): 
    def __init__(self):
        super().__init__("football")

    def parse_players(self, data: pd.DataFrame):
        self.list_player = {}
        for index, row in data.iterrows():
            dob = str(self.fetch_safety_data(row["birthday"], int))
            dob = dob[:4] + "-" + dob[4:6] + "-" + dob[6:8]
            print(dob)
            player = Player(
                id=self.fetch_safety_data(row["player_api_id"], int),
                full_name=self.fetch_safety_data(row["player_name"], str),
                dob=dob,
                taille=self.fetch_safety_data(row["height (cm)"], int),
                poid=self.fetch_safety_data(row["weight (kg)"], int),
                sport="Football")
            self.list_player[player.id] = player

    def parse_competition(self, data: pd.DataFrame):
        pass

    def parse_matches(self, data: pd.DataFrame):
        pass

    def parse_team(self, data: pd.DataFrame):
        pass