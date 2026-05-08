from .Personne import Personne
from tabulate import tabulate


class Coach(Personne):
    """Définition d'un coach.

    Parameters
    ----------
    id : int (default = None)
        Identifiant unique du coach.
    first_name : str (default = None)
        Prénom du coach.
    last_name : str (default = None)
        Nom de famille du coach.
    full_name : str (default = None)
        Nom complet du coach.
    lieu_naissance : str (default = None)
        Lieu de naissance du coach.
    equipe : Any (default = None)
        Équipe associée au coach.
    nationalite : str (default = None)
        Nationalité du coach.
    pseudo : str (default = None)
        Pseudonyme.
    dob : str (default = None)
        Date de naissance du coach.
    sexe : str (default = None)
        Sexe du coach.
    role : str (default = None)
        Rôle spécifique du coach.

    Examples
    --------
    >>> c1 = Coach(id=1, first_name='Zinedine', last_name='Zidane', equipe='Real Madrid')
    >>> c2 = Coach(id=2, pseudo='Special One', nationalite='Portugaise', role='Principal')
    >>> print(c1)
    id : 1
    first_name : Zinedine
    last_name : Zidane
    full_name : Zinedine Zidane
    equipe : Real Madrid
    """

    def __init__(
        self,
        id: int = None,
        first_name: str = None,
        last_name: str = None,
        full_name: str = None,
        lieu_naissance: str = None,
        equipe: str = None,
        nationalite: str = None,
        pseudo: str = None,
        dob: str = None,
        sexe: str = None,
        role: str = None
    ) -> None:

        if not (isinstance(role, str) or role is None):
            raise ValueError("l'attribut role doit être du type str ou None")
        if not (isinstance(nationalite, str) or nationalite is None):
            raise ValueError("L'attribut region doit être du type")
        if not (isinstance(equipe, str) or equipe is None):
            raise ValueError("l'attribut equipe1 doit être du type str ou None")
        if not (isinstance(pseudo, str) or pseudo is None):
            raise ValueError("l'attribut equipe1 doit être du type str ou None")
        self.id = id
        super().__init__(
            id=id,
            first_name=first_name,
            last_name=last_name,
            full_name=full_name,
            lieu_naissance=lieu_naissance,
            dob=dob,
            sexe=sexe)


        self.equipe = equipe
        self.nationalite = nationalite
        self.pseudo = pseudo
        self.role = role
        self.id = id

    def __str__(self) -> str:
        """Convertit le coach en chaîne de caractères.

        Affiche uniquement les attributs qui ne sont pas définis à None.

        Returns
        -------
        str
            Représentation textuelle du coach.
        """
        dict_result = {
            element: [value] for element, value in self.__dict__.items() if value is not None
        }
        return tabulate(dict_result, headers="keys", tablefmt="rounded_grid")

    def __hash__(self) -> int:
        """Calcule l'hash du coach.

        Returns
        -------
        int
            Hash basé sur l'identifiant unique.

        Examples
        ---------
        >>> c1 = Coach(id=10)
        >>> hash(c1) == hash(10)
        True
        """
        return hash(self.id)
