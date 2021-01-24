import pydash
from constant import GRID_SIZE



class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.row =  [0] * GRID_SIZE
        self.column = [0] * GRID_SIZE
        self.left_diag = [0] * GRID_SIZE
        self.right_diag = [0] * GRID_SIZE

    def set_marker(self, marker):
        marker = pydash.map_(marker, int)
        self.marker_row, self.marker_column = marker[0], marker[1]

    def process_move(self):
        self.row[self.marker_row] += 1
        self.column[self.marker_column] += 1
        if self.marker_row == self.marker_column:
            self.left_diag[self.marker_row] += 1
        if self.marker_row + self.marker_column == GRID_SIZE:
            self.right_diag[self.marker_row] += 1

    def is_winner(self):
        if (
            self.row[self.marker_row] == GRID_SIZE
            or self.column[self.marker_column] == GRID_SIZE
            or self.left_diag[self.marker_row] == GRID_SIZE
            or self.right_diag[self.marker_row] == GRID_SIZE
        ):
            return True
        else:
            return False
