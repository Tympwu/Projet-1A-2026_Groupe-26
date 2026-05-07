from .Parser import Parser
import pandas as pd

from ..Model.Player import Player
from ..Model.Match import Match
from ..Model.Equipe import Equipe
from ..Model.Coach import Coach


class Volleyball_Parser(Parser):
    def __init__(self):
        super().__init__("volleyball")

    def parse_equipes(self, data: pd.DataFrame, other=None):
        """
        Fonction permettant de récupérer les éléments des bases de données et de créer les classes
        correspondantes. Cette dernière est spécifique aux Equipes de volleyball masculin
        """
        for index, row in data.iterrows():
            equipe = Equipe(
                id=index,
                nom_equipe=self.fetch_safety_data(row["country_long"], str) + " " + other,
                nom_abrev=self.fetch_safety_data(row["code"], str),
                pays_equipe=self.fetch_safety_data(row["country_long"], str),
                )
            self.dict_equipe[equipe.nom_equipe] = equipe

    def parse_players(self, data: pd.DataFrame, other=None):
        """
        Fonction permettant de récupérer les éléments des bases de données et de créer les classes
        correspondantes. Cette dernière est spécifique aux Joueurs de volleyball masculin
        """
        for index, row in data.iterrows():
            player = Player(
                id=index,
                sexe=other,
                full_name=self.fetch_safety_data(row["name"], str),
                dob=self.fetch_safety_data(row["birth_date"], str),
                pseudo=self.fetch_safety_data(row["nickname"], str),
                sport="volleyball",
                nationalite=self.fetch_safety_data(row["country_code"], str),
                equipe=self.fetch_safety_data(row["country_code"], str),
                taille=self.fetch_safety_data(row["height"], float))
            self.dict_player[player.id] = player

            for equipe in self.dict_equipe.values():
                if equipe.nom_abrev == player.equipe:
                    self.dict_equipe[equipe.nom_equipe].ajouter_joueur(player)

    def parse_coachs(self, data: pd.DataFrame, other=None):
        """
        Fonction permettant de récupérer les éléments des bases de données et de créer les classes
        correspondantes. Cette dernière est spécifique aux Coachs de leagues of legends
        """
        for index, row in data.iterrows():
            coach = Coach(
                sexe=other,
                id=index,
                full_name=self.fetch_safety_data(row["name"], str),
                dob=self.fetch_safety_data(row["birth_date"], str),
                nationalite=self.fetch_safety_data(row["country_code"], str),
                equipe=self.fetch_safety_data(row["country_code"], str),
                role=self.fetch_safety_data(row["function"], str)
                )
            self.dict_coach[coach.id] = coach

            for equipe in self.dict_equipe.values():
                if equipe.nom_abrev == coach.equipe:
                    self.dict_equipe[equipe.nom_equipe].ajouter_coach(coach)

    def parse_matchs(self, data: pd.DataFrame, other: pd.DataFrame, sexe=None):
        """
        Fonction permettant de récupérer les éléments des bases de données et de créer les classes
        correspondantes. Cette dernière est spécifique aux Matchs de volleyball masculin
        """

        self.dict_nom_abbreg_nom_equipe = dict()
        for index, row in other.iterrows():
            self.dict_nom_abbreg_nom_equipe[
                self.fetch_safety_data(row["code"], str)
                ] = self.fetch_safety_data(row["country_long"], str) + " " + sexe

        for index, row in data.iterrows():
            date_match = self.fetch_safety_data(row["date"], str)
            match = Match(
                id_match=index,
                equipe1=self.dict_equipe[
                    self.dict_nom_abbreg_nom_equipe[
                        self.fetch_safety_data(row["country_code_1"], str)]],
                equipe2=self.dict_equipe[
                    self.dict_nom_abbreg_nom_equipe[
                        self.fetch_safety_data(row["country_code_2"], str)]],
                date_match=date_match,
                score1=self.fetch_safety_data(row["set_country_1"], int),
                score2=self.fetch_safety_data(row["set_country_2"], int),
                )
            self.dict_matchs[match.id_match] = match
