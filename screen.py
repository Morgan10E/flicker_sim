class Screen:
    def __init__(self, screen_width, screen_height, empty_string):
        self.width = screen_width
        self.height = screen_height
        self.empty_square = empty_string

        self.board = [[empty_string] * screen_width for i in range(screen_height)]

    def clear(self):
        self.board = [[self.empty_square] * self.width for i in range(self.height)]

    # (0,0) top left corner
    def set(self, x, y, set_to_string):
        self.board[y][x] = set_to_string
    
    def print(self):
        print("⬜" * (self.width + 2))
        for row in self.board:
            print("⬜" + "".join(row) + "⬜")
        print("⬜" * (self.width + 2))