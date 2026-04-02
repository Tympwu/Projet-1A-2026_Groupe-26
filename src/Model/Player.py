
from .Personne import Personne


class Player(Personne):
    def __init__(
        self,
        id: int,
        full_name: str,
        sport: str,
        age: int,
        blessé: bool = False,
        sexe: str = None,
        palmares: list[str] = None
    ) -> None:
        super().__init__(full_name, age, sexe)
        if not isinstance(id, int):
            raise TypeError("'id' doit être une instance de int")
        if not isinstance(sport, str):
            raise TypeError("'sport' doit être une instance de str")
        if not isinstance(blessé, str) and blessé in ("blesse", "en_forme", None):
            raise TypeError("'etat_physique' doit être une instance de etat_physique dans ('blesse', 'en_forme', None)")
        if not all(isinstance(p, str) for p in palmares):
            raise TypeError("palamares doit être une liste de str")
        self.id = id
        self.sport = sport
        self.palmares = palmares
        self.blessé = blessé
    
    def __repr__(self) -> str:
        return f"Player( Nom:{self.full_name}, Sport:{self.sport})"

    def __str__(self) -> str:
        return f"""Nom joueu{"se" if self.sexe == "femme" else "r"}: {self.full_name}\n
        ID: {self.id}\n
        Sport: {self.sport}\n
        Age: {self.age} ans\n
        Palmarès: {self.palmares}\n
        Blessé{"e" if self.sexe == "femme" else ""}: {"Oui" if self.blessé is True else "Non"}."""

    def victoire_finale(self) -> None:
        if self.palmares is None:
            self.palmares = 1
        else:
            self.palmares += 1

    def set_palmares(self, valeur: int) -> None:
        for _ in range(valeur):
            self.victoire_finale

    def blessure(self) -> None:
        if self.etat_physique == "en forme" or self.etat_physique is None:
            self.blesse = "blessé"

    def retabli(self) -> None:
        if self.etat_physique == "blessé" or self.etat_physique is None:
            self.etat_physique = "en forme"
