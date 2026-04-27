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
        for player in self.data.values():
            print(player)
