#
# ps9pr2.py  (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below

class Player:
    """ a class that represents a player in the Connect Four
        game
    """
    # Number 1
    def __init__(self, checker):
        """ a constructor that constructs a new Player object
            by initializing two attributes, checker and
            num_moves
        """
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0

    # Number 2
    def __repr__(self):
        """ Returns a string representation of the Player
            object
        """
        s = 'Player '
        return s + self.checker

    # Number 3
    def opponent_checker(self):
        """ Returns a one-character string representing the
            checker of the Player object's opponent
        """
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'

    # Number 4
    def next_move(self, board):
        """ Accepts a Board object as a parameter and
            returns the column where the player wants to make
            the next move
        """
        self.num_moves += 1
        
        while True:
            col = int(input('Enter a column: '))
            if col > (board.width - 1) or col < 0:
                print('Try again!')
            elif board.can_add_to(col) == False:
                print('Try again!')
            else:
                return col
        
