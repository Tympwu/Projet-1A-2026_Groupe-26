from .Coach import Coach
from .Player import Player


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

    def __str__(self) -> str:
        result = ""
        for nom_argument, valeur in self.__dict__.items():
            if valeur is not None:
                result += f"\n{nom_argument} : {valeur}"
        return result

    def ajouter_joueur(self, joueur: Player | None = None) -> None:
        if isinstance(joueur, Player) and (joueur is not None):
            if self.joueurs_equipe is None:
                self.joueurs_equipe = set()
            self.joueurs_equipe.add(joueur)

    def ajouter_coach(self, coach: Coach | None = None) -> None:
        if isinstance(coach, Coach) and (Coach is not None):
            if self.coach_equipe is None:
                self.coach_equipe = set()
            self.coach_equipe.add(coach)


