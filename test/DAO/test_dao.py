import pandas as pd
import pytest
import numpy as np
from unittest.mock import patch
from src.DAO.Interaction import DAO


# Fixtures

SAMPLE_DATA = pd.DataFrame({
    "id":    [1, 2, 3, 4],
    "nom":   ["Alice", "Bob", "Charlie", "Alice"],
    "age":   [30, 25, 35, 30],
    "email": ["a@x.com", "b@x.com", "c@x.com", "a@x.com"],
})

SAMPLE_CSV = "data/test.csv"


@pytest.fixture
def dao():
    with patch("src.DAO.Interaction.pd.read_csv",
               return_value=SAMPLE_DATA.copy()):
        return DAO(SAMPLE_CSV)


@pytest.fixture
def dao_prive():
    with patch("src.DAO.Interaction.pd.read_csv",
               return_value=SAMPLE_DATA.copy()):
        return DAO(SAMPLE_CSV, col_prive=["email"])


@pytest.fixture
def dao_nan():
    donnees = pd.DataFrame({
        "id":  [1, 2, 3],
        "nom": ["Alice", None, "Charlie"],
        "age": [30, 25, np.nan],
    })
    with patch("src.DAO.Interaction.pd.read_csv",
               return_value=donnees):
        return DAO(SAMPLE_CSV)


@pytest.fixture
def dao_doublons():
    donnees = pd.DataFrame({
        "id":  [1, 1, 2],
        "nom": ["Alice", "Alice", "Bob"],
        "age": [30, 30, 25],
    })
    with patch("src.DAO.Interaction.pd.read_csv",
               return_value=donnees):
        return DAO(SAMPLE_CSV)


# test __init__

def test_init_fichier_valide(dao):
    assert dao is not None


def test_init_fichier_mauvais_type_leve_assertion():
    with patch("src.DAO.Interaction.pd.read_csv", return_value=SAMPLE_DATA.copy()):
        with pytest.raises(AssertionError):
            DAO(123)


def test_init_col_prive_liste(dao_prive):
    assert dao_prive is not None


def test_init_col_prive_none_accepte(dao):
    assert dao is not None


def test_init_col_prive_mauvais_type_leve_assertion():
    with patch("src.DAO.Interaction.pd.read_csv", return_value=SAMPLE_DATA.copy()):
        with pytest.raises(AssertionError):
            DAO(SAMPLE_CSV, col_prive="email")


def test_init_data_chargee(dao):
    assert isinstance(dao.data, pd.DataFrame)
    assert len(dao.data) == 4


# test __repr__ / __str__

def test_repr_contient_fichier(dao_prive):
    assert SAMPLE_CSV in repr(dao_prive)
    assert "email" in repr(dao_prive)


def test_str_retourne_fichier(dao):
    assert str(dao) == SAMPLE_CSV


# test data (property)

def test_data_retourne_dataframe(dao):
    assert isinstance(dao.data, pd.DataFrame)


def test_data_integrite(dao):
    pd.testing.assert_frame_equal(dao.data, SAMPLE_DATA)


# test choix_col

def test_choix_col_une_colonne(dao):
    result = dao.choix_col(["nom"])
    assert list(result.columns) == ["nom"]
    assert len(result) == 4


def test_choix_col_plusieurs_colonnes(dao):
    result = dao.choix_col(["nom", "age"])
    assert list(result.columns) == ["nom", "age"]


def test_choix_col_inexistante_leve_keyerror(dao):
    with pytest.raises(KeyError):
        dao.choix_col(["inexistante"])


# test filtrer

def test_filtrer_valeur_existante(dao):
    result = dao.filtrer("nom", ["Alice"])
    assert list(result["nom"]) == ["Alice", "Alice"]


def test_filtrer_plusieurs_valeurs(dao):
    result = dao.filtrer("nom", ["Alice", "Bob"])
    assert len(result) == 3


def test_filtrer_valeur_absente_retourne_vide(dao):
    result = dao.filtrer("nom", ["Inconnu"])
    assert len(result) == 0


