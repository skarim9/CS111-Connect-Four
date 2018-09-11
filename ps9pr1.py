# Shihab Karim
# Problem Set 9 Problem 1
# A Connect Four Board Class

class Board:
    """ a class that represents the board for the game of
        Connect Four
    """

    # Number 1
    def __init__(self, height, width):
        """ a constructor that initializes three atributes,
            height (number of rows), width (number of
            columns), and slots
        """
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]

    # Number 2
    def __repr__(self):
        """ Returns a string representation for a Board object.
        """
        s = ''         # begin with an empty string

        # add one row of slots at a time
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        # Add code here for the hyphens at the bottom of the board
        # and the numbers underneath it.
        
        s += (((2 * self.width) + 1) * '-')

        s += '\n '
        columns = self.width
        
        if columns <= 10:
            for c in range(columns):
                s += str(c) + ' '
        else:
            while columns > 10:
                for c in range(10):
                    s += str(c) + ' '
                columns -= 10
            for c in range(columns):
                s += str(c) + ' '
            
        return s

    # Number 3
    def add_checker(self, checker, col):
        """ Accepts two inputs, checker and col. Checker is
            a one-character string to add to the board. Col
            is the index of the column of where the checker
            is to be added
        """
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)
        row = 0
        if self.slots[0][col] == ' ':   # if column is full, function stops and checker does not replace anything

            while self.slots[row][col] == ' ':
                if row == (self.height - 1):
                    break
                else:
                    row += 1
            if self.slots[row][col] != ' ':
                row -= 1
                
            self.slots[row][col] = checker

    # Number 4
    def reset(self):
        """ Resets the Board object and clears the board
        """
        for c in range(self.height):
            for x in range(self.width):
                self.slots[c][x] = ' '

    # Number 5
    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
        checkers in those columns of the called Board object, 
        starting with 'X'.
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    # Number 6
    def can_add_to(self, col):
        """ Returns True if column col is not full or is
            legal. Otherwise, returns False
        """
        if col > (self.width - 1) or col < 0:
            return False
        elif self.slots[0][col] != ' ':
            return False
        else:
            return True

    # Number 7
    def is_full(self):
        """ Returns True if the called Board object is
            completely full of checkers and returns False
            otherwise
        """
        for c in range(self.width):
            if self.can_add_to(c) == True:
                return False
        return True

    # Number 8
    def remove_checker(self, col):
        """ Removes the top checker from the col of the
            called Board object. If column is empty, then
            method should do nothing
        """
        if self.slots[-1][col] != ' ':
            row = 0
            while self.slots[row][col] == ' ':
                if row == (self.height - 1):
                    break
                else:
                    row += 1
            self.slots[row][col] = ' '

    # Number 9
    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True

        # if we make it here, there were no horizontal wins
        return False

    def is_vertical_win(self, checker):
        """ Checks for a vertical win for the specified
            checker
        """
        for row in range(self.height - 3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                    return True
        return False

    def is_down_diagonal_win(self, checker):
        """ Checks for a downward diagonal win for the
            specified checker
        """
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col + 1] == checker and \
                   self.slots[row + 2][col + 2] == checker and \
                   self.slots[row + 3][col + 3] == checker:
                    return True
        return False

    def is_up_diagonal_win(self, checker):
        """ Checks for a upward diagonal win for the
            specified checker
        """
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row + 3][col] == checker and \
                   self.slots[row + 2][col + 1] == checker and \
                   self.slots[row + 1][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True
        return False

    def is_win_for(self, checker):
        """ Accepts a parameter checekr that is either 'X'
            or 'O' and returns True if there are four
            consecutive slots containing checker on the
            board. Otherwise, it should return False
        """
        assert(checker == 'X' or checker == 'O')
        if self.is_horizontal_win(checker) == True or \
           self.is_vertical_win(checker) == True or \
           self.is_down_diagonal_win(checker) == True or \
           self.is_up_diagonal_win(checker) == True:
            return True
        else:
            return False
