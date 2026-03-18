import pandas as pd
from typing import Any


class DAO:
    def __init__(self, fichier: str, col_prive: list[str]):
        assert isinstance(fichier, str), "Le type de fichier ne correspond pas"
        assert isinstance(col_prive, list), "Le type de col_prive ne correspond pas"
        self.__fichier: str = fichier
        self.__data: pd.DataFrame = pd.read_csv(fichier)
        self.__col_prive: list[str] = col_prive

    @property
    def data(self):
        return self.__data

    def __repr__(self):
        return f"DAO({self.__fichier}, {self.__col_prive})"

    def __str__(self):
        return self.__fichier

    def sauvegarde(self, admin=False):
        nom = input("Nom du fichier: ") + ".csv"
        if admin:
            df = self.__data
        else:
            df = self.__data.drop(columns=self.__col_prive)
        df.to_csv(nom, index=False)

    def choix_col(self, colonne: list[str]) -> pd.DataFrame:
        return self.__data[colonne]

    def filtrer(self, colonne: str, valeur: list[Any]) -> pd.DataFrame:
        return self.__data[self.__data[colonne].isin(valeur)]

    def inserer(self, ligne: dict) -> None:
        self.__data = pd.concat([self.__data, pd.DataFrame([ligne])], ignore_index=True)

    def modifier(self, id: int, data: dict) -> None:
        for col, val in data.items():
            self.__data.at[id, col] = val

    def supprimer(self, id: int) -> None:
        self.__data = self.__data.drop(index=id).reset_index(drop=True)

    def enlever_valeur_duplique(self) -> None:
        self.__data = self.__data.drop_duplicates()
        self.__data = self.__data.reset_index(drop=True, inplace=True)

    def enlever_valeur_manquante(self, colonne: str | None = None) -> None:
        if colonne:
            self.__data = self.__data.dropna(subset=[colonne])
        else:
            self.__data = self.__data.dropna()
        self.__data.reset_index(drop=True, inplace=True)

    def get_types(self) -> pd.DataFrame:
        return self.__data.dtypes

    def description(self) -> pd.DataFrame:
        return self.__data.describe(include="all")
