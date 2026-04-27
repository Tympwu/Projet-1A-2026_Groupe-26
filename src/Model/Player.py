from .Personne import Personne
from typing import Any
from tabulate import tabulate


class Player(Personne):
    """Classe représentant un joueur de n'importe quel sport.
    Cette classe hérite de la classe Personne.
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
        return str(self)

    def __str__(self) -> str:
        """Fonction permettant d'afficher une représentation d'un joueur."""
        dict_result = {
            element: [value] for element, value in self.__dict__.items() if value is not None
        }
        return tabulate(dict_result, headers="keys", tablefmt="rounded_grid")

    def __hash__(self):
        return hash(self.id)
