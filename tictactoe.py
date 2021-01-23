from enum import Enum
import pprint
from constant import CROSS_SYMBOL, NAUGHT_SYMBOL


class TicTacToe:
    class STATES(Enum):
        CROSS_TURN = 0
        NAUGHT_TURN = 1
        DRAW = 2
        CROSS_WON = 3
        NAUGHT_WON = 4

    def __init__(self):
        self.grid = [[""] * 3 for i in range(3)]
        self.state = TicTacToe.STATES.CROSS_TURN

    def place_marker(self, symbol, row, column):
        if self.get_cell_value(row, column) == "":
            self.grid[row][column] = symbol
        else:
            return "grid is already marked with {}".format(
                self.get_cell_value(row, column)
            )

    def get_cell_value(self, row, column):
        return self.grid[row][column]

    def print_grid(self):
        pp = pprint.PrettyPrinter(indent=2, width=2, depth=1)
        pp.pprint(self.grid)

    def reset_grid(self):
        self.grid = [[""] * 3 for i in range(3)]

    def check_horizontal_streak(self, symbol):
        for row in range(2):
            if (
                self.get_cell_value(row, 0) == symbol
                and self.get_cell_value(row, 1) == symbol
                and self.get_cell_value(row, 2) == symbol
            ):
                return True
        return False

    def check_vertical_streak(self, symbol):
        for column in range(2):
            if (
                self.get_cell_value(0, column) == symbol
                and self.get_cell_value(1, column) == symbol
                and self.get_cell_value(2, column) == symbol
            ):
                return True
        return False

    def check_diaganol_streak(self, symbol):
        if (
            self.get_cell_value(0, 0) == symbol
            and self.get_cell_value(1, 1) == symbol
            and self.get_cell_value(2, 2) == symbol
        ):
            return True
        elif (
            self.get_cell_value(0, 2) == symbol
            and self.get_cell_value(1, 1) == symbol
            and self.get_cell_value(2, 0) == symbol
        ):
            return True
        else:
            return False

    def check_grid_complete(self):
        for i in range(2):
            for j in range(2):
                if self.get_cell_value(i, j) == "":
                    return False
        return True

    def process_state(self):
        if (
            self.check_vertical_streak(CROSS_SYMBOL)
            or self.check_horizontal_streak(CROSS_SYMBOL)
            or self.check_diaganol_streak(CROSS_SYMBOL)
        ):
            self.state = TicTacToe.STATES.CROSS_WON
        if (
            self.check_vertical_streak(NAUGHT_SYMBOL)
            or self.check_horizontal_streak(NAUGHT_SYMBOL)
            or self.check_diaganol_streak(NAUGHT_SYMBOL)
        ):
            self.state = TicTacToe.STATES.NAUGHT_WON
        if self.check_grid_complete():
            self.state = TicTacToe.STATES.DRAW
        if self.state == TicTacToe.STATES.CROSS_TURN:
            self.state = TicTacToe.STATES.NAUGHT_TURN
        else:
            self.state = TicTacToe.STATES.CROSS_TURN
