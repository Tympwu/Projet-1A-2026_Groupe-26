from typing import Any
from abc import abstractmethod, ABC

class Graphique(ABC):
    """
    Class qui regroupe les caractéristiques commune des graphiques

    attribut:
    titre: str = "" représente le titre du graphique
    data1: list[Any] = [] représente la 1ère série de donnée
    data2: list[Any] = [] représente la 2ème série de donnée
    """

    def __init__(
        self,
        titre: str = "",
        data1: list[Any] = [],
        data2: list[Any] = []
    ) -> None:
        if not isinstance(titre, str):
            raise TypeError("l'attribut titre doit être du type str")
        if not isinstance(data1, list):
            raise TypeError("l'attribut data1 doit être du type liste")
        if not isinstance(data2, list):
            raise TypeError("l'attribut data2 doit être du type liste")
        self.titre = titre
        self.data1 = data1
        self.data2 = data2