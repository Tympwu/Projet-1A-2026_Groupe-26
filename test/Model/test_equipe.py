import re

import pytest

from src.Model.Player import Player
from src.Model.Equipe import Equipe
from src.Model.Coach import Coach

J = [Player(id=i, full_name= f"J{i}") for i in range(11)]
C = [Coach(id=i, full_name=f"C{i}") for i in range(6)]

equipe1 = Equipe(id=0,
        joueurs_equipe= {J[0],J[1]},
        coach_equipe={C[0], C[1]},
        nom_equipe= "equipe1",
        nom_abrev="E1",
        nickname="E1",
        ville_equipe="ville1",
        region_equipe="region1",
        pays_equipe="pays1",
        continent_equipe="continent1",
        ligue="ligue1",
        annee_fondation= 2000
        )

def test_equipe_init():
    assert equipe1.id == 0
    assert J[0] in equipe1.joueurs_equipe
    assert J[1] in equipe1.joueurs_equipe
    assert C[0] in equipe1.coach_equipe
    assert C[1] in equipe1.coach_equipe
    assert equipe1.nom_equipe == "equipe1"
    assert equipe1.nom_abrev == "E1"
    assert equipe1.nickname == "E1"
    assert equipe1.ville_equipe == "ville1"
    assert equipe1.region_equipe == "region1"
    assert equipe1.continent_equipe == "continent1"
    assert equipe1.ligue == "ligue1"
    assert equipe1.annee_fondation == 2000

def test_ajouter_joueur():
    equipe1.ajouter_joueur(J[3])
    assert len(equipe1.joueurs_equipe) == 3
    equipe1.ajouter_joueur(J[0])
    assert len(equipe1.joueurs_equipe) == 3

def test_ajouter_coach():
    equipe1.ajouter_coach(C[3])
    assert len(equipe1.coach_equipe) == 3
    equipe1.ajouter_coach(C[0])
    assert len(equipe1.coach_equipe) == 3


def test_equipe_str():
    e = Equipe(id=1, nom_equipe="PSG")
    attendu = (
        "╭──────┬──────────────╮\n"
        "│   id │ nom_equipe   │\n"
        "├──────┼──────────────┤\n"
        "│    1 │ PSG          │\n"
        "╰──────┴──────────────╯\n"
        "\n"
        "Joueurs :\n"
        "Aucun\n"
        "\n"
        "Coach :\n"
        "Aucun"
    )
    assert str(e).strip() == attendu.strip()