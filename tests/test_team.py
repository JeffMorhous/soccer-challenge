import pytest

# We need this for relative imports unless I want to make the classes a package
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from team import Team

def test_team_initialization():
    team = Team("Jeffs Team")
    assert team.name == "Jeffs Team"
    assert team.points == 0

def test_team_add_points():
    team = Team("Jeffs Team")
    team.add_points(3)
    assert team.points == 3
    team.add_points(2)
    assert team.points == 5

def test_team_string_representation():
    team = Team("Jeffs Team")
    assert str(team) == "Jeffs Team, 0 pts"
    team.add_points(1)
    assert str(team) == "Jeffs Team, 1 pt"
    team.add_points(1)
    assert str(team) == "Jeffs Team, 2 pts"

def test_team_comparisons():
    team1 = Team("A Team")
    team2 = Team("B Team")
    team1.add_points(3)
    team2.add_points(3)
    assert not team1 < team2  # team1 should not be considered "less than" team2 because names are in alphabetical order
    assert team2 < team1
    team2.add_points(1)
    assert team1 < team2  # Now team2 has more points, so team1 should be "less than" team2
