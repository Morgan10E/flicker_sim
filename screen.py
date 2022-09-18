class Screen:
    def __init__(self, screen_width, screen_height, empty_string):
        self.width = screen_width
        self.height = screen_height
        self.empty_square = empty_string

        self.board = [[empty_string] * screen_width for i in range(screen_height)]

    def clear(self):
        self.board = [[self.empty_square] * self.width for i in range(self.height)]

    # (0,0) top left corner
    def set_point(self, x, y, set_to_string):
        self.board[y][x] = set_to_string

    def set_board(self, board):
        if len(board) != self.height or len(board[0]) != self.width:
            raise Exception(f"board must match screen dimensions width: {self.width} height: {self.height}")
        for i in range(self.height):
            for k in range(self.width):
                if board[i][k] != None:
                    self.board[i][k] = board[i][k]
    
    def print(self):
        print("⬜" * (self.width + 2))
        for row in self.board:
            print("⬜" + "".join(row) + "⬜")
        print("⬜" * (self.width + 2))