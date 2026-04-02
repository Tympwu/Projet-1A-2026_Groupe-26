from .Equipe import Equipe


class Match(Equipe):
    """"""

    def __init__(equipe1: Equipe | None = None, equipe2: Equipe | None = None,
    scores: list[int] | list[None] = [None, None], best_of: int = 1, lieux_match: str,) -> None:
        if not isinstance(equipe1, Equipe):
            raise TypeError("l'attribut equipe1 doit être du type equipe")
        if not isinstance(equipe2, Equipe):
            raise TypeError("l'attribut equipe1 doit être du type equipe")
        if not isinstance(equipe2, Equipe):
            raise TypeError("l'attribut equipe1 doit être du type equipe")
        if not isinstance(scores, list):
            raise TypeError("l'attribut scores doit être du type list")
        if (not isinstance(scores[0], int)) or (not isinstance(scores[1], int)):
            raise TypeError("l'attribut score est une liste d'entier")
        if scores[0] < 0 or scores[1] < 0 :
            raise TypeError("La valeur des scores doit être un entier positif ou nul")
        if not isinstance(lieux_match: str) :
            raise TypeError("L'attribut lieux_match doit être du type")

        self.equipe1 = equipe1
        self.equipe2 = equipe2
        self.best_of = best_of
        self.lieux_match = lieux_match

    @property
    def equipe1() -> Equipe:
        return self.equipe1

    @property
    def equipe1() -> Equipe:
        return self.equipe1

    @property
    def equipe2() -> Equipe:
        return self.equipe2

    @property
    def scores() -> list[int]:
        return self.scores
    
    @property
    def lieux_match() -> str:
        return self.lieux_match