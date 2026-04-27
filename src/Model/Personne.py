from typing import Any
from tabulate import tabulate


class Personne:

    def __init__(
        self,
        first_name: str = None,
        last_name: str = None,
        full_name: str = None,
        dob: str = None,
        lieu_naissance: str = None,
        sexe: str = None
    ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        if full_name is None:
            self.full_name = self.first_name + " " + self.last_name
        else:
            self.full_name = full_name
        self.dob = dob
        self.sexe = sexe

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Personne):
            return other.full_name == self.full_name
        return NotImplemented

    def __str__(self) -> str:
        dict_result = {
            element: [value] for element, value in self.__dict__.items() if value is not None
        }
        return tabulate(dict_result, headers="keys", tablefmt="rounded_grid")
