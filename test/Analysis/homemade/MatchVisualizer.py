from src.Model.Match import Match
from src.Model.Sport import Sport


class MatchVisualizer():
    def display_match_title(match: Match, sport: Sport):
        if sport.is_individual:
            return '{match.player_1} VS {match.player_2}'

        return 'Équipe {match.player_1} VS Équipe {match.player_2}'
