import re

import pytest

from src.Model.Player import Player

"""
def test_Player_constructor_is_ok_with_valid_data():
    platoche = Player(1980, "Michel Platini", "false")
    assert platoche.id == 1980
    assert not platoche.is_the_goat


def test_player_repr_method_displays_goat_tag_for_the_goat():
    kiki = Player(2018, "Kylian Mbappé", "false")
    assert str(kiki) == "Kylian Mbappé"

    the_goat = Player(1928, "Arthur Friedenreich", True)
    assert str(the_goat) == "Arthur Friedenreich (GOAT)"
"""

def test_Player_init():
    P1 = Player(
        id=1, first_name="Edouard", last_name="Elric", sexe="M",
        dob="04-10-2003", lieu_naissance="Resembool", pseudo="ED",
        id_equipe=1, nationalite="Amestris", continent="Fictif",
        numero_maillot="66", main_forte="droite", taille=149.5,
        poid=50, role="Alchemist"
        )
    P2 = Player()
    assert P1.id == 1
    assert P1.first_name == "Edouard"
    assert P1.last_name == "Elric"
    assert P1.full_name == "Edouard Elric"
    assert P1.dob == "04-10-2003"
    assert P1.lieu_naissance == "Resembool"
    assert P2.id is None
    assert P2.last_name is None
    assert P2.first_name is None
    assert P2.full_name is None
    assert P2.lieu_naissance is None
    assert P2.pseudo is None
    assert P2.id_equipe is None
    assert P2.equipe is None
    assert P2.sexe is None
    assert P2.sexe is None
    assert P2.sexe is None
    assert P2.sexe is None