
from .Player import Player


class Equipe:
     """classe qui represente une equipe
        
        ------------------
        Parameters Equipe:

        nom_equipe: str (entre 2 et 32 caractères)
        joueurs_equipe: list(Player)
        nom_coach_equipe: Player =None
        region_equipe: str =None
        pays_equipe: str =None
        statut_equipe: str ="Casual"
        ------------
    """
    def __init__(
        self,
        id: int,
        joueurs_equipe: set[Player],
        coach_equipe: set[Coach],
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
        self.id: int = id
        self.joueurs_equipe: set[Player] = joueurs_equipe
        self.coach_equipe: set[Coach] = coach_equipe
        self.nom_equipe: str | None = nom_equipe
        self.nom_abrev: str | None = nom_abrev
        self.nickname: str | None = nickname
        self.ville_equipe: str | None = ville_equipe
        self.region_equipe: str | None = region_equipe
        self.pays_equipe: str | None = pays_equipe
        self.continent_equipe: str | None = continent_equipe
        self.ligue: str | None = ligue
        self.annee_fondation: int | None = annee_fondation
