
from .Personne import Personne


class Coach(Personne):
    def __init__(
        self,
        full_name: str,
        age: int,
        sexe: str = None,
        palmares_coach: int = None
    ) -> None:
        super().__init__(full_name, age, sexe)
        if not isinstance(palmares_coach, int):
            raise TypeError("palamres_coach doit être une instance de int")
        self.palamres_coach = palmares_coach
   
    def victoire_finale_coach(self) -> None:
        if self.palmares is None:
            self.palmares = 1
        else:
            self.palmares += 1

    def set_palmares_coach(self, valeur: int) -> None:
        for _ in range(valeur):
            self.victoire_finale_coach
