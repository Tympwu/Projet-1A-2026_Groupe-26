import pandas as pd
from typing import Any


class DAO:
    def __init__(self, fichier: str, col_prive: list[str]):
        self.__fichier = fichier
        self.__data = pd.read_csv(fichier)
        self.__col_prive = col_prive

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

    def choix_col(self, col_name: list[str]) -> pd.DataFrame:
        return self.__data[col_name]

    def filtrer(self, colonne: str, valeur: list[Any]) -> pd.DataFrame:
        return self.__data[self.__data[colonne].isin(valeur)]

    def inserer(self, row: dict) -> None:
        self.__data = pd.concat([self.__data, pd.DataFrame([row])], ignore_index=True)

    def modifier(self, id: int, data: dict) -> None:
        for col, val in data.items():
            self.__data.at[id, col] = val

    def supprimer(self, id: int) -> None:
        self.__data = self.__data.drop(index=id).reset_index(drop=True)

    def nettoyer(self) -> None:
        self.__data.drop_duplicates(inplace=True)
        self.__data.dropna(inplace=True)
        self.__data.reset_index(drop=True, inplace=True)

    def get_types(self) -> pd.Series:
        return self.__data.dtypes

    def description(self) -> pd.DataFrame:
        return self.__data.describe(include="all")
