from Parser import Parser
import pandas as pd

from ..Model.Player import Player
# from ..Model.match import Match
# from ..Model.Equipe import Equipe
# from ..Model.Coach import Coach


class Volleyball_Parser(Parser):
    def __init__(self):
        super().__init__("volleyball")

    def parse_players(self, data: pd.DataFrame, other=None):
        """
        Fonction permettant de récupérer les éléments des bases de données et de créer les classes
        correspondantes. Cette dernière est spécifique aux Joueurs de Volleyball
        """
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
            self.dict_player[player.id] = player
