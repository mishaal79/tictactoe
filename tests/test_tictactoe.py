import pytest
from tictactoe import TicTacToe
from constant import GRID_SIZE,  CROSS_SYMBOL, NAUGHT_SYMBOL
from player import Player


@pytest.fixture()
def game():
    return TicTacToe(GRID_SIZE, Player('tom', CROSS_SYMBOL), Player('mark', NAUGHT_SYMBOL))


def test_place_marker_valid(game):
    game.place_marker(CROSS_SYMBOL, 1, 1)
    assert game.grid[1][1] == CROSS_SYMBOL
    assert(game.move_count == 1)



def test_place_marker_invalid(game):
    game.place_marker(CROSS_SYMBOL, 1, 1)
    assert game.place_marker(NAUGHT_SYMBOL, 1, 1) == False


def test_reset_grid(game):
    game.grid[1][0] = CROSS_SYMBOL
    game.reset_grid()
    assert game.grid[1][0] == ""


def test_get_cell_value(game):
    game.grid[0][1] = NAUGHT_SYMBOL
    assert game.get_cell_value(0, 1) == NAUGHT_SYMBOL