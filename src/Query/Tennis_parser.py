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
                id=index,
                joueur1=self.fetch_safety_data(row["winner_id"], int),
                joueur2=self.fetch_safety_data(row["loser_id"], int),
                score1=get_set_scores(self.fetch_safety_data(row["score"], str))[0],
                score2=get_set_scores(self.fetch_safety_data(row["score"], str))[1],
                best_of=self.fetch_safety_data(row["best_of"], int),
                temps_match=self.fetch_safety_data(row["minutes"], int)
            )
            self.dict_matchs[index] = match
            
    def parse_competition(self, data: pd.DataFrame, other=None):
        for index, row in data.iterrows():
            competition = Competition(
                self.id= index
                self.sport = sport
                self.nom= nom
                self.surface= surface
                self.draw_size= draw_size
                self.level= level
                self.date = date
                self.match= {}
            )
    
    