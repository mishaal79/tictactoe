from tictactoe import TicTacToe
from player import Player
from constant import CROSS_SYMBOL, NAUGHT_SYMBOL
import pydash


def main():
    print("Welcome to TicTacToe")
    game = TicTacToe()
    player1 = Player(input("Enter player1 name: "), CROSS_SYMBOL)
    player2 = Player(input("Enter player2 name: ",),NAUGHT_SYMBOL)
    running = True
    while running:
        game.print_grid()
        if(game.state == TicTacToe.STATES.CROSS_TURN):
            print("Player1 turn")
            marker = input("Input row, column to place marker in: ").split(',')
            marker = pydash.map_(marker, int)
            game.place_marker(CROSS_SYMBOL, marker[0], marker[1])
        
        if(game.state == TicTacToe.STATES.NAUGHT_TURN):
            print("Player2 turn")
            marker = input("Input row, column to place marker in: ").split(',')
            marker = pydash.map_(marker, int)
            game.place_marker(NAUGHT_SYMBOL, marker[0], marker[1])

        game.process_state()
        if(game.state == TicTacToe.STATES.DRAW):
            running = False
            print('The game is drawn')
        
        if(game.state == TicTacToe.STATES.CROSS_WON):
            running = False
            print('{} wins the game'.format(player1.name))
        
        if(game.state == TicTacToe.STATES.NAUGHT_WON):
            running = False
            print('{} wins the game'.format(player2.name))
                        


if __name__ == "__main__":
    main()