import pytest

from src.Model.Match import Match
from src.Model.Equipe import Equipe
from src.Model.Player import Player


# ---------- Fixtures ----------

@pytest.fixture
def equipe1():
    return Equipe(id=1, nom_equipe="Team A")


@pytest.fixture
def equipe2():
    return Equipe(id=2, nom_equipe="Team B")


@pytest.fixture
def joueur1():
    return Player(id=1, full_name="Alice")


@pytest.fixture
def joueur2():
    return Player(id=2, full_name="Bob")


# ---------- Tests constructeur ----------

def test_creation_match_valide(equipe1, equipe2):
    match = Match(
        id_match=1,
        equipe1=equipe1,
        equipe2=equipe2,
        best_of=3
    )

    assert match.id_match == 1
    assert match.equipe1 == equipe1
    assert match.equipe2 == equipe2
    assert match.best_of == 3


def test_creation_match_equipes_identiques(equipe1):
    with pytest.raises(ValueError):
        Match(
            equipe1=equipe1,
            equipe2=equipe1
        )


def test_creation_match_joueurs_identiques(joueur1):
    with pytest.raises(ValueError):
        Match(
            joueur1=joueur1,
            joueur2=joueur1
        )


def test_creation_match_id_invalide():
    with pytest.raises(TypeError):
        Match(id_match="abc")


# ---------- Tests ajouter_scores ----------

def test_ajouter_scores_valide(equipe1, equipe2):
    match = Match(
        equipe1=equipe1,
        equipe2=equipe2,
        best_of=3
    )

    match.ajouter_scores(2, 1)

    assert match.score1 == 2
    assert match.score2 == 1


def test_ajouter_scores_negatif(equipe1, equipe2):
    match = Match(
        equipe1=equipe1,
        equipe2=equipe2
    )

    with pytest.raises(ValueError):
        match.ajouter_scores(-1, 2)


def test_ajouter_scores_deja_existants(equipe1, equipe2):
    match = Match(
        equipe1=equipe1,
        equipe2=equipe2,
        score1=1,
        score2=0
    )

    with pytest.raises(ValueError):
        match.ajouter_scores(2, 1)


def test_ajouter_scores_incompatibles(equipe1, equipe2):
    match = Match(
        equipe1=equipe1,
        equipe2=equipe2,
        best_of=3
    )

    with pytest.raises(ValueError):
        match.ajouter_scores(3, 0)


# ---------- Tests gagnant/perdant ----------

def test_renvoyer_joueur_gagnant(joueur1, joueur2):
    match = Match(
        joueur1=joueur1,
        joueur2=joueur2,
        score1=2,
        score2=1
    )

    gagnant = match.renvoyer_joueur_gagnant()

    assert gagnant == joueur1


def test_renvoyer_joueur_perdant(joueur1, joueur2):
    match = Match(
        joueur1=joueur1,
        joueur2=joueur2,
        score1=2,
        score2=1
    )

    perdant = match.renvoyer_joueur_perdant()

    assert perdant == joueur2


def test_renvoyer_gagnant_sans_score(equipe1, equipe2):
    match = Match(
        equipe1=equipe1,
        equipe2=equipe2
    )

    with pytest.raises(ValueError):
        match.renvoyer_equipe_gagnante()