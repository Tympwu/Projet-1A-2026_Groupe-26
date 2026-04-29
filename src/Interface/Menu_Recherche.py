from .Menu import Menu


class Recherche(Menu):
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
        super().__init__()
        self.printer = printer

    def visualise_data(self):
        """
        Fonction permettant de savoir quelles données affichées entre joueurs, matchs et autre
        """
        while True:
            result = self.menu_question(
                "Que voulez-vous voir ?",
                ["Les joueurs", "Les équipes", "Les matchs"],
                {1: "joueurs", 2: "equipes", 3: "matchs"}
            )
            if result == 0:
                return
            else:
                if result == 2 and self.sport in {"tennis"}:
                    print("Il n'y a pas d'équipe dans ce sport")
                else:
                    self.categorie = result
                    self.menu_recherche()

    def menu_recherche(self):
        """
        Fonction permettant de gérer l'affichage d'un ou plusieurs joueurs / matchs / equipes...
        """
        self.filtered_attr = self.list_attr(
            self.printer[self.categorie].data,
            self.parameters_allowed[self.categorie]
            )
        self.menu_question(
            f"\n===== MENU {self.categorie.upper()} =====\n",
            [f"Afficher tous les {self.categorie}", "Recherche avancée"],
            {1: self.printer[self.categorie].all_printer,
             2: self.recherche_par_attribut}
        )

    def recherche_par_attribut(self):
        attr = self.menu_question(
            f"\n===== RECHERCHE {self.categorie.upper()} =====\n\nRecherche par:",
            self.filtered_attr,
            {i: ele for i, ele in enumerate(self.filtered_attr, 1)}
            )
        if attr == 0:
            return
        elif attr is not None:
            valeur = input(f"Valeur pour {attr} : ")
            self.printer[self.categorie].single_printer(attr, valeur)
