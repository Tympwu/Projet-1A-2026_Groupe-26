class Competition:
    def __init__(
        self,
        id : int | None = None,
        nom : str | None = None,
        surface : str | None = None,
        draw_size : int | None = None,
        level : str | None = None,
        date : str | None = None
    ):
        self.id = id
        self.nom = nom
        self.surface = surface
        self.draw_size = draw_size
        self.level = level
        self.date = date