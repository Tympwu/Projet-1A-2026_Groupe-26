from src.Interface.Menu_Début import Menu_Début


Interface = Menu_Début()
Interface.main_menu()

"""
self.dao_match_name = {
    "basketball": {
        "equipes": "team", "joueurs": "player", "matchs": "game"
    },
    "football_european_leagues": {
        "pays": "country", "league": "competition", "matchs": "match",
        "joueurs": "player", "equipes": "equipe"
    },
    "league_of_legends": {
        "equipes": "team", "joueurs": "player", "matchs": "match", "coach": "coach"
    },
    "tennis": {
        "matchs": ["atp_matches_2024", "wta_matches_2024"],
        "joueurs": ["atp_players_2024", "wta_players_2024"]
    },
    "volleyball": {
        "pays": "country",
        "coachs": ["coach_men", "coach_women"],
        "matchs": ["match_men", "match_women"],
        "joueurs": ["player_men", "player_women"]
    }
}
"""
