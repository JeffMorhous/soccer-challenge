class Team:
    def __init__(self, name):
        self.name = name
        self.points = 0

    def add_points(self, points):
        self.points += points

    def __lt__(self, other):
        if self.points == other.points:
            return self.name > other.name
        return self.points < other.points

    def __str__(self):
        return f"{self.name}, {self.points} pts" if self.points > 1 or self.points == 0 else f"{self.name}, {self.points} pt"