
from ..DAO.interaction import DAO


class Data_loader:
    def __init__(self, sport: str):
        if not isinstance(sport, str):
            raise TypeError("sport doit être une chaîne de caractères")
        self.sport = sport
        self.dao = {}

    def __data_basketball(self):
        self.dao["game"] = DAO(fichier="data/basketball/game.csv")
        self.dao["player"] = DAO(fichier="data/basketball/player.csv")
        self.dao["team"] = DAO(fichier="data/basketball/team.csv")

    def __data_football_european_leagues(self):
        self.dao["country"] = DAO(fichier="data/football_european_leagues/country.csv")
        self.dao["league"] = DAO(fichier="data/football_european_leagues/league.csv")
        self.dao["match"] = DAO(fichier="data/football_european_leagues/match.csv")
        self.dao["player"] = DAO(fichier="data/football_european_leagues/player.csv")
        self.dao["equipe"] = DAO(fichier="data/football_european_leagues/team.csv")

    def __data_league_of_legends(self):
        self.dao["coach"] = DAO(fichier="data/league_of_legends/coach.csv")
        self.dao["match"] = DAO(fichier="data/league_of_legends/match.csv")
        self.dao["player"] = DAO(fichier="data/league_of_legends/player.csv")
        self.dao["team"] = DAO(fichier="data/league_of_legends/team.csv")

    def __data_tennis(self):
        self.dao["atp_matches_2024"] = DAO(fichier="data/tennis/atp_matches_2024.csv")
        self.dao["atp_players_2024"] = DAO(fichier="data/tennis/atp_players_2024.csv")
        self.dao["wta_matches_2024"] = DAO(fichier="data/tennis/wta_matches_2024.csv")
        self.dao["wta_players_2024"] = DAO(fichier="data/tennis/wta_players_2024.csv")

    def __data_volleyball(self):
        self.dao["coach_men"] = DAO(fichier="data/volleyball/coach_men.csv")
        self.dao["coach_women"] = DAO(fichier="data/volleyball/coach_women.csv")
        self.dao["country"] = DAO(fichier="data/volleyball/country.csv")
        self.dao["match_men"] = DAO(fichier="data/volleyball/match_men.csv")
        self.dao["match_women"] = DAO(fichier="data/volleyball/match_women.csv")
        self.dao["player_men"] = DAO(fichier="data/volleyball/player_men.csv")
        self.dao["player_women"] = DAO(fichier="data/volleyball/player_women.csv")

    def __data_badminton(self):
        pass
    
    def handle_unknown():
        raise ValueError("Sport non pris en charge")

    def loader(self):
        action = {
            "basketball": self.__data_basketball,
            "football_european_leagues": self.__data_football_european_leagues,
            "league_of_legends": self.__data_league_of_legends,
            "tennis": self.__data_tennis,
            "volleyball": self.__data_volleyball,
            "Badminton": self.__data_badminton
        }
        action[self.sport]()
