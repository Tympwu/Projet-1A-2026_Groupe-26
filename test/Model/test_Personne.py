from src.Model.Personne import Personne


def test_Personne_init():
    P1 = Personne(
        id=1, first_name="Edouard", last_name="Elric", sexe="M",
        dob="04-10-2003", lieu_naissance="Resembool"
        )
    P2 = Personne()
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
    assert P2.sexe is None


@pytest.mark.parametrize(
    "id, first_name, last_name, sexe, dob, lieu_naissance, message_erreur",
    [
        ("", None, None, None, None, None, "l'attribut id doit être du type int ou None"),
        (1, 1, None, None, None, None, "l'attribut first_name doit être du type str ou None"),
        (1, None, 1, None, None, None, "l'attribut last_name doit être du type str ou None"),
        (1, None, None, 1, None, None, "l'attribut sexe doit être du type str ou None"),
        (1, None, None, None, 1, None, "l'attribut bob doit être du type str ou None"),
        (1, None, None, None, None, 1, "l'attribut lieu_naissance doit être du type str ou None"),
    ],
)
def test_Personne_init_erreur(
    id, first_name, last_name, sexe, dob, lieu_naissance, message_erreur
        ) -> None:
    with pytest.raises(ValueError, match=re.escape(message_erreur)):
        Personne(
            id=id, first_name=first_name, last_name=last_name, sexe=sexe,
            dob=dob, lieu_naissance=lieu_naissance
            )


def test_Personne_eq() -> None:
    P1 = Personne(first_name="Edouard", last_name="Elric")
    P2 = Personne(full_name="Edouard Elric")
    P3 = Personne(full_name="Edouard  Elric")
    P4 = Personne(id = 5)
    P5 = Personne(id = 4)
    assert Personne(P1).__eq__(P1) == True
    assert Personne(P2).__eq__(P1) == True
    assert Personne(P3).__eq__(P2) == False
    assert Personne(P4).__eq__(P5) == True

def test_Personne_str() -> None:
    P1 = Personne(first_name="Marc", last_name="Evans", sexe = "M")
    assert str(P1) == "╭────────────┬──────────────┬──────────────╮\n" +
    "│ first_name │   last_name  │ sexe         │\n"+
    "├────────────┼──────────────┼──────────────┤\n"+
    "│       Marc │     Evans    │ M            │\n"+
    "╰────────────┴──────────────┴──────────────╯"



