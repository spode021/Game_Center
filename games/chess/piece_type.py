#########################################################
# This file contains the piece types
#########################################################

from enum import Enum

class Piece_Type(Enum):
    NOTYPE = 0
    PAWN   = 1
    KNIGHT = 2
    ROOK   = 3
    BISHOP = 4
    QUEEN  = 5
    KING   = 6
