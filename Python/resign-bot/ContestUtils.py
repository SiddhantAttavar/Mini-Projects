"""
This file will be available to you via import. The starter code file imports
everything accessible already.
"""
from enum import Enum

# This enum represents the player colour
PlayerColour = Enum('PlayerColour', [
    'White', 
    'Black'
])

# This enum represents the pieces available
BoardPiece = Enum('BoardPiece', [
    'WhitePawn',
    'WhiteKnight',
    'WhiteBishop',
    'WhiteRook',
    'WhiteQueen',
    'WhiteKing',
    'BlackPawn',
    'BlackKnight',
    'BlackBishop',
    'BlackRook',
    'BlackQueen',
    'BlackKing',
    'EmptySquare',
    'Resignation',
    'Invalid'
])

files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
ranks = ['1', '2', '3', '4', '5', '6', '7', '8']

all_squares = [file+rank for file in files for rank in ranks]

# This class represents the board state
class BoardState:

    @staticmethod
    def resign():
        states = {}
        for file in files:
            for rank in ranks:
                states[file + rank] = BoardPiece.Resignation
        return BoardState(states)

    @staticmethod
    def invalid():
        states = {}
        for file in files:
            for rank in ranks:
                states[file + rank] = BoardPiece.Invalid
        return BoardState(states)

    # Create a new board state with a dictionary mapping positions (like
    # e4, a8, ...) to BoardPiece members. Empty squares can either be 
    # specified to be empty, or ommitted entirely. 
    def __init__(self, position_states):
        invalidate = False
        resign = False
        if type(position_states) is not dict:
            invalidate = True
        for (position, piece) in position_states.items():
            if type(piece) is not BoardPiece:
                invalidate = True
            if type(position) is not str:
                invalidate = True
            if position not in all_squares:
                invalidate = True
            if piece == BoardPiece.Invalid:
                invalidate = True
            if piece == BoardPiece.Resignation:
                resign = True

        if invalidate:
            for position in all_squares:
                position_states[position] = BoardPiece.Invalid
            self._state = position_states
            return
        if resign:
            for position in all_squares:
                position_states[position] = BoardPiece.Resignation
            self._state = position_states
            return

        for position in all_squares:
            if position not in position_states.keys():
                position_states[position] = BoardPiece.EmptySquare
        self._state = position_states

    # Get a piece at a file and rank
    # Note that files are lowercase alphabet a-h
    # Note that ranks are strings of 1-8
    def piece_at(self, file, rank):
        if file not in files or rank not in ranks:
            return BoardPiece.Invalid
        return self._state[file + rank]
