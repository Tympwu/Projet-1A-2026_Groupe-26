import pandas as pd
from ..DAO.interaction import DAO


class Recherche:
    def __init__(self, sport: str):
        self.sport = sport
        self.dao = {}

    def data_basketball():
        self.dao["game"] = DAO(fichier = "data/basketball/game.csv")
        self.dao["player"] = DAO(fichier = "data/basketball/player.csv")
        self.dao["team"] = DAO(fichier = "data/basketball/team.csv" )

    def data_football_european_leagues():
        self.dao["country"] = DAO(fichier = "data/football_european_leagues/country.csv")
        self.dao["league"] = DAO(fichier = "data/football_european_leagues/league.csv")
        self.dao["match"] = DAO(fichier = "data/football_european_leagues/")
        self.dao["player"] = DAO(fichier = "data/football_european_leagues/")
        self.dao["team"] = DAO(fichier = "data/football_european_leagues/")
        

    def data_league_of_legends():
        self.dao["coach"] = DAO(fichier = "data/league_of_legends/coach.csv")
        self.dao["match"] = DAO(fichier = "data/league_of_legends/match.csv")
        self.dao["player"] = DAO(fichier = "data/league_of_legends/player.csv")
        self.dao["team"] = DAO(fichier = "data/league_of_legends/team.csv")

    def data_tennis():
        self.dao[""] = DAO(fichier = )
        self.dao[""] = DAO(fichier = )
        self.dao[""] = DAO(fichier = )
        self.dao[""] = DAO(fichier = )
    
    def data_volleyball():
        self.dao[""] = DAO(fichier = )
        self.dao[""] = DAO(fichier = )
        self.dao[""] = DAO(fichier = )
        self.dao[""] = DAO(fichier = )
        self.dao[""] = DAO(fichier = )
        self.dao[""] = DAO(fichier = )
        self.dao[""] = DAO(fichier = )

    def handle_unknown():
        raise ValueError("Sport non pris en charge")

    def cherche(self):
        action = {
            "basketball": data_basketball
            "football_european_leagues": data_football_european_leagues
            "league_of_legends": data_league_of_legends
            "tennis": data_tennis
            "volleyball": data_volleyball
        }
        actions.get(status, handle_unknown)()