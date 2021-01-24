from enum import Enum
from constant import CROSS_SYMBOL, NAUGHT_SYMBOL
from prettytable import PrettyTable, ALL
from player import Player


class TicTacToe:
    class STATES(Enum):
        CROSS_TURN = 0
        NAUGHT_TURN = 1
        DRAW = 2
        CROSS_WON = 3
        NAUGHT_WON = 4

    def __init__(self, grid_size, player1, player2):
        self.grid = [[""] * grid_size for i in range(grid_size)]
        self.state = TicTacToe.STATES.CROSS_TURN
        self.player1 = player1
        self.player2 = player2
        self.move_count = 0

    def place_marker(self, symbol, row, column):
        if self.get_cell_value(row, column) == "":
            self.grid[row][column] = symbol
            self.move_count += 1
            self.print_grid()
            return True
        else:
            return False


    def get_cell_value(self, row, column):
        return self.grid[row][column]

    def print_grid(self):
        table = PrettyTable()
        for row in self.grid:
            table.add_row(row)
        print(table.get_string(header=False, hrules=ALL))

    def reset_grid(self):
        self.grid = [[""] * 3 for i in range(3)]