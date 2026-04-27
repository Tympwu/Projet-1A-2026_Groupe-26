class Joueur_printer:
    """
    Classe permettant d'afficher un ou plusieurs joueurs de tout sports
    """
    def __init__(self, data: dict):
        self.data = data
    
    def single_player_printer(self, id):
        player = self.data.get(id)
        if player is None:
            print("Ce joueur n'existe pas")
        else:
            print(player)
    
    def all_player_printer(self):
        print("\n===== LISTE DES JOUEURS =====")
        for player in self.data.values():
            print(player)
