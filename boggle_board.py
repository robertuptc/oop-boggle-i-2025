import string
import random
alphabet = string.ascii_uppercase


class BoggleBoard():
    def __init__(self):
        self.random_letters = []
        self.home_screen = ''
        self.fill_board()

    def shake(self):
        # self.fill_board()
        self.get_letters()
        self.display_board()

    def fill_board(self):
        line = ''

        for i in range(4):
            for j in range(4):
                if len(line) < 4:
                    line += "_"
            print(line)
        return self.get_letters()

    def get_letters(self):
        self.random_letters = [[random.choice(alphabet) for __ in range(4)] for _ in range(4)]
        return self.random_letters

    def display_board(self):
        for _ in self.random_letters:
            print(''.join(_))
        print("\n")


new_game = BoggleBoard()
new_game.shake()
new_game.shake()
