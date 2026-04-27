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
        continent: str = None,
        sport: str = None,
        numero_maillot: int = None,
        main_forte: str = None,
        taille: int = None,
        poids: int = None,
        stat: dict[str, int] = None,
        role: str = None
    ) -> None:
        super().__init__(
            first_name=first_name, last_name=last_name, full_name=full_name,
            lieu_naissance=lieu_naissance, dob=dob, sexe=sexe
        )
        self.id = id
        self.pseudo = pseudo
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
        result = ""
        for nom_argument, valeur in self.__dict__.items():
            if valeur is None:
                continue
            else:
                result += f"\n{nom_argument} : {valeur} | "
        return result

    def __hash__(self):
        return hash(self.id)