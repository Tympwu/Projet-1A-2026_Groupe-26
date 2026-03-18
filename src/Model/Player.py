
from .Personne import Personne


class Player(Personne):
    def __init__(
        self,
        id: int,
        full_name: str,
        sport: str,
        age: int,
        etat_physique: str = None,
        sexe: str = None,
        palmares: int = None
    ) -> None:
        super().__init__(full_name, age, sexe)
        if not isinstance(id, int):
            raise TypeError("'id' doit être une instance de int")
        if not isinstance(sport, str):
            raise TypeError("'sport' doit être une instance de str")
        if not isinstance(etat_physique, str) and etat_physique in ("blesse", "en_forme", None):
            raise TypeError("'etat_physique' doit être une instance de etat_physique dans ('blesse', 'en_forme', None)")
        if not isinstance(palmares, int):
            raise TypeError("palamares doit être une instance de int")
        self.id = id
        self.sport = sport
        self.palmares = palmares
        self.etat_physique = etat_physique
    
    def __repr__(self) -> str:
        return f"Nom:{self.full_name}, Sport:{self.sport}"

    def __str__(self) -> str:
        return f"Le joueur s'appelle {self.full_name} et se distingue en {self.sport}."

    def victoire_finale(self) -> None:
        if self.palmares is None:
            self.palmares = 1
        else:
            self.palmares += 1

    def set_palmares(self, valeur: int) -> None:
        for _ in range(valeur):
            self.victoire_finale

    def blessure(self) -> None:
        if self.etat_physique == "en_forme" or self.etat_physique is None:
            self.blesse = "blesse"

    def retabli(self) -> None:
        if self.etat_physique == "blesse" or self.etat_physique is None:
            self.etat_physique = "en_forme"
