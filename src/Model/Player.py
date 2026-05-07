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
    equipe : str (default = None)
        nom de l'équipe à laquelle le joueur appartient.
    id_equipe : int (defautl = None)
        id de l'équipe à laquelle le joueur appartient.
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

    id: int
    first_name: str
    last_name: str
    full_name: str
    sexe: str
    dob: str
    lieu_naissance: str
    pseudo: str
    id_equipe: int
    equipe: str
    nationalite: str
    continent: str
    sport: str
    numero_maillot: int
    main_forte: str
    taille: int
    poids: int
    stat: dict[str, int]
    role: str

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
        taille: float = None,
        poids: float = None,
        stat: dict[str, int] = None,
        role: str = None
    ) -> None:
        super().__init__(
            id=id, first_name=first_name, last_name=last_name, full_name=full_name,
            lieu_naissance=lieu_naissance, dob=dob, sexe=sexe
        )
        if (pseudo is not None) and (not isinstance(pseudo, str)):
            raise ValueError("l'attribut pseudo doit être du type str ou None")
        if (id_equipe is not None) and (not isinstance(id_equipe, int)):
            raise ValueError("l'attribut id_equipe doit être du type int ou None")
        if (nationalite is not None) and (not isinstance(nationalite, str)):
            raise ValueError("l'attribut nationalite doit être du type str ou None")
        if (continent is not None) and (not isinstance(continent, str)):
            raise ValueError("l'attribut continent doit être du type str ou None")
        if (sport is not None) and (not isinstance(sport, str)):
            raise ValueError("l'attribut sport doit être du type str ou None")
        if (numero_maillot is not None) and (not isinstance(numero_maillot, int)):
            raise ValueError("l'attribut numero_maillot doit être du type int ou None")
        if (main_forte is not None) and (not isinstance(main_forte, str)):
            raise ValueError("l'attribut main_forte doit être du type str ou None")
        if (taille is not None) and (not isinstance(taille, (float, int))):
            raise ValueError("l'attribut taille doit être du type float, int ou None")
        if (poids is not None) and (not isinstance(poids, (float, int))):
            raise ValueError("l'attribut poids doit être du type str ou None")
        if (role is not None) and (not isinstance(role, str)):
            raise ValueError("l'attribut role doit être du type str ou None")
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
