import re

import pytest

from src.Model.Coach import Coach


def test_Coach_init():
    P1 = Coach(
        id=1, first_name="Harry", last_name="Potter", sexe="M",
        dob="31-07-1980", lieu_naissance="Godric's Hollow", role="Aurore",
        nationalite="Britannique", equipe="Poudlard", pseudo="L'Élu"
        )
    P2 = Coach()
    assert P1.id == 1
    assert P1.first_name == "Harry"
    assert P1.last_name == "Potter"
    assert P1.full_name == "Harry Potter"
    assert P1.dob == "31-07-1980"
    assert P1.lieu_naissance == "Godric's Hollow"
    assert P1.role == "Aurore"
    assert P1.nationalite == "Britannique"
    assert P1.equipe == "Poudlard"
    assert P1.pseudo == "L'Élu"
    assert P2.id is None
    assert P2.last_name is None
    assert P2.first_name is None
    assert P2.full_name is None
    assert P2.lieu_naissance is None
    assert P2.sexe is None
    assert P2.role is None
    assert P2.nationalite is None
    assert P2.equipe is None
    assert P2.pseudo is None


@pytest.mark.parametrize(
    "id, first_name, last_name, sexe, dob, lieu_naissance, " +
    "role, nationalite, equipe, pseudo, message_erreur",
    [
        ("", None, None, None, None, None, None, None, None, None,
         "l'attribut id doit être du type int ou None"),
        (1, 1, None, None, None, None, None, None, None, None,
         "l'attribut first_name doit être du type str ou None"),
        (1, None, 1, None, None, None, None, None, None, None,
         "l'attribut last_name doit être du type str ou None"),
        (1, None, None, 1, None, None, None, None, None, None,
         "l'attribut sexe doit être du type str ou None"),
        (1, None, None, None, 1, None, None, None, None, None,
         "l'attribut dob doit être du type str ou None"),
        (1, None, None, None, None, 1, None, None, None, None,
         "l'attribut lieu_naissance doit être du type str ou None"),
        (1, None, None, None, None, None, True, None, None, None,
         "l'attribut role doit être du type str ou None"),
        (1, None, None, None, None, None, None, True, None, None,
         "l'attribut nationalite doit être du type str ou None"),
        (1, None, None, None, None, None, None, None, True, None,
         "l'attribut equipe doit être du type str ou None"),
        (1, None, None, None, None, None, None, None, None, True,
         "l'attribut pseudo doit être du type str ou None"),
    ],
)
def test_Coach_init_erreur(
    id, first_name, last_name, sexe, dob, lieu_naissance, role,
    nationalite, equipe, pseudo, message_erreur
        ) -> None:
    with pytest.raises(ValueError, match=re.escape(message_erreur)):
        Coach(
            id=id, first_name=first_name, last_name=last_name, sexe=sexe,
            dob=dob, lieu_naissance=lieu_naissance, role=role,
            nationalite=nationalite, equipe=equipe, pseudo=pseudo,
            )


def test_Coach_str() -> None:
    P1 = Coach(first_name="Luis", last_name="Enrique", equipe="PSG")
    assert str(P1) == (
        "╭──────────────┬─────────────┬──────────────┬──────────╮\n" +
        "│ first_name   │ last_name   │ full_name    │ equipe   │\n" +
        "├──────────────┼─────────────┼──────────────┼──────────┤\n" +
        "│ Luis         │ Enrique     │ Luis Enrique │ PSG      │\n" +
        "╰──────────────┴─────────────┴──────────────┴──────────╯")
