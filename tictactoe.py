from enum import Enum


class TicTacToe:
    class STATES(Enum):
        CROSS_TURN = 0
        NAUGHT_TURN = 1
        DRAW = 2
        CROSS_WON = 3
        NAUGHT_WON = 4

    def __init__(self):
        pass

    def place_marker(self, symbol, row, column):
        pass

    # ...
    # Other methods as necessary.
    # ...