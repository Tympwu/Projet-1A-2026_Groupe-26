
from .Personne import Personne
from typing import Any


class Coach(Personne):
    def __init__(
        self,
        full_name: str,
        equipe: Any,
        nationalite: str = None,
        pseudo: str = None,
        dob: str = None,
        sexe: str = None,
    ) -> None:
        super().__init__(full_name, age, sexe)