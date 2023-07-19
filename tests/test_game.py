import pytest

# We need this for relative imports unless I want to make the classes a package
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game import Game

def test_game_initialization():
    game = Game("Lions 3, Snakes 1")
    assert game.team1_name == "Lions"
    assert game.team2_name == "Snakes"
    assert game.score1 == 3
    assert game.score2 == 1

def test_game_with_multi_word_team_name():
    game = Game("FC Awesome 1, Tarantulas 3")
    assert game.team1_name == "FC Awesome"
    assert game.team2_name == "Tarantulas"
    assert game.score1 == 1
    assert game.score2 == 3

def test_game_with_invalid_format():
    with pytest.raises(ValueError):
        game = Game("InvalidFormat")
