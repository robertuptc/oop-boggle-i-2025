import string
import random
alphabet = string.ascii_uppercase


class BoggleBoard():
    def __init__(self):
        self.boggle_list = [
                                "AAEEGN", 
                                "ELRTTY", 
                                "AOOTTW", 
                                "ABBJOO", 
                                "EHRTVW", 
                                "CIMOTU", 
                                "DISTTY", 
                                "EIOSST", 
                                "DELRVY", 
                                "ACHOPS", 
                                "HIMNQU", 
                                "EEINSU", 
                                "EEGHNW", 
                                "AFFKPS", 
                                "HLNNRZ", 
                                "DEILRX"
                            ]
        self.random_letters = []
        self.fill_board()

    def shake(self):
        self.get_letters()
        self.display_board()

    def fill_board(self):
        line = ''

        for i in range(4):
            for j in range(4):
                if len(line) < 4:
                    line += "_"
            print(line)


    def get_letters(self):
        random_list = random.sample(self.boggle_list, 4) 

        for l in random_list: 
            self.random_letters.append(random.sample(l, 4))

    def display_board(self):
        for _ in self.random_letters:
            if "Q" in _:
                idx = _.index('Q')
                _[idx] = "Qu"
            print('  '.join(_))
        print("\n")
        self.random_letters = []


new_game = BoggleBoard()
new_game.shake()
new_game.shake()
