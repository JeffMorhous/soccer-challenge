import sys
from league import League

def print_rankings(rankings):
    rank = 1
    last_points = None
    for i, team in enumerate(rankings):
        if last_points is not None and team.points < last_points:
            rank = i + 1
        print(f"{rank}. {team}")
        last_points = team.points

def main():
    league = League()
    for line in sys.stdin:
        league.process_match(line.strip())

    print_rankings(league.get_rankings())

# Is this being run as a script rather than a module?
if __name__ == "__main__":
    main()
