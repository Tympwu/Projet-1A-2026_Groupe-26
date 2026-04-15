from match import Match


class Competition:
    def __init__(
        self,
        sport : str | None = None,
        id : int | None = None,
        nom : str | None = None,
        surface : str | None = None,
        draw_size : int | None = None,
        level : str | None = None,
        date : str | None = None
    ):
        self.id: int = id
        self.sport: str = sport
        self.nom: str = nom
        self.surface: str = surface
        self.draw_size: int = draw_size
        self.level: str = level
        self.date: str = date
        self.match: dict[str, Match] = {}

    def __str__(self):
        result = "Compétition : \n"
        for key, item  in self.__dict__.items():
            if item != None:
                result += key + " : " + str(item) + "\n"
        return result
