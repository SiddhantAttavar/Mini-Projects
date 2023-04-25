"""
Write your code in this file to participate in the Chess Bot challenge!

Username: SiddhantAttavar
"""
from ContestUtils import PlayerColour
from ContestUtils import BoardState

class Engine:

    """
    This function will be called at the start of each game. You should use this to
    set up any key data structures you will need for the game. You can also use
    this function to precompute any data you will use during the game.

    Parameters:
      - colour:             PlayerColour.White or PlayerColour.Black, representing the 
                            colour your bot will be playing for this game.
      - time_per_move:      Float representing the number of seconds you have per move
                            for each move during this game. 

    Return:
      - Nothing. You can choose to return something if you wish, but nothing will be 
        done with this information.

    Constraints:
      - This function must complete running in at most 10 seconds, or the game will
        automatically be considered forfeited.
    """
    def __init__(self, colour, time_per_move):
        pass

    """
    This function will be called every time your opponent makes a move (or, if you're
    playing white, also at the start). In other words, this function will be called
    whenever it's your turn to make a move. You can use this function to calculate 
    your next move and then send it.

    Parameters:
      - board_state:        BoardState object representing the current state of the
                            board. 

    Return:
      - A new board state after your move is made, represented using the BoardState 
        object. 

    Constraints:
      - If the new board state you return is not a valid board state resulting from
        a valid move you can make, then you will immediately lose the game.
      - If this function takes more than time_per_move seconds to run, you will
        immediately lose the game.
      - You can return BoardState.resign() if you'd like to resign.
    """
    def get_move(self, board_state):
        return BoardState.resign()
