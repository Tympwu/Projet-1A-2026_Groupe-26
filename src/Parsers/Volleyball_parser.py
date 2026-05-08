from .Parser import Parser
import pandas as pd

from ..Model.Player import Player
from ..Model.Match import Match
from ..Model.Equipe import Equipe
from ..Model.Coach import Coach


class Volleyball_Parser(Parser):
    def __init__(self):
        super().__init__("volleyball")
        self.dict_nom_abbreg_nom_equipe = dict()

    def parse_equipes(self, data: pd.DataFrame, other=None):
        """
        Fonction permettant de récupérer les éléments des bases de données et de créer les classes
        correspondantes. Cette dernière est spécifique aux Equipes de volleyball masculin
        """
        if other == "H":
            id_add = 0
        elif other == "F":
            id_add = len(self.dict_equipe)
        for index, row in data.iterrows():
            equipe = Equipe(
                id=index + id_add,
                nom_equipe=self.fetch_safety_data(row["country"], str) + " " + other,
                nom_abrev=self.fetch_safety_data(row["code"], str),
                pays_equipe=self.fetch_safety_data(row["country_long"], str),
                )
            self.dict_equipe[equipe.nom_equipe] = equipe

    def parse_players(self, data: pd.DataFrame, other=None):
        """
        Fonction permettant de récupérer les éléments des bases de données et de créer les classes
        correspondantes. Cette dernière est spécifique aux Joueurs de volleyball masculin
        """
        if other == "H":
            id_add = 0
        elif other == "F":
            id_add = len(self.dict_player)
        for index, row in data.iterrows():
            player = Player(
                id=index + id_add,
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
        if other == "H":
            id_add = 0
        elif other == "F":
            id_add = len(self.dict_coach)
        for index, row in data.iterrows():
            coach = Coach(
                sexe=other,
                id=index + id_add,
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

        for index, row in other.iterrows():
            self.dict_nom_abbreg_nom_equipe[
                self.fetch_safety_data(row["code"], str) + sexe
                ] = self.fetch_safety_data(row["country"], str) + " " + sexe

        # Système pour s'occuper des équipes en fonction du sexe
        if sexe == "H":
            def equipe_data(row, entry):
                return self.dict_equipe[self.dict_nom_abbreg_nom_equipe[
                    self.fetch_safety_data(row[entry], str) + sexe
                    ]]
            rows = ["country_code_1", "country_code_2"]
            id_add = 0
        elif sexe == "F":
            def equipe_data(row, entry):
                return self.dict_equipe[self.fetch_safety_data(row[entry], str) + " " + sexe]
            rows = ["country_1", "country_2"]
            id_add = len(self.dict_matchs)

        for index, row in data.iterrows():
            date_match = self.fetch_safety_data(row["date"], str)
            match = Match(
                id_match=index + id_add,
                equipe1=equipe_data(row, rows[0]),
                equipe2=equipe_data(row, rows[1]),
                date_match=date_match,
                score1=self.fetch_safety_data(row["set_country_1"], int),
                score2=self.fetch_safety_data(row["set_country_2"], int),
                )
            self.dict_matchs[match.id_match] = match
