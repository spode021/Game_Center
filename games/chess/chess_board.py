
class Chess_Board:

    board_width = 10

    board_height = 10

    # 2D matrix for storing chess piece location on board
    board_matrix = [[0 for x in range(board_width)] for y in range(board_height)]

    # print out the board with piece locations
    def print_board():
        pass


    # Add a chess piece to the board_matrix
    def add_piece(x_pos, y_pos, piece):
        pass
        board_matrix[x_pos][y_pos] = piece
