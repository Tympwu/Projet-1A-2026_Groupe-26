
from .Player import Player


class Equipe:
        """classe qui represente une equipe
        
        ------------------
        Parameters Equipe:

        nom_equipe: str (entre 2 et 32 caractères)
        joueurs_equipe: list(Player)
        nom_coach_equipe: Player =None
        region_equipe: str =None
        pays_equipe: str =None
        statut_equipe: str ="Casual"
        ------------

        """
    def __init__(
        self, nom_equipe: str, joueurs_equipe: list, nom_coach_equipe: str =None,
        region_equipe: str =None, pays_equipe: str =None, statut_equipe: str =None
                ) -> None:
                liste_pays = ["FRA","BEL", "GBR"]
                #liste_statut
                if not isinstance(nom_equipe, str):
                    raise TypeError("L'attribut nom_equipe doit être de type str")
                if not all(isinstance(p, Player) for p in joueurs_equipe):
                    raise TypeError("L'attribut joueurs_equipe doit être de type list de joueurs")
                if not isinstance(nom_coach_equipeoach_equipe, Player):
                    raise TypeError("L'attribut nom_coach_equipe doit être de type Player")
                if not isinstance(pays_equipe, str):
                    raise TypeError("L'attribut pays_equipe doit être de type str")
                if not pays_equipe in liste_pays:
                    raise ValueError("l'attribut pays doit être exprimer en code ISO (FRA pour France)")
                if not isinstance(statut_equipe, str):
                    raise TypeError("L'attribut statut_equipe doit être de type str ")