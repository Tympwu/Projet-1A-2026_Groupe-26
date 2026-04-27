class Recherche:
    """
    Classe permettant de faire les recherches des joueurs, matchs et autres
    """
    def __init__(self, sport: str, printer):
        """
        sport : str
            Sport choisi par l'utilisateur
        printer : dict[str : Printer]
            dictionnaire contenant les différentes classes d'affichages pour les données
        """
        self.sport = sport
        self.printer = printer
        self.joueur_attr_allowed = [
            "id", "first_name", "last_name", "full_name", "sexe", "pseudo", "equipe", "taille",
            "nationalite", "continent", "numero_maillot", "main_forte", "poids", "role"
        ]

    def answer_question(self, autorise_value: set):
        result: str = input("Réponse : ")
        if not result.isnumeric():
            print("La valeur renseignée n'est pas valide")
            result = -1
        elif int(result) not in autorise_value:
            print("La valeur renseignée n'est pas correct")
            result = -1
        else:
            result = int(result)
        return result

    def visualise_data(self):
        """
        Fonction permettant de savoir quelles données affichées entre joueurs, matchs et autre
        """
        while True:
            print("-------------------------------------------")
            print("Que voulez-vous voir ?")
            print("1. Les joueurs")
            print("2. Les équipes")
            print("3. Les matchs\n")
            print("0. Revenir en arrière\n\n")
            result = self.answer_question({0, 1, 2, 3})
            result_match = {1: self.menu_recherche_joueurs, 2: "equipes", 3: "match"}
            if result == 0:
                return
            elif result != -1:
                result_match[result]()

    def visualise_precise_data(self, wanted: str):
        """
        A définir, à garder ?
        """
        while True:
            if wanted == "matchs":
                print("-------------------------------------------")
                print("Voulez-vous voir un élément précis ou l'ensemble ?")
                print("Pour un élément précis notez son indice, sinon juste validez")
                print("0. Revenir en arrière\n\n")
                result = input("Réponse : ")
                if result == "":
                    self.__match_printer.all_match_printer()
                if not result.isnumeric():
                    print("La valeur renseignée n'est pas valide")
                elif result == "0":
                    return
                else:
                    result = int(result)
            elif wanted == "equipes":
                pass
            elif wanted == "joueurs":
                if result == "":
                    self.__joueur_printer.all_player_printer()
                if not result.isnumeric():
                    print("La valeur renseignée n'est pas valide")
                elif result == "0":
                    return
                else:
                    self.__joueur_printer.single_player_printer("id", int(result))
            else:
                print("Cette option n'existe pas")

    def menu_recherche_joueurs(self):
        """
        Fonction permettant de gérer l'affichage d'un ou plusieurs joueurs
        """
        sample_player = next(iter(self.printer["joueurs"].data.values()))
        # attributes = list(sample_player.__dict__.keys())
        filtered_attr = [
            k for k, v in sample_player.__dict__.items()
            if v is not None and k in self.joueur_attr_allowed
        ]

        while True:
            print("-------------------------------------------")
            print("\n===== MENU JOUEURS =====\n")
            print("0. Retour")
            print("1. Afficher tous les joueurs")
            print("2. Recherche avancée\n\n")

            choice = input("Réponse : ")
            if choice == "0":
                return
            elif choice == "1":
                self.printer["joueurs"].all_player_printer()
            elif choice == "2":
                self.recherche_par_attribut_joueur(filtered_attr)
            else:
                print("Cette option n'existe pas\n\n")

    def recherche_par_attribut_joueur(self, attributes: list[str]):
        while True:
            print("-------------------------------------------")
            print("\n===== RECHERCHE JOUEUR =====\n\nRecherche par:")
            for i, attr in enumerate(attributes, 1):
                print(f"{i}. {attr}")
            print("0. Retour\n\n")
            choix = str(input("Réponse : "))
            if choix == "0":
                return
            if choix.isnumeric() and int(choix) in range(1, len(attributes)+1):
                attr = attributes[int(choix) - 1]
                valeur = input(f"Valeur pour {attr} : ")
                self.printer["joueurs"].single_player_printer(attr, valeur)
            else:
                print("Réponse invalide\n\n")
