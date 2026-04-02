import pandas as pd
from ..DAO.interaction import DAO


class Recherche:
    def __init__(self, sport: str):
        self.sport = sport
        self.dao = None

    def cherche(self):
        if self.sport == "basketball":

        if self.sport == "tennis":