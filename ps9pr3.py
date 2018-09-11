#
# ps9pr3.py  (Problem Set 9, Problem 3)
#
# Playing the game 
#   

from ps9pr1 import Board
from ps9pr2 import Player
import random
    
def connect_four(player1, player2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: player1 and player2 are objects representing Connect Four
                  players (objects of the Player class or a subclass of Player).
                  One player should use 'X' checkers and the other should
                  use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if player1.checker not in 'XO' or player2.checker not in 'XO' \
       or player1.checker == player2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    board = Board(6, 7)
    print(board)
    
    while True:
        if process_move(player1, board) == True:
            return board

        if process_move(player2, board) == True:
            return board

# Number 1
def process_move(player, board):
    """ Takes two parameters, a Player object whose move is
        being processed and a Board object for the game that
        is being played
    """
    print(player.__repr__() + "'s turn")
    new_col = player.next_move(board)
    board.add_checker(player.checker, new_col)
    print('\n')
    print(board)
    print('\n')
    if board.is_win_for(player.checker) == True:
        print(player.__repr__() + ' wins in ' + \
              str(player.num_moves) + ' moves.' \
              + '\n' + 'Congratulations!')
        return True
    elif board.is_win_for(player.checker) == False and \
         board.is_full() == True:
        print("It's a tie!")
        return True
    else:
        return False

# Number 2
class RandomPlayer(Player):
    """ a subclass of the Player class and represents an
        unintelligent computer player that chooses at random
        from the available columns
    """
    def next_move(self, board):
        """ Overrides the next_move function that is
            inherited from Player. This function chooses at
            random from the columns in the specified board
            that are not yet full and returns the index
            of that randomly selected column
        """
        free_col = []
        for x in range(board.width):
            if board.can_add_to(x) == True:
                free_col += [x]
        self.num_moves += 1
        return random.choice(free_col)
