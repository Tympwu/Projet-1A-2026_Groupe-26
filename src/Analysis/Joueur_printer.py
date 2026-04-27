from tabulate import tabulate


class Joueur_printer:
    """
    Classe permettant d'afficher un ou plusieurs joueurs de tout sports
    """
    def __init__(self, data: dict):
        self.data = data

    def single_player_printer(self, attr, val):
        found = False
        count = 0
        for player in self.data.values():
            value = getattr(player, attr, None)
            if value is not None and str(value).lower() == str(val).lower():
                count += 1
                print(player)
                found = True
        if not found:
            print("Aucun joueur trouvé")
        print("\n"+str(count) + " résultats trouvés")

    def all_player_printer(self):
        print("\n===== LISTE DES JOUEURS =====")
        tab = []
        for player in self.data.values():
            tab.append([player.id, player.full_name, player.dob, player.equipe, player.sexe])
        print(tabulate(
            tab, headers=["Id", "Name", "Date de naissance", "Équipe", "Sexe"],
            tablefmt="grid", colalign=("right", "center", "center", "left", "left"),
            missingval="\U0000274C"
        ))
