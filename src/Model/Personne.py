from typing import Any


class Personne:

    def __init__(self, first_name: str, last_name: str,  age: int, sexe: str = None) -> None:
        if not isinstance(first_name, str):
            raise TypeError("'first_name' doit être une instance de str")
        if not isinstance(sexe, str) and sexe in ("femme", "homme", None):
            raise TypeError("'sexe' doit être une instance de str dans 'femme', 'homme' ou None")
        if not isinstance(age, int):
            raise TypeError("'age' doit être une instance de int")
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sexe = sexe

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Personne):
            return other.full_name == self.full_name
        return NotImplemented

    def __str__(self) -> str:
        return f"""Nom: {self.first_name} {self.last_name}\n
        Age: {self.age}\n
        Sexe: {self.sexe}."""
