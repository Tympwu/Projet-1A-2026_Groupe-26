from Parser import Parser
import pandas as pd

from ..Model.Player import Player
from ..Model.match import Match
from ..Model.Equipe import Equipe


class Football_European_leagues_Parser(Parser):
    def __init__(self):
        super().__init__("football")

    def parse_players(self, data: pd.DataFrame, other=None):
        """
        Fonction permettant de récupérer les éléments des bases de données et de créer les classes
        correspondantes. Cette dernière est spécifique aux Joueurs de Football européen
        """
        for index, row in data.iterrows():
            player = Player(
                id=self.fetch_safety_data(row["player_api_id"], int),
                full_name=self.fetch_safety_data(row["player_name"], str),
                dob=self.fetch_safety_data(row["birthday"], str),
                taille=self.fetch_safety_data(row["height (cm)"], int),
                poids=self.fetch_safety_data(row["weight (kg)"], int),
                sport="Football")
            self.dict_player[player.id] = player

    def parse_equipes(self, data: pd.DataFrame, other=None):
        """
        Fonction permettant de récupérer les éléments des bases de données et de créer les classes
        correspondantes. Cette dernière est spécifique aux Equipes de Football européen
        """
        for index, row in data.iterrows():
            equipe = Equipe(
                id=self.fetch_safety_data(row["team_api_id"], int),
                nom_equipe=self.fetch_safety_data(row["team_long_name"], str),
                nom_abrev=self.fetch_safety_data(row["team_short_name"], str),
                )
            self.dict_equipe[equipe.id] = equipe

    def parse_matchs(self, data: pd.DataFrame, other: pd.DataFrame):
        """
        Fonction permettant de récupérer les éléments des bases de données et de créer les classes
        correspondantes. Cette dernière est spécifique aux Matchs de Football européen
        """
        dict_contry_id: dict[int, str] = {}
        for index, row in other.iterrows():
            dict_contry_id[row["id"]] = row["name"]
        for index, row in data.iterrows():
            date_match = self.fetch_safety_data(row["date"],str)
            date_match = date_match[:4] + "-" + date_match[5:7] + "-" + date_match[8:10]
            match = Match(
                id_match=self.fetch_safety_data(row["match_api_id"], int),
                region=dict_contry_id[self.fetch_safety_data(row["country_id"], int)],
                equipe1=self.dict_equipe[self.fetch_safety_data(row["home_team_api_id"], int)],
                equipe2=self.dict_equipe[self.fetch_safety_data(row["away_team_api_id"], int)],
                score1=self.fetch_safety_data(row["home_team_goal"], int),
                score2=self.fetch_safety_data(row["away_team_goal"], int),
                date_match=date_match
                )
            self.dict_matchs[match.id_match] = match

    def parse_competition(self, data: pd.DataFrame, other=None):
        """
        Fonction permettant de récupérer les éléments des bases de données et de créer les classes
        correspondantes. Cette dernière est spécifique aux Compétitions de Football européen
        """
        pass