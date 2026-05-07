from .Menu import Menu
from tabulate import tabulate


class Recherche(Menu):
    """
    Classe permettant de faire les recherches des joueurs, matchs et autres
    """
    def __init__(self):
        """
        sport : str
            Sport choisi par l'utilisateur
        """
        super().__init__()

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
                if result == 2 and not self.team_sport:
                    print("Il n'y a pas d'équipe dans ce sport")
                else:
                    self.categorie = result
                    self.menu_recherche()

    def menu_recherche(self):
        """
        Fonction permettant de gérer l'affichage d'un ou plusieurs joueurs / matchs / equipes...
        """
        self.filtered_attr = self.list_attr(
            self.parser_match_name[self.categorie],
            self.parameters_allowed[self.categorie]
            )
        self.menu_question(
            f"\n===== MENU {self.categorie.upper()} =====\n",
            [f"Afficher tous les {self.categorie}", "Recherche avancée"],
            {1: self.all_printer,
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
            self.search_element(attr, valeur)

    def search_element(self, attr, val):
        """
        Fonction permettant de rechercher un ou plusieurs éléments correspondant

        Parameters
        ----------
        attr :
            attribue voulu / autorisé pour cette catégorie d'élément
        val :
            La valeur précise recherché permettant de faire le tri
        """
        found = False
        count = 0
        for element in self.parser_match_name[self.categorie].values():
            value = getattr(element, attr, None)
            if value is not None and str(value).lower() == str(val).lower():
                count += 1
                print(element)
                found = True
        if not found:
            print(f"Aucun(e) {self.categorie} trouvé(e)")
        else:
            print("\n"+str(count) + " résultats trouvés")

    def all_printer(self):
        """
        Fonction permettant d'afficher tous les éléments d'une catégorie
        """
        print(f"\n===== LISTE DES {self.categorie.upper()} =====")
        tab = []
        if self.categorie == "matchs":
            if self.team_sport is True:
                for match in self.parser_match_name[self.categorie].values():
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
                for match in self.parser_match_name[self.categorie].values():
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
        elif self.categorie == "joueurs":
            for player in self.parser_match_name[self.categorie].values():
                tab.append([player.id, player.full_name, player.dob, player.equipe, player.sexe])
            print(tabulate(
                tab, headers=["Id", "Name", "Date de naissance", "Équipe", "Sexe"],
                tablefmt="grid", colalign=("right", "center", "center", "left", "left"),
                missingval="\U0000274C"
            ))
        elif self.categorie == "equipes":
            for equipe in self.parser_match_name[self.categorie].values():
                tab.append([equipe.id, equipe.nom_equipe, equipe.ville_equipe,
                            equipe.region_equipe, equipe.pays_equipe, equipe.annee_fondation])
            print(tabulate(
                tab, headers=["Id", "Name", "Ville", "Région", "Pays", "Année de fondation"],
                tablefmt="grid",
                missingval="\U0000274C"
            ))
