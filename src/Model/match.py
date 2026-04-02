from .Equipe import Equipe


class Match:
    """"""

    def __init__(
        self, lieux_match: str, equipe1: Equipe | None = None, equipe2: Equipe | None = None,
        scores: list[int] | list[None] = [None, None], best_of: int = 1
    ) -> None:
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
        if scores[0] < 0 or scores[1] < 0:
            raise TypeError("La valeur des scores doit être un entier positif ou nul")
        if not isinstance(lieux_match, str):
            raise TypeError("L'attribut lieux_match doit être du type")
        self.equipe1 = equipe1
        self.equipe2 = equipe2
        self.best_of = best_of
        self.lieux_match = lieux_match

    @property
    def equipe1(self) -> Equipe:
        return self.equipe1

    @property
    def equipe2(self) -> Equipe:
        return self.equipe2

    @property
    def best_of(self) -> Equipe:
        return self.best_of

    @property
    def scores(self) -> list[int]:
        return self.scores

    @property
    def lieux_match(self) -> str:
        return self.lieux_match

    def __str__(self) -> str:
        return f"Voici leMatch:\n L'Equipe 1: {self.equipe1.nom}\n L'Equipe 2: {self.equipe2.nom}"
        f"best of: {self.best_of}\n scores ([Equipe 1, Equipe 2]): {self.scores}"
        f"lieux du match: {self.lieux_match}"
