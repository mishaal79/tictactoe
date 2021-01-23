import pytest
from tictactoe import TicTacToe
from constant import CROSS_SYMBOL, NAUGHT_SYMBOL


@pytest.fixture()
def game():
    return TicTacToe()


def test_place_marker(game):
    game.place_marker(CROSS_SYMBOL, 1, 1)
    assert game.grid[1][1] == CROSS_SYMBOL


def test_reset_grid(game):
    game.grid[1][0] = CROSS_SYMBOL
    game.reset_grid()
    assert game.grid[1][0] == ""


def test_print_grid(game):
    game.print_grid()


def test_get_cell_value(game):
    game.grid[0][1] = NAUGHT_SYMBOL
    assert game.get_cell_value(0, 1) == NAUGHT_SYMBOL


def test_check_vertical_streak(game):
    game.grid[0][0] = CROSS_SYMBOL
    game.grid[1][0] = CROSS_SYMBOL
    game.grid[2][0] = CROSS_SYMBOL
    assert game.check_vertical_streak(CROSS_SYMBOL) == True


def test_check_horizontal_streak(game):
    game.grid[0][0] = NAUGHT_SYMBOL
    game.grid[0][1] = NAUGHT_SYMBOL
    game.grid[0][2] = NAUGHT_SYMBOL
    assert game.check_horizontal_streak(NAUGHT_SYMBOL) == True


def test_check_left_diaganol_streak(game):
    game.grid[0][0] = CROSS_SYMBOL
    game.grid[1][1] = CROSS_SYMBOL
    game.grid[2][2] = CROSS_SYMBOL
    assert game.check_diaganol_streak(CROSS_SYMBOL) == True


def test_check_right_diaganol_streak(game):
    game.grid[0][2] = CROSS_SYMBOL
    game.grid[1][1] = CROSS_SYMBOL
    game.grid[2][0] = CROSS_SYMBOL
    assert game.check_diaganol_streak(CROSS_SYMBOL) == True


def test_check_complete_grid(game):
    pass