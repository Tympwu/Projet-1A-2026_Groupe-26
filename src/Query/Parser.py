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
            type(data)
            return None

    @abstractmethod
    def parse_players(self, data, other=None):
        pass

    @abstractmethod
    def parse_matches(self, data, other=None):
        pass

    @abstractmethod
    def parse_competition(self, data, other=None):
        pass

    @abstractmethod
    def parse_team(self, data, other=None):
        pass


class Tennis_Parser(Parser):
    def __init__(self):
        super().__init__("tennis")

    def parse_players(self, data: pd.DataFrame, other: str):
        """
        Fonction permettant de récupérer les éléments des bases de données et de créer les classes
        correspondantes. Cette dernière est spécifique aux joueurs de Tennis
        """
        for index, row in data.iterrows():
            dob = str(self.fetch_safety_data(row["dob"], int))
            dob = dob[:4] + "-" + dob[4:6] + "-" + dob[6:8]
            print(dob)
            player = Player(
                id=self.fetch_safety_data(row["player_id"], int),
                sexe=other,
                first_name=self.fetch_safety_data(row["name_first"], str),
                last_name=self.fetch_safety_data(row["name_last"], str),
                main_forte=self.fetch_safety_data(row["hand"], str),
                dob=dob,
                nationalite=self.fetch_safety_data(row["ioc"], str),
                taille=self.fetch_safety_data(row["height"], int),
                sport="Tennis")
            self.dict_player[player.id] = player

    def parse_competition(self, data: pd.DataFrame, other=None):
        """
        Fonction permettant de récupérer les éléments des bases de données et de créer les classes
        correspondantes. Cette dernière est spécifique aux compétitions de Tennis
        """
        pass

    def parse_matches(self, data: pd.DataFrame, other=None):
        """
        Fonction permettant de récupérer les éléments des bases de données et de créer les classes
        correspondantes. Cette dernière est spécifique aux Équipes de Tennis
        """
        pass


class Badminton_Parser(Parser):
    def __init__(self):
        super().__init__("badminton")
    
    def parse_players(self, data: pd.DataFrame, other=None):
        for index, row in data.iterrows():
            full_name = self.fetch_safety_data(row["name"], str).strip()
            continent = self.fetch_safety_data(row["continent"], str).strip()
            parts = full_name.split()
            if continent.lower() == "africa":
                first_name = parts[0]
                last_name = " ".join(parts[1:])
            else:
                first_name = " ".join(parts[:-1])
                last_name = parts[-1]
            player = Player(
                id=index,
                first_name=first_name,
                last_name=last_name,
                nationalite=self.fetch_safety_data(row["country"], str),
                continent = self.fetch_safety_data(row["continent"], str),
                sport="badminton")
            self.dict_player[player.id] = player

    def parse_competition(self, data: pd.DataFrame):
        pass

    def parse_matches(self, data: pd.DataFrame):
        pass


    



class Volleyball_Parser(Parser):
    def __init__(self):
        super().__init__("volleyball")

    def parse_players(self, data: pd.DataFrame):
        self.list_player = {}
        for index, row in data.iterrows():
            player = Player(
                sexe="H",
                full_name=self.fetch_safety_data(row["name"], str),
                pseudo=self.fetch_safety_data(row["nickname"], str),
                lieu_naissance=self.fetch_safety_data(row["birth_place"], str),
                dob=str(self.fetch_safety_data(row["birthdate"], int)),
                nationalite=self.fetch_safety_data(row["country_code"], str),
                taille=self.fetch_safety_data(row["height"], int),
                sport="Volleyball")
            self.list_player[player.id] = player



class League_of_legend_Parser(Parser):


class Basketball_Parser(Parser):
    def __init__(self):
        super().__init__("tennis")

    def parse_players(self, data: pd.DataFrame, other=None):
        for index, row in data.iterrows():
            dob = str(self.fetch_safety_data(row["birthdate"], int))
            if len(dob) != 10:
                dob = dob[:9] + "0"
                print(dob)
            taille=self.fetch_safety_data(row["height"], str)
            taille1=int(taille[0])
            taille2=int(taille[2:])
            taille=30,48*taille1 + 2,54*taille2
            poids=self.fetch_safety_data(row["weight"], int)
            poids=0,454*poids
            player = Player(
                id=self.fetch_safety_data(row["person_id"], int),
                first_name=self.fetch_safety_data(row["first_name"], str),
                last_name=self.fetch_safety_data(row["last_name"], str),
                numero_maillot=self.fetch_safety_data(row["jersey"], int),
                dob=dob,
                role=self.fetch_safety_data(row["position"], str),
                taille=taille,
                poids=poids,
                equipe=dict_equipe[self.fetch_safety_data(row["team_id"], int)],
                sport="Basketball")
            self.dict_player_player[player.id] = player

class Football_Parser(Parser):
    def __init__(self):
        super().__init__("football")

    def parse_players(self, data: pd.DataFrame):
        for index, row in data.iterrows():
            player = Player(
                id=self.fetch_safety_data(row["player_api_id"], int),
                full_name=self.fetch_safety_data(row["player_name"], str),
                dob=self.fetch_safety_data(row["birthday"], str),
                taille=self.fetch_safety_data(row["height (cm)"], int),
                poids=self.fetch_safety_data(row["weight (kg)"], int),
                sport="Football")
            self.dict_player[player.id] = player

    def parse_team(self, data: pd.DataFrame):
        for index, row in data.iterrows():
            equipe = Equipe(
                id=self.fetch_safety_data(row["team_api_id"], int),
                nom_equipe=self.fetch_safety_data(row["team_long_name"], str),
                nom_abrev=self.fetch_safety_data(row["team_short_name"], str)
                )
            self.dict_equipe[equipe.id] = equipe

    def parse_competition(self, data: pd.DataFrame):
        pass

    def parse_matches(self, data: pd.DataFrame):
        pass