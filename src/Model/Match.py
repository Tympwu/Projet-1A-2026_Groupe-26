from .Equipe import Equipe
from tabulate import tabulate

from .Player import Player


class Match:
    """
    Classe représentant un match
    """
    def __init__(
        self,
        id_match: int | None = None,
        region: str | None = None,
        equipe1: Equipe | None = None,
        equipe2: Equipe | None = None,
        joueur1: Player | None = None,
        joueur2: Player | None = None,
        score1: int | None = None,
        score2: int | None = None,
        best_of: int = 1,
        date_match: str | None = None,
        temps_match: str | None = None,
    ) -> None:
    
        if not (isinstance(id_match, int) or id_match is None):
            raise TypeError("l'attribut id_match doit être du type int ou None")
        if not (isinstance(region, str) or region is None):
            raise TypeError("L'attribut region doit être du type")
        if not (isinstance(equipe1, Equipe) or equipe1 is None):
            raise TypeError("l'attribut equipe1 doit être du type equipe ou None")
        if not (isinstance(equipe2, Equipe) or equipe2 is None):
            raise TypeError("l'attribut equipe1 doit être du type equipe ou None")
        if (equipe1 is not None) and (equipe2 is not None) and (equipe1 == equipe2):
            raise ValueError(
                "les attributs equipe1 et equipe2 doivent être différent s'ils sont renseignés"
                )
        if not (isinstance(joueur1, Player) or joueur1 is None):
            raise TypeError("l'attribut joueur1 doit être du type Player ou None")
        if not (isinstance(joueur2, Player) or joueur2 is None):
            raise TypeError("l'attribut joueur2 doit être du type Player ou None")
        if (joueur1 is not None) and (joueur2 is not None) and (joueur1 == joueur2):
            raise ValueError(
                "les attributs joueur1 et joureur2 doivent être différent s'ils sont renseignés"
                )
        if not (isinstance(score1, int) or score1 is None):
            raise ValueError("l'attribut score1 doit être un entier naturel positif")
        if not (isinstance(score2, int) or score2 is None):
            raise ValueError("l'attribut score2 doit être un entier naturel positif")
        if not (isinstance(best_of, int) or best_of is None) or best_of < 0:
            raise ValueError("l'attribut best_of doit être un entier naturel positif")
        if not (isinstance(date_match, str) or date_match is None):
            raise TypeError("l'attribut date_match doit être du type str")
        if not (isinstance(temps_match, str) or temps_match is None):
            raise ValueError("l'attribut temps_match doit être du type str")
        self.id_match = id_match
        self.region = region
        self.equipe1 = equipe1
        self.equipe2 = equipe2
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.score1 = score1
        self.score2 = score
        self.best_of = best_of
        self.date_match = date_match
        self.temps_match = temps_match

    def __str__(self) -> str:
        if self.equipe1 is None:
            participants = {
                "id": [self.joueur1.id, self.joueur2.id],
                "nom": [self.joueur1.full_name, self.joueur2.full_name],
                "score": [self.score1, self.score2]
            }
        else:
            participants = {
                "id": [self.equipe1.id, self.equipe2.id],
                "nom": [self.equipe1.nom_equipe, self.equipe2.nom_equipe],
                "score": [self.score1, self.score2]
            }

        dict_result = {
            element: [value] for element, value in self.__dict__.items()
            if not ((value is None) or (element in {
                "equipe1", "equipe2", "joueur1", "joueur2",
                "score1", "score2", "score"
                })
                )
        }

        tab_match = tabulate(dict_result, headers="keys", tablefmt="rounded_grid")
        tab_score = tabulate(participants, headers="keys", tablefmt="rounded_grid")
        return f"{tab_match}\n\nParticipants :\n{tab_score}"

    def ajouter_scores(self, score1: int, score2: int) -> None:
        """
        Permet d'ajouter le score du match entre les 2 équipes (renseignés au prealable)

        Parameters:
        -----------
        - score1: int
        - score2: int

        Return:
        -------
        None
        """
        if (not isinstance(score1, int)) or score1 < 0:
            raise ValueError("l'attribut score1 est un entier positif")
        if (not isinstance(score2, int)) or score2 < 0:
            raise ValueError("l'attribut score2 est un entier positif")
        if self.equipe1 is None:
            raise ValueError("l'attribut equipe1 du match vaut None")
        if self.equipe2 is None:
            raise ValueError("l'attribut equipe2 du match vaut None")
        if (self.score1 is not None) or (self.score2 is not None):
            raise ValueError("les scores ont déjà été enregistrés")
        if score1 + score2 == self.best_of:
            self.score1 = score1
            self.score2 = score2
        else:
            if max(score1, score2) == (self.best_of + 1) / 2:
                self.score1 = score1
                self.score2 = score2
            else:
                raise ValueError("score non compatible avec le format (attribut best_of)")

    def renvoyer_equipe_gagnante(self) -> Equipe | None:
        """
        Permet une fois les équipes d'un match et leurs scores renseignés de renvoyé l'equipe
        gagnante

        Return:
        -------
        Equipe

        """
        if self.score1 is None or self.score2 is None:
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
            if self.score2 > self.score1:
                return self.equipe1
            else:
                return self.equipe2

    def renvoyer_joueur_gagnant(self) -> Player | None:
        """
        Permet une fois les joueurs d'un match et leurs scores renseignés de renvoyé le joueur
        gagnant

        Return:
        -------
        Equipe

        """
        if self.score1 is None or self.score2 is None:
            raise ValueError("les scores n'ont pas été mis")
        else:
            if self.score1 > self.score2:
                return self.joueur1
            else:
                return self.joueur2

    def renvoyer_joueur_perdant(self) -> Equipe | None:
        """
        Permet une fois les joueurs d'un match et leurs scores renseignés de renvoyé le joueur
        perdant

        Return:
        -------
        Equipe

        """
        if self.score1 is None or self.score2 is None:
            raise ValueError("les scores n'ont pas été mis")
        else:
            if self.score2 > self.score1:
                return self.joueur1
            else:
                return self.joueur2
