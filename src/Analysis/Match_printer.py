from tabulate import tabulate


class Match_printer:
    """
    Classe permettant d'afficher un ou des matchs de tout sports
    """
    def __init__(self, data: dict, team_sport=True):
        self.data = data
        self.team_sport = team_sport

    def single_match_printer(self, attr, val):
        found = False
        count = 0
        for match in self.data.values():
            value = getattr(match, attr, None)
            if value is not None and str(value).lower() == str(val).lower():
                count += 1
                print(match)
                found = True
        if not found:
            print("Aucun match trouvé")
        print("\n"+str(count) + " résultats trouvés")

    def all_match_printer(self):
        print("\n===== LISTE DES MATCHS =====")
        tab = []
        if self.team_sport is True:
            for match in self.data.values():
                tab.append([
                    match.id_match, match.best_of, match.date_match,
                    match.equipe1.nom_equipe, match.equipe2.nom_equipe,
                    match.score1, match.score2
                ])
            print(tabulate(
                tab, headers=[
                    "Id", "Best of", "Date du match", "Équipe 1",
                    "Équipe 2", "Score équipe 1", "Score équipe 2"
                ],
                tablefmt="grid",
                missingval="\U0000274C"
            ))
        else:
            for match in self.data.values():
                tab.append([
                    match.id_match, match.best_of, match.date_match,
                    match.joueur1, match.joueur2, match.score1, match.score2
                ])
            print(tabulate(
                tab, headers=[
                    "Id", "Best of", "Date du match", "Joueur 1",
                    "Joueur 2", "Score joueur 1", "Score joueur 2"],
                tablefmt="grid",
                missingval="\U0000274C"
            ))

        

