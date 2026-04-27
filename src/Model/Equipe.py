from .Coach import Coach
from .Player import Player
from tabulate import tabulate


class Equipe:
    def __init__(
        self,
        id: int,
        joueurs_equipe: set[Player] = None,
        coach_equipe: set[Coach] = None,
        nom_equipe: str = None,
        nom_abrev: str = None,
        nickname: str = None,
        ville_equipe: str = None,
        region_equipe: str = None,
        pays_equipe: str = None,
        continent_equipe: str = None,
        ligue: str = None,
        annee_fondation: int = None
    ) -> None:
        self.id = id
        self.joueurs_equipe = joueurs_equipe
        self.coach_equipe = coach_equipe
        self.nom_equipe = nom_equipe
        self.nom_abrev = nom_abrev
        self.nickname = nickname
        self.ville_equipe = ville_equipe
        self.region_equipe = region_equipe
        self.pays_equipe = pays_equipe
        self.continent_equipe = continent_equipe
        self.ligue = ligue
        self.annee_fondation = annee_fondation

    def ajouter_joueur(self, joueur: Player | None = None) -> None:
        """
        Permet de rajouter des joueurs à l'équipe
        
        Parameters
        ----------
        joueur : Player | None, optional

        """
        if isinstance(joueur, Player) and (joueur is not None):
            if self.joueurs_equipe is None:
                self.joueurs_equipe = set()
            self.joueurs_equipe.add(joueur)

    def ajouter_coach(self, coach: Coach | None = None) -> None:
        """
        Permet d'ajouter un coach à l'équipe
        
        Parameters
        ----------
        coach : Coach | None, optional

        """
        if isinstance(coach, Coach) and (Coach is not None):
            if self.coach_equipe is None:
                self.coach_equipe = set()
            self.coach_equipe.add(coach)

    def __str__(self):
        """
        Fonction d'affichage d'une équipe, l'affichage est de la forme Equipe, 
        puis Joueurs puis Coach
        """
        # On récupère les données des 3 catégories (Equipe, Joueurs et Coach) puis
        # on créer un tableau avec les données correspondantes

        # ÉQUIPES
        dict_result_equipe = {
            element: [value] for element, value in self.__dict__.items() if not (
                (value is None) or (element in {"joueurs_equipe", "coach_equipe"}))
        }
        tab_equipe = tabulate(dict_result_equipe, headers="keys", tablefmt="rounded_grid")

        # JOUEURS
        if self.joueurs_equipe is not None:
            dict_result_joueur = []
            for player in self.joueurs_equipe:
                dict_result_joueur.append([
                    player.id, player.full_name, player.dob, player.equipe, player.sexe])
            tab_joueurs = tabulate(
                dict_result_joueur, headers=["Id", "Name", "Date de naissance", "Équipe", "Sexe"],
                tablefmt="grid", colalign=("right", "center", "center", "left", "left"),
                missingval="\U0000274C"
            )
        else:
            tab_joueurs = "Aucun"

        # COACH
        if self.coach_equipe is not None:
            dict_result_coach = []
            for player in self.coach_equipe:
                dict_result_coach.append([
                    player.id, player.full_name, player.dob, player.equipe, player.sexe
                ])
            tab_coach = tabulate(
                dict_result_joueur, headers=["Id", "Name", "Date de naissance", "Équipe", "Sexe"],
                tablefmt="grid", colalign=("right", "center", "center", "left", "left"),
                missingval="\U0000274C"
            )
        else:
            tab_coach = "Aucun"

        return f"{tab_equipe}\n\nJoueurs :\n{tab_joueurs}\n\nCoach :\n{tab_coach}"
