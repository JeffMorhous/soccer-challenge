import pytest

# We need this for relative imports unless I want to make the classes a package
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from league import League

def test_league_initialization():
    league = League()
    assert league.teams == {}

def test_process_match():
    league = League()
    league.process_match("Lions 3, Snakes 1")
    assert league.teams["Lions"].points == 3
    assert league.teams["Snakes"].points == 0
    league.process_match("Tarantulas 1, Lions 1")
    assert league.teams["Tarantulas"].points == 1
    assert league.teams["Lions"].points == 4

def test_get_rankings():
    league = League()
    league.process_match("Lions 3, Snakes 1")
    league.process_match("Tarantulas 1, Lions 1")
    league.process_match("FC Awesome 0, Tarantulas 1")
    rankings = league.get_rankings()
    assert rankings[0].name == "Lions"
    assert rankings[0].points == 4
    assert rankings[1].name == "Tarantulas"
    assert rankings[1].points == 4
    assert rankings[2].name == "FC Awesome"
    assert rankings[2].points == 0
    assert rankings[3].name == "Snakes"
    assert rankings[3].points == 0
