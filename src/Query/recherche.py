import pandas as pd
from ..DAO.interaction import DAO


class Recherche:
    def __init__(self, sport: str):
        self.sport = sport
        self.dao = {}

    def data_basketball():
        self.dao["game"]=DAO(fichier = "../data/basketball/player.csv")
        self.dao["player"]=DAO(fichier = )
        self.dao["team"]=DAO(fichier = )

    def data_football_european_leagues():
        self.dao[]

    def data_league_of_legends():

    def data_tennis():

    def data_volleyball():

    def handle_unknown():
        log.write("unknown role")
        raise PermissionError("Unknown role")

    def cherche(self):
        if self.sport == "basketball":

        if self.sport == "football_european_leagues":

        if self.sport == "league_of_legends":

        if self.sport == "tennis":

        if self.sport == "volleyball":
    
    action = {

    }

    actions.get(status, handle_unknown)()