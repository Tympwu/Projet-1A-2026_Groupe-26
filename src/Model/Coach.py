from .Personne import Personne
from typing import Any
from tabulate import tabulate


class Coach(Personne):
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
        
    def __str__(self) -> str:
        dict_result = {
            element: [value] for element, value in self.__dict__.items() if value is not None
        }
        return tabulate(dict_result, headers="keys", tablefmt="rounded_grid")

    def __hash__(self):
        return hash(self.id)