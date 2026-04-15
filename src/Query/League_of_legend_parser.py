from Parser import Parser
import pandas as pd

from ..Model.Player import Player
from ..Model.match import Match
from ..Model.Equipe import Equipe
from ..Model.Coach import Coach


class League_of_legend_Parser(Parser):

    def __init__(self):
        super().__init__("leagues_of_legends")

    def parse_equipes(self, data: pd.DataFrame, other=None):
        """
        Fonction permettant de récupérer les éléments des bases de données et de créer les classes
        correspondantes. Cette dernière est spécifique aux Equipes de leagues of legends
        """
        for index, row in data.iterrows():
            equipe = Equipe(
                id=index,
                nom_equipe=self.fetch_safety_data(row["team"], str),
                nom_abrev=self.fetch_safety_data(row["team_abbreviation"], str),
                region_equipe=self.fetch_safety_data(row["region"], str),
                pays_equipe=self.fetch_safety_data(row["location"], str),
                )
            self.dict_equipe[equipe.nom_equipe] = equipe

    def parse_players(self, data: pd.DataFrame, other=None):
        """
        Fonction permettant de récupérer les éléments des bases de données et de créer les classes
        correspondantes. Cette dernière est spécifique aux Joueurs de leagues of legends
        """
        for index, row in data.iterrows():
            player = Player(
                id=index,
                full_name=self.fetch_safety_data(row["name"], str),
                dob=self.fetch_safety_data(row["birthdate"], str),
                pseudo=self.fetch_safety_data(row["pseudo"], str),
                role=self.fetch_safety_data(row["role"], int),
                sport="League of legends",
                nationalite=self.fetch_safety_data(row["country_of_birth"], str),
                equipe=self.fetch_safety_data(row["team"], str))
            self.dict_player[player.id] = player

            for equipe in self.dict_equipe.values():
                if equipe.nom_equipe == player.equipe:
                    self.dict_equipe[equipe.nom_equipe].ajouter_joueur(player)

    def parse_coach(self, data: pd.DataFrame, other=None):
        """
        Fonction permettant de récupérer les éléments des bases de données et de créer les classes
        correspondantes. Cette dernière est spécifique aux Coachs de leagues of legends
        """
        for index, row in data.iterrows():
            coach = Coach(
                id=index,
                full_name=self.fetch_safety_data(row["name"], str),
                dob=self.fetch_safety_data(row["birthdate"], str),
                pseudo=self.fetch_safety_data(row["pseudo"], str),
                role=self.fetch_safety_data(row["role"], int),
                nationalite=self.fetch_safety_data(row["country_of_birth"], str),
                equipe=self.fetch_safety_data(row["team"], str))
            self.dict_coach[coach.id] = coach

            for equipe in self.dict_equipe.values():
                if equipe.nom_equipe == coach.equipe:
                    self.dict_equipe[equipe.nom_equipe].ajouter_coach(coach)

    def parse_matchs(self, data: pd.DataFrame, other: pd.DataFrame):
        """
        Fonction permettant de récupérer les éléments des bases de données et de créer les classes
        correspondantes. Cette dernière est spécifique aux Matchs de leagues of legends
        """
        self.dict_nom_abbreg_nom_equipe = dict()
        for index, row in other.iterrows():
            self.dict_nom_abbreg_nom_equipe[
                self.fetch_safety_data(row["team_abbreviation"], str)
                ] = self.fetch_safety_data(row["team"], str)
        print(self.dict_nom_abbreg_nom_equipe)
        for index, row in data.iterrows():
            date_match = self.fetch_safety_data(row["date"], str)
            date_match = date_match[:4] + "-" + date_match[5:7] + "-" + date_match[8:10]
            match = Match(
                id_match=index,
                equipe1=self.dict_equipe[
                    self.dict_nom_abbreg_nom_equipe[self.fetch_safety_data(row["team_blue"], str)]],
                equipe2=self.dict_equipe[
                    self.dict_nom_abbreg_nom_equipe[self.fetch_safety_data(row["team_red"], str)]],
                temps_match=self.fetch_safety_data(row["time"], str),
                date_match=date_match
                )
            if self.fetch_safety_data(row["winner"], str) == match.equipe1.nom_equipe:
                match.ajouter_scores(score1=1, score2=0)
            else:
                match.ajouter_scores(score1=0, score2=1)

            self.dict_matchs[match.id_match] = match

        pass

    def parse_competition(self, data: pd.DataFrame, other=None):
        """
        Fonction permettant de récupérer les éléments des bases de données et de créer les classes
        correspondantes. Cette dernière est spécifique aux Compétitions de leagues of legends
        """
        pass

