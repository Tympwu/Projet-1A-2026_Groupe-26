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
        self.categorie_allowed = []
        for key, element in self.parser_match_name.items():
            if element != {}:
                self.categorie_allowed.append(key)

    def visualise_data(self):
        """
        Fonction permettant de savoir quelles données affichées entre joueurs, matchs et autre
        """
        possible_answer = ["Les " + element for element in self.categorie_allowed]
        dict_possible_answer = {i: element for i, element in enumerate(self.categorie_allowed, 1)}
        while True:
            result = self.menu_question(
                "Que voulez-vous voir ?",
                possible_answer,
                dict_possible_answer
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
        # Permet de gérer le cas des matchs avec la possibilité de tri avec les équipes ou joueurs
        if self.categorie == "matchs":
            parameter_allow = self.parameters_allowed[self.categorie].copy()
            parameter_allow.extend(["equipe1", "equipe2", "joueur1", "joueur2"])
        else:
            parameter_allow = self.parameters_allowed[self.categorie]

        # Création de la liste des paramètres autorisés
        self.filtered_attr = self.list_attr(
            self.parser_match_name[self.categorie],
            parameter_allow
        )

        # Proposition des différents choix
        self.menu_question(
            f"\n===== MENU {self.categorie.upper()} =====\n",
            [f"Afficher tous les {self.categorie}", "Recherche avancée"],
            {1: self.all_printer,
             2: self.recherche_par_attribut}
        )

    def recherche_par_attribut(self):
        """
        Fonction permettant de rechercher un élément précis en fonction d'un paramètre
        """
        attr = self.menu_question(
            f"\n===== RECHERCHE {self.categorie.upper()} =====\n\nRecherche par:",
            self.filtered_attr,
            {i: ele for i, ele in enumerate(self.filtered_attr, 1)}
            )
        if attr == 0:
            return
        elif attr is not None:
            valeur = input(f"Valeur pour {attr} : ")
            if attr in {"equipe1", "equipe2"}:
                attr = attr + ".nom_equipe"
            elif attr in {"joueur1", "joueur2"}:
                attr = attr + ".full_name"
            self.search_element(attr, valeur)

    def search_element(self, attr: str, val: str):
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
        if ("." in attr):
            attr = attr.split(sep=".")
        for element in self.parser_match_name[self.categorie].values():
            if isinstance(attr, list):
                value = getattr(getattr(element, attr[0], None), attr[1], None)
            else:
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
                        match.id_match, match.best_of, match.date_match, match.joueur1.full_name,
                        match.joueur2.full_name, match.score1, match.score2
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
        elif self.categorie == "coachs":
            for coach in self.parser_match_name[self.categorie].values():
                tab.append([coach.id, coach.full_name, coach.equipe, coach.role])
            print(tabulate(
                tab, headers=["Id", "Name", "Équipe", "Rôle"],
                tablefmt="grid",
                missingval="\U0000274C"
            ))
