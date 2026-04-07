from typing import Any


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
        self.full_name = full_name
        self.dob = dob
        self.sexe = sexe

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Personne):
            return other.full_name == self.full_name
        return NotImplemented

    def __str__(self) -> str:
        result = ""
        for nom_argument, valeur in self.__dict__.items():
            if valeur is not None:
                result += f"\n{nom_argument} : {valeur}"
        return result
