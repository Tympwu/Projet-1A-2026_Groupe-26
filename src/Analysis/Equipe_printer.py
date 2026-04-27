from tabulate import tabulate


class Equipe_printer:
    """
    Classe permettant d'afficher une ou plusieurs équipe de tout sports
    """
    def __init__(self, data: dict):
        self.data = data

    def single_equipe_printer(self, attr, val):
        found = False
        count = 0
        for equipe in self.data.values():
            value = getattr(equipe, attr, None)
            if value is not None and str(value).lower() == str(val).lower():
                count += 1
                print(equipe)
                found = True
        if not found:
            print("Aucun joueur trouvé")
        print("\n"+str(count) + " résultats trouvés")

    def all_equipe_printer(self):
        print("\n===== LISTE DES ÉQUIPES =====")
        tab = []
        for equipe in self.data.values():
            tab.append([equipe.id, equipe.nom_equipe, equipe.ville_equipe,
                        equipe.region_equipe, equipe.pays_equipe, equipe.annee_fondation])
        print(tabulate(
            tab, headers=["Id", "Name", "Ville", "Région", "Pays", "Année de fondation"],
            tablefmt="grid",
            missingval="\U0000274C"
        ))
