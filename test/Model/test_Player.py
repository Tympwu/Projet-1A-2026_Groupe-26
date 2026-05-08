import re

import pytest

from src.Model.Player import Player


def test_Player_init():
    P1 = Player(
        id=1, first_name="Edouard", last_name="Elric", sexe="M",
        dob="04-10-2003", lieu_naissance="Resembool", pseudo="ED",
        id_equipe=1, nationalite="Amestris", continent="Fictif",
        numero_maillot=66, main_forte="droite", taille=149.5,
        poids=50, role="Alchemist"
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


@pytest.mark.parametrize(
    "pseudo, id_equipe, nationalite, continent, numero_maillot, " +
    "main_forte, taille, role, poids, message_erreur",
    [
        (1, None, None, None, None, None, None, None, None,
         "l'attribut pseudo doit être du type str ou None"),
        (None, [], None, None, None, None, None, None, None,
         "l'attribut id_equipe doit être du type int ou None"),
        (None, None, {}, None, None, None, None, None, None,
         "l'attribut nationalite doit être du type str ou None"),
        (None, None, None, 1, None, None, None, None, None,
         "l'attribut continent doit être du type str ou None"),
        (None, None, None, None, "", None, None, None, None,
         "l'attribut numero_maillot doit être du type int ou None"),
        (None, None, None, None, None, 15, None, None, None,
         "l'attribut main_forte doit être du type str ou None"),
        (None, None, None, None, None, None, "", None, None,
         "l'attribut taille doit être du type float, int ou None"),
        (None, None, None, None, None, None, None, 12, None,
         "l'attribut role doit être du type str ou None"),
        (None, None, None, None, None, None, None, None, "",
         "l'attribut poids doit être du type str ou None"),
    ],
)
def test_Personne_init_erreur(
    pseudo, id_equipe, nationalite, continent, numero_maillot,
    main_forte, taille, role, poids, message_erreur
        ) -> None:
    with pytest.raises(ValueError, match=re.escape(message_erreur)):
        Player(
            pseudo=pseudo, id_equipe=id_equipe, nationalite=nationalite,
            continent=continent, numero_maillot=numero_maillot,
            main_forte=main_forte, taille=taille, role=role, poids=poids
            )


def test_Player_str() -> None:
    P1 = Player(first_name="Marc", last_name="Evans", sexe="M")
    assert str(P1) == (
        "╭──────────────┬─────────────┬─────────────┬────────╮\n" +
        "│ first_name   │ last_name   │ full_name   │ sexe   │\n" +
        "├──────────────┼─────────────┼─────────────┼────────┤\n" +
        "│ Marc         │ Evans       │ Marc Evans  │ M      │\n" +
        "╰──────────────┴─────────────┴─────────────┴────────╯")
