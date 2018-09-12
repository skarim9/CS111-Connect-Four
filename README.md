# Connect-Four

A Connect Four game that allows for single player, multiplayer, and simulation use. There are four different classes used in this game: the
Board class, the Player class, the RandomPlayer class, and the AIPlayer class. The Board class represents the board for the game.
The Player class represents a player in the Connect Four game. The RandomPlayer class is a subclass of the Player class represents an 
unintelligent computer player that chooses at random from the available columns. The AIPlayer is a subclass of the Player class and
represents an AI Player that looks ahead some number of moves and makes a move based on the possible moves. In single player,
the player has two choices of opponents: RandomPlayer and AIPlayer. In multiplayer, there can only be one more other player. In simulation,
you can pit two RandomPlayers against each other, one RandomPlayer against an AIPlayer, or even two skilled AIPlayers against each other.
