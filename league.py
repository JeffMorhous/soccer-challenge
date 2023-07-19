from collections import defaultdict
from game import Game
from team import Team

class League:
    def __init__(self):
        self.teams = defaultdict(lambda: Team(''))

    def process_match(self, match_line):
        game = Game(match_line)
        self.teams[game.team1_name].name = game.team1_name
        self.teams[game.team2_name].name = game.team2_name
        if game.score1 > game.score2:
            self.teams[game.team1_name].add_points(3)
        elif game.score1 < game.score2:
            self.teams[game.team2_name].add_points(3)
        else:
            self.teams[game.team1_name].add_points(1)
            self.teams[game.team2_name].add_points(1)

    # Uses Team's overwritten __lt__ operator
    def get_rankings(self):
        return sorted(self.teams.values(), reverse=True)
