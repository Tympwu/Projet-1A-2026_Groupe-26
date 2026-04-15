from .Parser import Parser
import pandas as pd

from ..Model.Player import Player
from ..Model.match import Match
from ..Model.Competition import Competition
# from ..Model.Equipe import Equipe
# from ..Model.Coach import Coach


class Tennis_Parser(Parser):
    def __init__(self):
        super().__init__("tennis")

    def parse_players(self, data: pd.DataFrame, other: str):
        """
        Fonction permettant de récupérer les éléments des bases de données et de créer les classes
        correspondantes. Cette dernière est spécifique aux joueurs de Tennis
        """
        for index, row in data.iterrows():
            dob = str(self.fetch_safety_data(row["dob"], int))
            dob = dob[:4] + "-" + dob[4:6] + "-" + dob[6:8]
            player = Player(
                id=self.fetch_safety_data(row["player_id"], int),
                sexe=other,
                first_name=self.fetch_safety_data(row["name_first"], str),
                last_name=self.fetch_safety_data(row["name_last"], str),
                main_forte=self.fetch_safety_data(row["hand"], str),
                dob=dob,
                nationalite=self.fetch_safety_data(row["ioc"], str),
                taille=self.fetch_safety_data(row["height"], int),
                sport="Tennis")
            self.dict_player[player.id] = player

    def parse_matchs(self, data: pd.DataFrame, other=None):
        """
        Fonction permettant de récupérer les éléments des bases de données et de créer les classes
        correspondantes. Cette dernière est spécifique aux Match de Tennis
        """
        def get_set_scores(score):
            sets = []
            res_score = [0, 0]
            for s in score.split():
                main_score = s.split("(")[0]
                if main_score in ["RET", "W/O", "DEF"]:
                    return (1,0)
                else:
                    games1, games2 = main_score.split("-")
                    sets.append((int(games1), int(games2)))
            for set in sets:
                if set[0] > set[1]:
                    res_score[0] += 1
                else:
                    res_score[1] += 1
            return (res_score[0], res_score[1])
    
        for index, row in data.iterrows():
            match = Match(
                id = index,
                tourney_id = self.fetch_safety_data(row["tourney_id"], int),
                joueur1 = self.fetch_safety_data(row["winner_id"], int),
                joueur2 = self.fetch_safety_data(row["loser_id"], int),
                score1 = get_set_scores(self.fetch_safety_data(row["score"], str))[0],
                score2 = get_set_scores(self.fetch_safety_data(row["score"], str))[1],
                best_of = self.fetch_safety_data(row["best_of"], int),
                temps_match = self.fetch_safety_data(row["minutes"], int)
            )
            self.dict_matchs[index] = match
            
    def parse_competition(self, data: pd.DataFrame, other=None):
        list_competition = []
        for index, row in data.iterrows():
            tourney_id_temp = self.fetch_safety_data(row["tourney_id"], str)
            if self.fetch_safety_data(row["tourney_id"], str) not in list_competition:
                date_data = str(self.fetch_safety_data(row["tourney_date"], int))
                date = date_data[:4] + "-" + date_data[4:6] + "-" + date_data[6:8]
                for match in self.dict_matchs:
                    if match.tourney_id 
                    matchs = {}
                competition = Competition(
                    id = self.fetch_safety_data(row["tourney_id"], str),
                    sport = "tennis",
                    nom = self.fetch_safety_data(row["tourney_name"], str),
                    surface = self.fetch_safety_data(row["surface"], str),
                    draw_size = self.fetch_safety_data(row["draw_size"], int),
                    level = self.fetch_safety_data(row["tourney_level"], int),
                    date = date,
                    match = matchs
                )
                list_competition.append(self.fetch_safety_data(row["tourney_id"], str))
                self.dict_competition[index]=competition
    
    