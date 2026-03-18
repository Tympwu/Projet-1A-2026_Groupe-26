from typing import Any


class Personne:

    def __init__(self, full_name: str,  age: int, sexe: str = None) -> None:
        if not isinstance(full_name, str):
            raise TypeError("'full_name' doit être une instance de str")
        if not isinstance(sexe, str) and sexe in ("femme", "homme", None):
            raise TypeError("'sexe' doit être une instance de str dans 'femme', 'homme' ou None")
        if not isinstance(age, int):
            raise TypeError("'age' doit être une instance de int")
        self.full_name = full_name
        self.age = age
        self.sexe = sexe

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Personne):
            return other.full_name == self.full_name
        return NotImplemented

    def __str__(self) -> str:
        return f'Le nom complet de cette personne est {self.full_name}.'
