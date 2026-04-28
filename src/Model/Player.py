from .Personne import Personne
from typing import Any
from tabulate import tabulate


class Player(Personne):
    """Définition d'un joueur.

    Cette classe représente un athlète de n'importe quel sport. Elle hérite
    des attributs de base de la classe Personne et y ajoute des données
    biométriques, sportives et statistiques.

    Parameters
    ----------
    id : int
        Identifiant unique du joueur.
    first_name : str (default = None)
        Prénom du joueur.
    last_name : str (default = None)
        Nom de famille du joueur.
    full_name : str (default = None)
        Nom complet du joueur.
    sexe : str (default = None)
        Sexe du joueur.
    dob : str (default = None)
        Date de naissance du joueur.
    lieu_naissance : str (default = None)
        Ville ou pays de naissance du joueur.
    pseudo : str (default = None)
        Pseudonyme sportif.
    equipe : Any (default = None)
        Instance de l'équipe à laquelle le joueur appartient.
    nationalite : str (default = None)
        Nationalité du joueur.
    continent : str (default = None)
        Continent d'origine ou de pratique.
    sport : str (default = None)
        Discipline sportive pratiquée.
    numero_maillot : int (default = None)
        Numéro porté par le joueur.
    main_forte : str (default = None)
        Main forte du joueur.
    taille : int (default = None)
        Taille du joueur.
    poids : int (default = None)
        Poids du joueur.
    stat : dict[str, int] (default = None)
        Dictionnaire contenant les statistiques de performance.
    role : str (default = None)
        Poste ou rôle sur le terrain.

    Examples
    --------
    >>> p1 = Player(id=10, first_name='Lionel', last_name='Messi', sport='Football')
    >>> print(p1.sport)
    Football
    >>> p1.id
    10
    """

    def __init__(
        self,
        id: int,
        first_name: str = None,
        last_name: str = None,
        full_name: str = None,
        sexe: str = None,
        dob: str = None,
        lieu_naissance: str = None,
        pseudo: str = None,
        id_equipe: int = None,
        equipe: Any = None,
        nationalite: str = None,
        continent: str = None,
        sport: str = None,
        numero_maillot: int = None,
        main_forte: str = None,
        taille: int = None,
        poids: int = None,
        stat: dict[str, int] = None,
        role: str = None
    ) -> None:
        self.id = id
        super().__init__(
            first_name=first_name, last_name=last_name, full_name=full_name,
            lieu_naissance=lieu_naissance, dob=dob, sexe=sexe
        )
        self.pseudo = pseudo
        self.id_equipe = id_equipe
        self.equipe = equipe
        self.nationalite_equipe = nationalite
        self.continent = continent
        self.sport = sport
        self.numero_maillot = numero_maillot
        self.main_forte = main_forte
        self.taille = round(taille, 2) if taille is not None else None
        self.poids = round(poids, 2) if poids is not None else None
        self.stat = stat
        self.role = role

    def __repr__(self) -> str:
        """Représentation officielle de l'objet Player.

        Returns
        -------
        str
            La chaîne de caractères générée par __str__.
        """
        return str(self)

    def __str__(self) -> str:
        """Renvoie un tableau correspondant à l'affichage du joueur.

        Examples
        ---------
        >>> j1 = Player(id=1, full_name='Gérard Bill')
        >>> print(j1)
        ╭────────────┬──────────────╮
        │         id │ full_name    │
        ├────────────┼──────────────┤
        │          1 │ Gérard Bill  │
        ╰────────────┴──────────────╯
        """
        dict_result = {
            element: [value] for element, value in self.__dict__.items() if value is not None
        }
        return tabulate(dict_result, headers="keys", tablefmt="rounded_grid")

    def __hash__(self):
        """Calcule le hash du joueur.

        Returns
        -------
        int
            Hash basé sur l'identifiant id.
        """
        return hash(self.id)
