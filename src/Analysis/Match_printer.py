class Match_printer:
    """
    Classe permettant d'afficher un ou des matchs de tout sports
    """
    def __init__(self, data: dict, team_sport=True):
        self.data = data
        self.team_sport = team_sport

    def single_match_printer(self, id):
        res = f"""
        {self.equipe_1.nom.equipe if self.team_sport is True else self.joueur_1.full_name} : {self.score_1}
        """
        + f"""
        {self.equipe_2.nom.equipe if self.team_sport is True else self.joueur_2.full_name} : {self.score_2}
        """
        return res

    def all_match_printer(self):
        pass