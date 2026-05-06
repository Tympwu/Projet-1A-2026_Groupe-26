from .Personne import Personne
from typing import Any
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
        equipe: Any = None,
        nationalite: str = None,
        pseudo: str = None,
        dob: str = None,
        sexe: str = None,
        role: str = None
    ) -> None:
        self.id = id
        super().__init__(first_name, last_name, full_name, lieu_naissance, dob, sexe)
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

        Examples
        ---------
        >>> c1 = Coach(id=7, pseudo='Pep')
        >>> print(c1)
        pseudo : Pep
        id : 7
        """
        result = ""
        for nom_argument, valeur in self.__dict__.items():
            if valeur is not None:
                result += f"\n{nom_argument} : {valeur}"
        return result

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
