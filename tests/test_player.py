import pytest
from constant import CROSS_SYMBOL
from player import Player


@pytest.fixture()
def player():
    return Player("tom", CROSS_SYMBOL)


def test_set_marker(player):
    player.set_marker([0, 1])
    assert player.marker_row == 0 and player.marker_column == 1


def test_is_winner_for_row_returns_true(player):
    player.row[0] = 3
    player.marker_row = 0
    player.marker_column = 1
    assert player.is_winner() == True


def test_is_winner_for_column_returns_true(player):
    player.column[0] = 3
    player.marker_row = 1
    player.marker_column = 0
    assert player.is_winner() == True


def test_is_winner_for_left_diag_returns_true(player):
    player.left_diag = 3
    player.marker_row = 2
    player.marker_column = 2
    assert player.is_winner() == True


def test_is_winner_for_right_diag_returns_true(player):
    player.right_diag = 3
    player.marker_row = 0
    player.marker_column = 2
    assert player.is_winner() == True


def test_is_winner_returns_false(player):
    player.row[0] = 2
    player.marker_row = 0
    player.marker_column = 1
    assert player.is_winner() == False


def test_process_move(player):
    player.marker_row = 0
    player.marker_column = 0
    player.process_move()
    assert player.row[0] == 1
