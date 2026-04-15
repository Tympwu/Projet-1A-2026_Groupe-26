from .Parser import Parser
import pandas as pd

from ..Model.Player import Player
# from ..Model.match import Match
# from ..Model.Equipe import Equipe
# from ..Model.Coach import Coach


class Badminton_Parser(Parser):

    def __init__(self):
        super().__init__("badminton")
    
    def parse_players(self, data: pd.DataFrame, other=None):
        """
        Fonction permettant de récupérer les éléments des bases de données et de créer les classes
        correspondantes. Cette dernière est spécifique aux joueurs de Badminton
        """
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
                continent=self.fetch_safety_data(row["continent"], str),
                sport="badminton")
            self.dict_player[player.id] = player

    def parse_competition(self, data: pd.DataFrame, other=None):
        """
        Fonction permettant de récupérer les éléments des bases de données et de créer les classes
        correspondantes. Cette dernière est spécifique aux compétition de Badminton
        """
        pass

    def parse_matchs(self, data: pd.DataFrame, other=None):
        """
        Fonction permettant de récupérer les éléments des bases de données et de créer les classes
        correspondantes. Cette dernière est spécifique aux Matchs de Badminton
        """
        pass