def test_filtrer_colonne_numerique(dao):
    result = dao.filtrer("age", [30])
    assert len(result) == 2


# test inserer

def test_inserer_ajout_ligne(dao):
    dao.inserer({"id": [5], "nom": ["Dave"], "age": [40], "email": ["d@x.com"]})
    assert len(dao.data) == 5
    assert dao.data.iloc[-1]["nom"] == "Dave"


def test_inserer_ajout_multiple(dao):
    dao.inserer(
        {"id": [5, 6], "nom": ["Dave", "Eve"], "age": [40, 28], "email": ["d@x.com", "e@x.com"]}
    )
    assert len(dao.data) == 6


# test modifier

def test_modifier_valeur(dao):
    dao.modifier(0, {"nom": "Alicia"})
    assert dao.data.at[0, "nom"] == "Alicia"


def test_modifier_plusieurs_colonnes(dao):
    dao.modifier(1, {"nom": "Robert", "age": 99})
    assert dao.data.at[1, "nom"] == "Robert"
    assert dao.data.at[1, "age"] == 99


def test_modifier_id_inexistant_leve_keyerror(dao):
    with pytest.raises(KeyError):
        dao.modifier(999, {"nom": "X"})


# test supprimer

def test_supprimer_reduit_taille(dao):
    dao.supprimer(0)
    assert len(dao.data) == 3


def test_supprimer_reindex(dao):
    dao.supprimer(0)
    assert list(dao.data.index) == [0, 1, 2]


def test_supprimer_bonne_ligne(dao):
    nom_ligne_1 = dao.data.at[1, "nom"]
    dao.supprimer(0)
    assert dao.data.at[0, "nom"] == nom_ligne_1


def test_supprimer_id_inexistant_leve_keyerror(dao):
    with pytest.raises(KeyError):
        dao.supprimer(999)


# test enlever_valeur_duplique

def test_enlever_duplique_supprime_doublons(dao_doublons):
    dao_doublons.enlever_valeur_duplique()
    assert len(dao_doublons.data) == 2


def test_enlever_duplique_reindex(dao_doublons):
    dao_doublons.enlever_valeur_duplique()
    assert list(dao_doublons.data.index) == list(range(len(dao_doublons.data)))


def test_enlever_duplique_sans_doublons_aucun_changement(dao):
    taille_avant = len(dao.data)
    dao.enlever_valeur_duplique()
    assert len(dao.data) == taille_avant


# test enlever_valeur_manquante

def test_enlever_nan_sans_colonne(dao_nan):
    dao_nan.enlever_valeur_manquante()
    assert len(dao_nan.data) == 1
    assert not dao_nan.data.isnull().values.any()


def test_enlever_nan_avec_colonne(dao_nan):
    dao_nan.enlever_valeur_manquante("nom")
    assert len(dao_nan.data) == 2


def test_enlever_nan_reindex(dao_nan):
    dao_nan.enlever_valeur_manquante()
    assert list(dao_nan.data.index) == list(range(len(dao_nan.data)))


def test_enlever_nan_sans_nan_aucun_changement(dao):
    taille_avant = len(dao.data)
    dao.enlever_valeur_manquante()
    assert len(dao.data) == taille_avant


# test description

def test_description_retourne_dataframe(dao):
    assert isinstance(dao.description(), pd.DataFrame)


def test_description_contient_count(dao):
    assert "count" in dao.description().index


# test sauvegarde

def test_sauvegarde_sans_col_privees(dao_prive, tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr("builtins.input", lambda _: "sortie")
    dao_prive.sauvegarde(admin=False)
    df = pd.read_csv(tmp_path / "sortie.csv")
    assert "email" not in df.columns


def test_sauvegarde_admin_inclut_col_privees(dao_prive, tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr("builtins.input", lambda _: "sortie_admin")
    dao_prive.sauvegarde(admin=True)
    df = pd.read_csv(tmp_path / "sortie_admin.csv")
    assert "email" in df.columns
