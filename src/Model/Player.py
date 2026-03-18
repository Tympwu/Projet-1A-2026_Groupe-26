
from .Personne import Personne


class Player(Personne):
    def __init__(self, id: int, full_name: str, sport: str, age: int, blesse: int = 0, sexe: str = None, palmares: int = 0):
        super().__init__(full_name, age, sexe)
        if not isinstance(id, int):
            raise TypeError("'id' doit être une instance de int")
        if not isinstance(sport, str):
            raise TypeError("'sport' doit être une instance de str")
        if not isinstance(blesse, int) and blesse in (0, 1):
            raise TypeError("'blesse' doit être une instance de int dans (0, 1)")
        self.id = id
        self.palmares = palmares
        self.blesse = blesse
      
    def __repr__(self):
        return f"Nom:{self.full_name}, Id:{self.id}, Sport:{self.sport}"

    def __str__(self):
        return f"Le joueur {self.id} s'appelle {self.full_name} et se distingue en {self.sport}."

    def victoire_finale(self):
        self.palmares += 1

    def blessure(self):
        if self.blesse == 0:
            self.blesse = 1

    def retabli(self):
        if self.blesse == 1:
            self.blesse = 0
