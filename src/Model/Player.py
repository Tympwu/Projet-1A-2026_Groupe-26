
from .Personne import Personne
from typing import Any


class Player(Personne):
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
        equipe: Any = None,
        nationalite: str = None,
        sport: str = None,
        poste: str = None,
        numero_maillot: int = None,
        main_forte: str = None,
        taille: int = None,
        poids: int = None,
        stat: dict[str, int] = None,
        role: str = None
    ) -> None:
        super().__init__(first_name, last_name, full_name, lieu_naissance, age, sexe)
        self.id = id
        self.pseudo = pseudo
        self.equipe = equipe
        self.nationalite_equipe = nationalite
        self.sport = sport
        self.poste = poste
        self.numero_maillot = numero_maillot
        self.main_forte = main_forte
        self.taille = taille
        self.poids = poids
        self.stat = stat
        self.role =
    
    def __repr__(self) -> str:
        return f"Player( Nom:{self.full_name}, Sport:{self.sport})"

    def __str__(self) -> str:
        return f"""Nom joueu{"se" if self.sexe == "femme" else "r"}: {self.first_name} {self.last_name}\n
        ID: {self.id}\n
        Sport: {self.sport}\n
        Age: {self.age} ans\n
        """

