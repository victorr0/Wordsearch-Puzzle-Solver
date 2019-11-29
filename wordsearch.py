import json
import numpy as np


class WordSolver:

    def __init__(self, file, directions=None):
        if directions is None:
            self.directions = ["lr", "rl", "tb", "bt", "md_t", "md_b", "ad_t", "ad_b"]
        self.file = file
        self.word_grid = np.array(self.read_puzzle(self.file))
        self.solutions = self.dictionary_entries()
        self.rows = len(self.word_grid)
        self.cols = len(self.word_grid[0])

    def solve(self):
        lines = []

        if "lr" in self.directions:
            lines.extend(self.left_right())
        if "rl" in self.directions:
            lines.extend(self.right_left())
        if "tb" in self.directions:
            lines.extend(self.top_bottom())
        if "bt" in self.directions:
            lines.extend(self.bottom_top())
        if "md_t" in self.directions:
            lines.extend(self.main_diagonal_top())
        if "md_b" in self.directions:
            lines.extend(self.main_diagonal_bottom())
        if "ad_t" in self.directions:
            lines.extend(self.anti_diagonal_top())
        if "ad_b" in self.directions:
            lines.extend(self.anti_diagonal_bottom())

        lines = list(map("".join, lines))
        result = []

        for line in lines:
            for word in self.solutions:
                if word in line:
                    result.append(word)

        set_longer_than_one = set(list(filter(lambda x: len(x) > 1, result)))
        return sorted(sorted(set_longer_than_one), key=lambda x: len(x))

    def left_right(self):
        return list(self.word_grid)

    def right_left(self):
        return [list(reversed(line)) for line in self.word_grid]

    def top_bottom(self):
        return [list(self.word_grid[:, i]) for i in range(self.cols)]

    def bottom_top(self):
        return [list(reversed(self.word_grid[:, i])) for i in range(self.cols)]

    def main_diagonal_bottom(self):
        return [list(self.word_grid.diagonal(i)) for i in range(-self.rows, self.cols)]

    def main_diagonal_top(self):
        return [list(reversed(self.word_grid.diagonal(i))) for i in range(-self.rows, self.cols)]

    def anti_diagonal_bottom(self):
        new_grid = np.flip(np.array([[s for s in x] for x in self.word_grid]), axis=0)
        return [list(new_grid.diagonal(i)) for i in range(-self.cols, self.rows)]

    def anti_diagonal_top(self):
        new_grid = np.flip(np.array([[s for s in x] for x in self.word_grid]), axis=0)
        return [list(reversed(new_grid.diagonal(i))) for i in range(-self.cols, self.rows)]

    @staticmethod
    def read_puzzle(file):
        word_grid = open(file, 'r').read().split('\n')
        word_grid = [[letter for letter in line] for line in word_grid]
        return list(filter(lambda x: len(x) > 0, word_grid))

    @staticmethod
    def dictionary_entries():
        with open('dictionary.json', 'r', encoding='utf-8') as f:
            data = json.load(f)['words']

        return set([item.upper() for item in data])
