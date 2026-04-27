from .Parser import Parser
import pandas as pd

from ..Model.Player import Player
from ..Model.match import Match
from ..Model.Equipe import Equipe


class Basketball_Parser(Parser):

    def __init__(self):
        super().__init__("basketball")

    def parse_equipes(self, data: pd.DataFrame, other=None):
        """
        Fonction permettant de récupérer les éléments des bases de données et de créer les classes
        correspondantes. Cette dernière est spécifique aux Equipes de Football européen
        """
        for index, row in data.iterrows():
            equipe = Equipe(
                id=self.fetch_safety_data(row["id"], int),
                nom_equipe=self.fetch_safety_data(row["full_name"], str),
                nom_abrev=self.fetch_safety_data(row["abbreviation"], str),
                nickname=self.fetch_safety_data(row["nickname"], str),
                ville_equipe=self.fetch_safety_data(row["city"], str),
                region_equipe=self.fetch_safety_data(row["state"], str),
                )
            self.dict_equipe[equipe.id] = equipe

    def parse_players(self, data: pd.DataFrame, other=None):
        """
        Fonction permettant de récupérer les éléments des bases de données et de créer les classes
        correspondantes. Cette dernière est spécifique aux Joueurs de Basketball
        """
        for index, row in data.iterrows():
            dob = self.fetch_safety_data(row["birthdate"], str)
            if len(dob) != 10:
                dob = dob[:9] + "0"
            taille = self.fetch_safety_data(row["height"], str)
            taille1 = int(taille[0])
            taille2 = int(taille[2:])
            taille = 30.48*taille1 + 2.54*taille2
            poids = self.fetch_safety_data(row["weight"], int)
            poids = 0.454*poids
            player = Player(
                id=self.fetch_safety_data(row["person_id"], int),
                first_name=self.fetch_safety_data(row["first_name"], str),
                last_name=self.fetch_safety_data(row["last_name"], str),
                numero_maillot=self.fetch_safety_data(row["jersey"], int),
                dob=dob,
                role=self.fetch_safety_data(row["position"], str),
                taille=taille,
                poids=poids,
                equipe=self.dict_equipe[self.fetch_safety_data(row["team_id"], int)],
                sport="Basketball")
            self.dict_player[player.id] = player

    def parse_matchs(self, data: pd.DataFrame, other: pd.DataFrame):
        """
        Fonction permettant de récupérer les éléments des bases de données et de créer les classes
        correspondantes. Cette dernière est spécifique aux Matchs de Football européen
        """
        for index, row in data.iterrows():
            match = Match(
                id_match=self.fetch_safety_data(row["game_id"], int),
                equipe1=self.dict_equipe[self.fetch_safety_data(row["team_id_home"], int)],
                equipe2=self.dict_equipe[self.fetch_safety_data(row["team_id_away"], int)],
                score1=self.fetch_safety_data(row["pts_home"], int),
                score2=self.fetch_safety_data(row["pts_away"], int),
                date_match=self.fetch_safety_data(row["game_date"], str)
                )
            self.dict_matchs[match.id_match] = match

    def parse_competition(self, data: pd.DataFrame, other=None):
        """
        Fonction permettant de récupérer les éléments des bases de données et de créer les classes
        correspondantes. Cette dernière est spécifique aux Compétitions de Football européen
        """
        pass
