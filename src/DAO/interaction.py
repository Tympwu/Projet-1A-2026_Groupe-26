import pandas as pd


class DAO:
    def __init__(self, fichier: str, col_prive: list[str]):
        self.__data = pd.read_csv(fichier)
        self.__col_prive = col_prive

    def __repr__(self):
        return "DAO(" f"{self.__fichier}, " f"{self.__data_prive}" ")"

    def __str__(self):
        return self.__fichier

    def sauvegarde(self, admin=False):
        nom = input("Nom du fichier: ") + ".csv"
        if admin:
            df = self.__data
        else:
            df = self.__data.drop(columns=self.__col_prive)
        df.to_csv(nom, index=False)

    def choix_col(self, col_name):
        return self.__data[col_name]
