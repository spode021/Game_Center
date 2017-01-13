#########################################################
# This file contains the piece types
#########################################################

from enum import Enum


class Piece_Type(Enum):
    NOTYPE = 'NOTYPE'
    PAWN = 'PAWN'
    KNIGHT = 'KNIGHT'
    ROOK = 'ROOK'
    BISHOP = 'BISHOP'
    QUEEN = 'QUEEN'
    KING = 'KING'
