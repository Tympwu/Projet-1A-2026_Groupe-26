from typing import Any
from tabulate import tabulate


class Personne:
    """Définition d'une personne.

    Cette classe sert de base pour représenter une identité civile au sein
    du système. Elle gère notamment la concaténation automatique du nom complet
    si celui-ci n'est pas fourni.

    Parameters
    ----------
    first_name : str (default = None)
        Prénom de la personne.
    last_name : str (default = None)
        Nom de famille de la personne.
    full_name : str (default = None)
        Nom complet. Si None, il est construit à partir de first_name et last_name.
    dob : str (default = None)
        Date de naissance (Date of Birth).
    lieu_naissance : str (default = None)
        Ville ou pays de naissance.
    sexe : str (default = None)
        Genre de la personne.

    Examples
    --------
    >>> p1 = Personne(first_name='Jean', last_name='Pohardy')
    >>> p1.full_name
    'JeanDupont'
    >>> p2 = Personne(full_name='Alex Yu')
    >>> print(p2.full_name)
    Alex Yu
    """

    first_name: str
    last_name: str
    full_name: str
    dob: str
    lieu_naissance: str
    sexe: str

    def __init__(
        self,
        id: int = None,
        first_name: str = None,
        last_name: str = None,
        full_name: str = None,
        dob: str = None,
        lieu_naissance: str = None,
        sexe: str = None
    ) -> None:
        if (id is not None) and (not isinstance(id, int)):
            raise ValueError("l'attribut id doit être du type int ou None")
        if  (first_name is not None) and (not isinstance(first_name, str)):
            raise ValueError("l'attribut first_name doit être du type str ou None")
        if  (last_name is not None) and (not isinstance(last_name, str)):
            raise ValueError("l'attribut last_name doit être du type str ou None")
        if  (full_name is not None) and (not isinstance(full_name, str)):
            raise ValueError("l'attribut full_name doit être du type str ou None")
        if  (dob is not None) and (not isinstance(dob, str)):
            raise ValueError("l'attribut dob doit être du type str ou None")
        if  (lieu_naissance is not None) and (not isinstance(lieu_naissance, str)):
            raise ValueError("l'attribut doit être du type ou None")
        if  (sexe is not None) and (not isinstance(sexe, str)):
            raise ValueError("l'attribut sexe doit être du type str ou None")

        self.first_name = first_name
        self.last_name = last_name
        # if full_name is None:
        #     self.full_name = self.first_name + " " + self.last_name
        # else:
        #     self.full_name = full_name
        if self.first_name is not None and self.last_name is not None:
            self.full_name = self.first_name + " " + self.last_name
        else:
            self.full_name = None
        self.lieu_naissance = lieu_naissance
        self.dob = dob
        self.sexe = sexe

    def __eq__(self, other: Any) -> bool:
        """Compare deux personnes sur la base de leur nom complet.

        Parameters
        ----------
        other : Any
            L'objet à comparer avec l'instance actuelle.

        Returns
        -------
        bool
            True si 'other' est une Personne et possède le même full_name.

        Examples
        ---------
        >>> p1 = Personne(full_name='Jean Pohardy')
        >>> p2 = Personne(full_name='Jean Pohardy')
        >>> p1 == p2
        True
        """
        if isinstance(other, Personne):
            return other.full_name == self.full_name
        return NotImplemented

    def __str__(self) -> str:
        """Convertit la personne en tableau de données.

        Affiche les attributs de l'instance qui ne sont pas à None.

        Returns
        -------
        str
            Représentation tabulaire des informations de la personne.

        Examples
        ---------
        >>> p = Personne(first_name='Marc', last_name='Evans, sexe='M')
        >>> print(p)
        ╭────────────┬──────────────┬──────────────╮
        │ first_name │   last_name  │ sexe         │
        ├────────────┼──────────────┼──────────────┤
        │       Marc │     Evans    │ M            │
        ╰────────────┴──────────────┴──────────────╯
        """
        dict_result = {
            element: [value] for element, value in self.__dict__.items() if value is not None
        }
        return tabulate(dict_result, headers="keys", tablefmt="rounded_grid")
