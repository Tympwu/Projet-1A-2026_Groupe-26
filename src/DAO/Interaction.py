import pandas as pd
from typing import Any
from pathlib import Path


class DAO:
    def __init__(self, fichier: str, col_prive: list[str] | None = None):
        assert isinstance(fichier, str), "Le type de fichier ne correspond pas"
        assert (
            isinstance(col_prive, list) or
            col_prive is None), "Le type de col_prive ne correspond pas"

        base = Path(__file__).parent.parent.parent
        full_path = base / fichier
        self.__fichier: str = fichier
        self.__data = pd.read_csv(full_path)
        # self.__data: pd.DataFrame = pd.read_csv(fichier)
        self.__col_prive: list[str] = col_prive if col_prive is not None else []

    @property
    def data(self):
        return self.__data

    def __repr__(self):
        return f"DAO({self.__fichier}, {self.__col_prive})"

    def __str__(self):
        return self.__fichier

    def sauvegarde(self, admin=False):
        """
        Sauvegarde les données dans un csv

        Parameters
        ----------
        admin : bool, optional
            _description_, by default False
        """
        nom = input("Nom du fichier: ") + ".csv"
        if admin:
            df = self.__data
        else:
            df = self.__data.drop(columns=self.__col_prive)
        df.to_csv(nom, index=False)

    def choix_col(self, colonne: list[str]) -> pd.DataFrame:
        return self.__data[colonne]

    def filtrer(self, colonne: str, valeur: list[Any]) -> pd.DataFrame:
        """
        Filtre les lignes du DataFrame en fonction des valeurs d'une colonne en entrée

        Parameters
        ----------
        colonne : str
            Nom de la colonne sur laquelle appliquer le filtre.
        valeur : list[Any]
            Liste des valeurs à rechercher dans la colonne.

        Returns
        -------
        pd.DataFrame
            Un nouveau DataFrame contenant uniquement les lignes pour lesquelles
            la valeur de la colonne spécifiée appartient à la liste fournie.
        """
        return self.__data[self.__data[colonne].isin(valeur)]

    def inserer(self, ligne: dict[str, list[Any]] | list[dict[str, Any]]) -> None:
        """
        Insère des données dans un tableaux selon un dictionnaire en entrée

        Parameters
        ----------
        ligne : dict | list
            données à insérer, ["colonne", [valeur1, valeur2...]]
            ou [{"colonne1" : valeur1, "colonne2" : valeur2...}{"colonne1"...}...]

        """
        self.__data = pd.concat([self.__data, pd.DataFrame(ligne)], ignore_index=True)

    def modifier(self, id: int, data: dict[str, Any]) -> None:
        """
        Modifie les données du tableau selon l'id de la ligne souhaité selon
        le dictionnaire de données en entrée

        Parameters
        ----------
        id : int
            identifiant de la ligne
        data : dict
            données à modifiées, ["colonne", valeur]

        """
        if id not in self.__data.index:
            raise KeyError(f"Index {id} inexistant")
        for col, val in data.items():
            self.__data.at[id, col] = val

    def supprimer(self, id: int) -> None:
        """
        Supprime les données d'un tableau selon l'index

        Parameters
        ----------
        id : int

        """
        if id not in self.__data.index:
            raise KeyError
        self.__data = self.__data.drop(index=id).reset_index(drop=True)

    def enlever_valeur_duplique(self) -> None:
        """
        Enlève les valeurs dupliquées
        """
        self.__data.drop_duplicates(inplace=True)
        self.__data.reset_index(drop=True, inplace=True)

    def enlever_valeur_manquante(self, colonne=None) -> None:
        """
        Enlève les valeurs manquantes d'un tableau selon la colonne choisie

        Parameters
        ----------
        colonne : _type_, optional
            _description_, by default None
        """
        if colonne is None:
            self.__data.dropna(inplace=True)
        else:
            self.__data.dropna(subset=[colonne], inplace=True)
        self.__data.reset_index(drop=True, inplace=True)

    def renvoyer_types(self) -> None:
        """
        Affiche le type des données du tableau
        """
        print(self.__data.dtypes)

    def description(self) -> pd.DataFrame:
        """
        Renvoie la description des données du tableau

        Returns
        -------
        pd.DataFrame
            _description_
        """
        return self.__data.describe(include="all")
