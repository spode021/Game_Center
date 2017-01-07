
#
# This file contains details about the chess pieces to be played with.
#
class Chess_Piece:
    #type of chess piece
    piece_type

    # X coordinate on board
    x_position

    # Y coordinate on board
    y_position

    # Populates the chess piece with information. Used at the start of
    # the game to initialize all of the pieces
    def Populate_Piece(x_pos, y_pos, p_type):
        x_position = x_pos
        y_position = y_pos
        piece_type = p_type
