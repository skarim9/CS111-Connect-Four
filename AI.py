#
# ps9pr4.py  (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four   
#

import random  
from ps9pr3 import *

# Number 1
class AIPlayer(Player):
    """ a subclass of the Player class and represents an AI
        Player that looks ahead some number of moves and
        makes a move based on the possible moves
    """

    # Number 2
    def __init__(self, checker, tiebreak, lookahead):
        """ a constructor that constructs a new AIPlayer object
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)

        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead

    # Number 3
    def __repr__(self):
        """ a string representation of the AIPlayer object
            which overrides the __repr__ method inherited
            from Player
        """
        s = 'Player ' + self.checker + ' (' + \
            str(self.tiebreak) + ', ' + str(self.lookahead) \
            + ')'
        return s

    # Number 4
    def max_score_column(self, scores):
        """ Takes a list containing a score for each column
            of the board, and returns the index of the column
            with the maximum score
        """
        max_score = max(scores)
        max_list = []
        for i in range(len(scores)):
            if scores[i] == max_score:
                max_list += [i]
        if self.tiebreak == 'LEFT':
            return max_list[0]
        elif self.tiebreak == 'RIGHT':
            return max_list[-1]
        else:
            return random.choice(max_list)

    # Number 5
    def scores_for(self, board):
        """ Takes a Board object board and determines the
            called AIPlayer's scores for the columns in the
            board.
        """
        scores = [50] * board.width
        for col in range(board.width):
            if board.can_add_to(col) == False:
                scores[col] = -1
            elif board.is_win_for(self.checker) == True:
                scores[col] = 100
            elif board.is_win_for(self.opponent_checker()) \
                 == True:
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                board.add_checker(self.checker, col)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                opp_scores = opponent.scores_for(board)
                max_opp = max(opp_scores)
                if max_opp == 0:
                    scores[col] = 100
                elif max_opp == 100:
                    scores[col] = 0
                else:
                    scores[col] = 50
                board.remove_checker(col)
        return scores

    # Number 6
    def next_move(self, board):
        """ Overrides the next_move method inherited from
            Player. This version of next_move should return
            the called AIPlayer's judgement of its best
            possible move
        """
        poss_moves = self.scores_for(board)
        best_move = self.max_score_column(poss_moves)
        self.num_moves += 1
        return best_move
