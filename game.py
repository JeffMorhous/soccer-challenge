class Game:
    def __init__(self, match_line):
        team1_with_score, team2_with_score = match_line.split(', ')
        self.team1_name, self.score1 = team1_with_score.rsplit(' ', 1)
        self.team2_name, self.score2 = team2_with_score.rsplit(' ', 1)
        self.score1 = int(self.score1)
        self.score2 = int(self.score2)
