
from .Personne import Personne


class Player(Personne):
    def __init__(
        self,
        id: int,
        first_name: str = None,
        last_name: str = None,
        full_name: str = None,
        pseudo: str = None,
        equipe: str = None,
        nationalite_equipe: str = None,
        lieu_naissance: str = None,
        sport: str = None,
        age: int = None,
        poste: str = None,
        numero_maillot: int = None,
        main_forte: str = None,
        taille: int = None,
        poids: int = None,
        blessé: bool = False,
        sexe: str = None,
        palmares: list[str] = None
    ) -> None:
        super().__init__(first_name, last_name, age, sexe)
        if not isinstance(id, int):
            raise TypeError("'id' doit être une instance de int")
        if not isinstance(sport, str):
            raise TypeError("'sport' doit être une instance de str")
        if not isinstance(blessé, str) and blessé in ("blesse", "en_forme", None):
            raise TypeError("'etat_physique' doit être une instance de etat_physique dans ('blesse', 'en_forme', None)")
        if not all(isinstance(p, str) for p in palmares):
            raise TypeError("palmares doit être une liste de str")
        self.id = id
        self.sport = sport
        self.palmares = palmares
        self.blessé = blessé
    
    def __repr__(self) -> str:
        return f"Player( Nom:{self.full_name}, Sport:{self.sport})"

    def __str__(self) -> str:
        return f"""Nom joueu{"se" if self.sexe == "femme" else "r"}: {self.first_name} {self.last_name}\n
        ID: {self.id}\n
        Sport: {self.sport}\n
        Age: {self.age} ans\n
        Palmarès: {self.palmares}\n
        Blessé{"e" if self.sexe == "femme" else ""}: {"Oui" if self.blessé is True else "Non"}."""

    def blessure(self) -> None:
        if self.blessé is False or self.blessé is None:
            self.blessé = True

    def retabli(self) -> None:
        if self.blessé is True or self.blessé is None:
            self.blessé = False
