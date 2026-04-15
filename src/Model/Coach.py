
from .Personne import Personne
from typing import Any


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
        super().__init__(first_name, last_name, full_name, lieu_naissance, dob, sexe)
        self.equipe = equipe
        self.nationalite = nationalite
        self.pseudo = pseudo
        self.role = role
        self.id = id
    def __str__(self) -> str:
        result = ""
        for nom_argument, valeur in self.__dict__.items():
            if valeur is not None:
                result += f"\n{nom_argument} : {valeur}"
        return result

    def __hash__(self):
        return hash(self.id)