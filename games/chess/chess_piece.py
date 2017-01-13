
#
# This file contains details about the chess pieces to be played with.
#

from piece_type.py import Piece_Type

# Class definition of Chess_Piece


class Chess_Piece:

    # type of chess piece
    piece_type

    alive

    # X coordinate on board
    x_position

    # Y coordinate on board
    y_position

    # Initiate pieces with default values tha

    def __init__(self, x_pos=-1, y_pos=-1, p_type=Piece_Type.NOTYPE, al = False):
        x_position = x_pos
        y_position = y_pos
        piece_type = p_type
        alive = al

    # Populates the chess piece with information. Used at the start of
    # the game to initialize all of the pieces
    def Populate_Piece(x_pos, y_pos, p_type):
        x_position = x_pos
        y_position = y_pos
        piece_type = p_type
        alive = True
