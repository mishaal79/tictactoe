from tictactoe import TicTacToe
from player import Player
from constant import *
import pydash


def main():
    print("Welcome to TicTacToe")
    player1 = Player(input("Enter name for player1: "), CROSS_SYMBOL)
    player2 = Player(input("Enter name for player2: "), NAUGHT_SYMBOL)
    game = TicTacToe(GRID_SIZE, player1, player2)
    running = True
    while running:
        game.print_grid()
        if game.state == TicTacToe.STATES.CROSS_TURN:
            print("Player1 turn")
            while True:
                marker = pydash.map_(input("Input row, column to place marker in: ").split(","), int)
                if game.place_marker(
                    CROSS_SYMBOL, marker[0], marker[1]
                ):
                    game.player1.set_marker(marker)
                    game.player1.process_move()
                    game.state = TicTacToe.STATES.NAUGHT_TURN
                    if game.player1.is_winner():
                        game.state = TicTacToe.STATES.CROSS_WON
                    break
                else:
                    print("Please input marker into empty cell")


        if game.state == TicTacToe.STATES.NAUGHT_TURN:
            print("Player2 turn")
            while True:
                marker = pydash.map_(input("Input row, column to place marker in: ").split(","), int)
                if game.place_marker(
                    NAUGHT_SYMBOL, marker[0], marker[1]
                ):
                    game.player2.set_marker(marker)
                    game.player2.process_move()
                    game.state = TicTacToe.STATES.CROSS_TURN
                    if game.player2.is_winner():
                        game.state = TicTacToe.STATES.NAUGHT_WON
                    break
                else:
                    print("Please input marker into empty cell")

        if game.state == TicTacToe.STATES.CROSS_WON:
            running = False
            print("{} wins the game".format(game.player1.name))

        if game.state == TicTacToe.STATES.NAUGHT_WON:
            running = False
            print("{} wins the game".format(game.player2.name))

        if (
            game.state == TicTacToe.STATES.CROSS_TURN
            and game.move_count == GRID_SIZE ^ 2
        ):
            running = False
            print("The game is drawn")


if __name__ == "__main__":
    main()