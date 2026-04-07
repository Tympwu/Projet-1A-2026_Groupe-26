from typing import Any


class Personne:

    def __init__(
        self,
        first_name: str = None,
        last_name: str = None,
        full_name: str = None,
        dob: str = None,
        lieu_naissance: str = None,
        age: str = None,
        sexe: str = None
    ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        if full_name is None:
            self.full_name = self.first_name + " " + self.last_name
        self.age = age
        self.sexe = sexe

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Personne):
            return other.full_name == self.full_name
        return NotImplemented

    def __str__(self) -> str:
        return f"""Nom: {self.full_name}\n
        Age: {self.age}\n
        Sexe: {self.sexe}\n
        Lieu de naissance: {self.lieu_naissance}."""
