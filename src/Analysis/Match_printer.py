class Match_printer:
    """
    Classe permettant d'afficher un ou des matchs de tout sports
    """
    def __init__(self, data: dict, team_sport=True):
        self.data = data
        self.team_sport = team_sport

    def single_match_printer(self, id):
        largeur_: int = max(len({self.equipe_1.nom.equipe if self.team_sport is True else self.joueur_1.full_name}), len({self.equipe_2.nom.equipe if self.team_sport is True else self.joueur_2.full_name}))
        trait: list[str] = ["*" * (largeur_ + 4)]
        res = "\n".join(trait +
            f"{self.equipe_1.nom.equipe if self.team_sport is True else self.joueur_1.full_name:<{largeur_}} : {self.score_1}" +
            f"{self.equipe_2.nom.equipe if self.team_sport is True else self.joueur_2.full_name:<{largeur_}} : {self.score_2}" +
            trait)
        return res

    def all_match_printer(self):
        pass

