from .Coach import Coach
from .Player import Player


class Equipe:
    """Définition d'une équipe.

    Cette classe regroupe l'ensemble des informations d'une équipe.

    Parameters
    ----------
    id : int
        Identifiant unique de l'équipe.
    joueurs_equipe : set[Player] (default = None)
        Ensemble des objets Player appartenant à l'équipe.
    coach_equipe : set[Coach] (default = None)
        Ensemble des objets Coach rattachés à l'équipe.
    nom_equipe : str (default = None)
        Nom officiel de l'équipe.
    nom_abrev : str (default = None)
        Abréviation ou code de l'équipe.
    nickname : str (default = None)
        Surnom de l'équipe.
    ville_equipe : str (default = None)
        Ville d'attache de l'équipe.
    region_equipe : str (default = None)
        Région ou province de l'équipe.
    pays_equipe : str (default = None)
        Pays d'origine de l'équipe.
    continent_equipe : str (default = None)
        Continent de l'équipe.
    ligue : str (default = None)
        Ligue ou championnat dans lequel évolue l'équipe.
    annee_fondation : int (default = None)
        Année de création de l'équipe.

    Examples
    --------
    >>> e1 = Equipe(id=101, nom_equipe='Olympique Lyonnais', ville_equipe='Lyon')
    >>> print(e1)
    id : 101
    nom_equipe : Olympique Lyonnais
    ville_equipe : Lyon
    """

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
        """Convertit l'équipe en chaîne de caractères.

        Examples
        ---------
        >>> e1 = Equipe(id=1, nom_equipe='PSG')
        >>> print(e1)
        id : 1
        nom_equipe : PSG
        """
        result = ""
        for nom_argument, valeur in self.__dict__.items():
            if valeur is not None:
                result += f"\n{nom_argument} : {valeur}"
        return result

    def ajouter_joueur(self, joueur: Player | None = None) -> None:
        """Permet de rajouter des joueurs à l'équipe.

        Parameters
        ----------
        joueur : Player | None (default = None)
            L'instance du joueur à ajouter à l'ensemble des joueurs.

        Examples
        ---------
        >>> equipe = Equipe(id=1)
        >>> p1 = Player(first_name='Jean')
        >>> equipe.ajouter_joueur(p1)
        >>> len(equipe.joueurs_equipe)
        1
        """
        if isinstance(joueur, Player) and (joueur is not None):
            if self.joueurs_equipe is None:
                self.joueurs_equipe = set()
            self.joueurs_equipe.add(joueur)

    def ajouter_coach(self, coach: Coach | None = None) -> None:
        """Permet d'ajouter un coach à l'équipe.

        Parameters
        ----------
        coach : Coach | None (default = None)
            L'instance du coach à ajouter à l'ensemble du staff technique.

        Examples
        ---------
        >>> equipe = Equipe(id=1)
        >>> c1 = Coach(first_name='Alex')
        >>> equipe.ajouter_coach(c1)
        >>> len(equipe.coach_equipe)
        1
        """
        if isinstance(coach, Coach) and (coach is not None):
            if self.coach_equipe is None:
                self.coach_equipe = set()
            self.coach_equipe.add(coach)