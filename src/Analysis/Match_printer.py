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

"""
        # Calcule la largeur du texte (sans compter l'étoile au début et à la fin)
    largeur_: int = max([largeur] + [len(string) for string in texte])

    # Définis le format pour l'alignement
    format_: str
    if alignement == "gauche":
        format_ = "<"
    elif alignement == "droite":
        format_ = ">"
    else:
        format_ = "^"

    # Calcule la première ligne (qui est identique à la dernière ligne)
    premiere_ligne: list[str] = ["*" * (largeur_ + 2)]

    # Calcule la chaîne de caractères finale
    res: str = "\n".join(premiere_ligne + [f"*{string:{format_}{largeur_}}*" for string in texte] + premiere_ligne)

    # Affiche le résultat
    print(res)
    """
