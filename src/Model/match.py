from .Equipe import Equipe


class Match:
    """"""

    def __init__(
        self, id_match: int, lieux_match: str, equipe1: Equipe | None = None,
        equipe2: Equipe | None = None, score_equipe1: int | None = None,
        score_equipe2: int | None = None, best_of: int = 1
    ) -> None:
        if not (isinstance(equipe1, Equipe) or equipe1 is None):
            raise TypeError("l'attribut equipe1 doit être du type equipe ou None")
        if not (isinstance(equipe2, Equipe) or equipe2 is None):
            raise TypeError("l'attribut equipe1 doit être du type equipe ou None")
        if (equipe1 is not None) and (equipe2 is not None) and (equipe1 == equipe2):
            raise ValueError(
                "les attributs equipe1 et equipe2 doivent être différent s'ils sont renseignés"
                )
        if not (isinstance(score_equipe1, int) or score_equipe1 is None) or score_equipe1 < 0:
            raise ValueError("l'attribut score_equipe1 doit être un entier naturel positif")
        if not (isinstance(score_equipe2, int) or score_equipe2 is None) or score_equipe2 < 0:
            raise ValueError("l'attribut score_equipe2 doit être un entier naturel positif")
        if not isinstance(lieux_match, str):
            raise TypeError("L'attribut lieux_match doit être du type")
        self.equipe1 = equipe1
        self.equipe2 = equipe2
        self.best_of = best_of
        self.lieux_match = lieux_match
        self.score_equipe1 = score_equipe1
        self.score_equipe2 = score_equipe2

    @property
    def equipe1(self) -> Equipe | None:
        return self.equipe1

    @property
    def equipe2(self) -> Equipe | None:
        return self.equipe2

    @property
    def best_of(self) -> Equipe | None:
        return self.best_of

    @property
    def score_equipe1(self) -> int | None:
        return self.score_equipe1

    def score_equipe2(self) -> int | None:
        return self.score_equipe2

    @property
    def lieux_match(self) -> str:
        return self.lieux_match

    def __str__(self) -> str:
        return f"Voici le Match:\nL'Equipe 1: {self.equipe1.nom}\nL'Equipe 2: {self.equipe2.nom}"
        f"best of: {self.best_of}\nscore equipe 1: {self.score_equipe1}\n"
        f"score equipe2: {self.score_equipe2}\nlieux du match: {self.lieux_match}"

    def ajouter_equipe1(self, equipe1: Equipe) -> None:
        """
        Permet d'ajouter l'équipe1 au match

        Parameter:
        ----------
        - equipe1: Equipe

        Return:
        -------
        None
        """
        if not isinstance(equipe1, Equipe):
            raise TypeError("l'attribut equipe1 est du type Equipe")
        if self.equipe1 is not None:
            raise ValueError("l'attribut equipe1 est déjà fournit dans le match")
        if equipe1 == self.equipe2:
            raise ValueError(
                "l'attribut equipe1 est déjà fournit dans le match (c'est la 2eme equipe)"
                )
        self.equipe1 = equipe1

    def ajouter_equipe2(self, equipe2: Equipe) -> None:
        """
        Permet d'ajouter l'équipe2 au match

        Parameter:
        ----------
        - equipe2: Equipe

        Return:
        -------
        None
        """
        if not isinstance(equipe2, Equipe):
            raise TypeError("l'attribut equipe2 est du type Equipe")
        if self.equipe_1 is not None:
            raise ValueError("l'attribut equipe_1 est déjà fournit dans le match")
        if equipe2 == self.equipe1:
            raise ValueError(
                "l'attribut equipe2 est déjà fournit dans le match (c'est la 1ère equipe)"
                )
        self.equipe2 = equipe2

    def ajouter_equipes(self, equipe1: Equipe, equipe2: Equipe) -> None:
        """
        Permet d'ajouter les 2 équipes du match

        Parameters:
        -----------
        -equipe1: Equipe
        -equipe2: Equipe

        Return:
        -------
        None
        """
        self.ajouter_equipe1(equipe1)
        self.ajouter_equipe2(equipe2)

    def ajouter_scores(self, score_equipe1: int, score_equipe2: int) -> None:
        """
        Permet d'ajouter le score du match entre les 2 équipes (renseignés au prealable)

        Parameters:
        -----------
        - score_equipe1: int
        - score_equipe2: int

        Return:
        -------
        None
        """
        if (not isinstance(score_equipe1, int)) or score_equipe1 < 0:
            raise ValueError("l'attribut score_equipe1 est un entier positif")
        if (not isinstance(score_equipe2, int)) or score_equipe2 < 0:
            raise ValueError("l'attribut score_equipe2 est un entier positif")
        if self.equipe_1 is None:
            raise ValueError("l'attribut equipe1 du match vaut None")
        if self.equipe_2 is None:
            raise ValueError("l'attribut equipe2 du match vaut None")
        if (self.score_equipe1 is not None) or (self.score_equipe2 is not None):
            raise ValueError("les scores ont déjà été enregistrés")
        if score_equipe1 + score_equipe2 == self.best_of:
            self.score_equipe1 = score_equipe1
            self.score_equipe2 = score_equipe2
        else:
            if max(score_equipe1, score_equipe2) == (self.best_of + 1) / 2:
                self.score_equipe1 = score_equipe1
                self.score_equipe2 = score_equipe2
            else:
                raise ValueError("score non compatible avec le format (attribut best_of)")

    def ajouter_equipes_et_scores(
        self, equipe1: Equipe, equipe2: Equipe,
        score_equipe1: int, score_equipe2: int
            ) -> None:
        """
        Permet d'ajouter les équipes d'un match ainsi que leurs scores

        Parameters:
        -----------
        - score_equipe1: int
        - score_equipe2: int
        -equipe1: Equipe
        -equipe2: Equipe

        Return:
        -------
        None
        """
        self.ajouter_equipes(equipe_1=equipe1, equipe_2=equipe2)
        self.ajouter_scores(score_equipe_1=score_equipe1, score_equipe_2=score_equipe2)

    def renvoyer_equipe_gagnante(self) -> Equipe | None:
        """
        Permet une fois les équipes d'un match et leurs scores renseignés de renvoyé l'equipe
        gagnante

        Return:
        -------
        Equipe

        """
        if self.score_equipe1 is None or self.score_equipe2 is None:
            raise ValueError("les scores n'ont pas été mis")
        else:
            if self.score_equipe_1 > self.score_equipe_2:
                return self.equipe_1
            else:
                return self.equipe_2

    def renvoyer_equipe_perdante(self) -> Equipe | None:
        """
        Permet une fois les équipes d'un match et leurs scores renseignés de renvoyé l'equipe
        perdante

        Return:
        -------
        Equipe

        """
        if self.score_equipe_1 is None or self.score_equipe_2 is None:
            raise ValueError("les scores n'ont pas été mis")
        else:
            if self.score_equipe2 > self.score_equipe1:
                return self.equipe1
            else:
                return self.equipe2
