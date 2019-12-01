import numpy as np

from solver.wordsearch import WordSolver

board_long = np.array([["A", "B"], ["C", "D"], ["E", "F"], ["G", "H"]])
long = WordSolver("tests/long.txt")

board_wide = np.array([["A", "B", "C", "D"], ["E", "F", "G", "H"]])
wide = WordSolver("tests/wide.txt")


def test_horizontal_from_left():
    # given
    sol = long.left_right()

    # expected
    assert all([A == E for A, E in zip(sol[0], ["A", "B"])])
    assert all([A == E for A, E in zip(sol[1], ["C", "D"])])
    assert all([A == E for A, E in zip(sol[2], ["E", "F"])])
    assert all([A == E for A, E in zip(sol[3], ["G", "H"])])

    # given
    sol = wide.left_right()

    # expected
    assert all([A == E for A, E in zip(sol[0], ["A", "B", "C", "D"])])
    assert all([A == E for A, E in zip(sol[1], ["E", "F", "G", "H"])])


def test_horizontal_from_right():
    # given
    sol = long.right_left()

    # expected
    assert all([A == E for A, E in zip(sol[0], ["B", "A"])])
    assert all([A == E for A, E in zip(sol[1], ["D", "C"])])
    assert all([A == E for A, E in zip(sol[2], ["F", "E"])])
    assert all([A == E for A, E in zip(sol[3], ["H", "G"])])

    # given
    sol = wide.right_left()

    # expected
    assert all([A == E for A, E in zip(sol[0], ["D", "C", "B", "A"])])
    assert all([A == E for A, E in zip(sol[1], ["H", "G", "F", "E"])])


def test_vertical_from_bottom():
    # given
    sol = long.bottom_top()

    # expected
    assert all([A == E for A, E in zip(sol[0], ["G", "E", "C", "A"])])
    assert all([A == E for A, E in zip(sol[1], ["H", "F", "D", "B"])])

    # given
    sol = wide.bottom_top()

    # expected
    assert all([A == E for A, E in zip(sol[0], ["E", "A"])])
    assert all([A == E for A, E in zip(sol[1], ["F", "B"])])
    assert all([A == E for A, E in zip(sol[2], ["G", "C"])])
    assert all([A == E for A, E in zip(sol[3], ["H", "D"])])


def test_vertical_from_top():
    # given
    sol = long.top_bottom()

    # expected
    assert all([A == E for A, E in zip(sol[0], ["A", "C", "E", "G"])])
    assert all([A == E for A, E in zip(sol[1], ["B", "D", "F", "H"])])

    # given
    sol = wide.top_bottom()

    # expected
    assert all([A == E for A, E in zip(sol[0], ["A", "E"])])
    assert all([A == E for A, E in zip(sol[1], ["B", "F"])])
    assert all([A == E for A, E in zip(sol[2], ["C", "G"])])
    assert all([A == E for A, E in zip(sol[3], ["D", "H"])])


def test_diag_main_from_top():
    # given
    sol = long.main_diagonal_top_bottom()

    # expected
    assert all([A == E for A, E in zip(sol[0], ["G"])])
    assert all([A == E for A, E in zip(sol[1], ["E", "H"])])
    assert all([A == E for A, E in zip(sol[2], ["C", "F"])])
    assert all([A == E for A, E in zip(sol[3], ["A", "D"])])
    assert all([A == E for A, E in zip(sol[4], ["B"])])

    # given
    sol = wide.main_diagonal_top_bottom()

    # expected
    assert all([A == E for A, E in zip(sol[0], ["E"])])
    assert all([A == E for A, E in zip(sol[1], ["A", "F"])])
    assert all([A == E for A, E in zip(sol[2], ["B", "G"])])
    assert all([A == E for A, E in zip(sol[3], ["C", "H"])])
    assert all([A == E for A, E in zip(sol[4], ["D"])])


def test_diag_main_from_bottom():
    # given
    sol = long.main_diagonal_bottom_top()

    # expected
    assert all([A == E for A, E in zip(sol[0], ["G"])])
    assert all([A == E for A, E in zip(sol[1], ["H", "E"])])
    assert all([A == E for A, E in zip(sol[2], ["F", "C"])])
    assert all([A == E for A, E in zip(sol[3], ["D", "A"])])
    assert all([A == E for A, E in zip(sol[4], ["B"])])

    # given
    sol = wide.main_diagonal_bottom_top()

    # expected
    assert all([A == E for A, E in zip(sol[0], ["E"])])
    assert all([A == E for A, E in zip(sol[1], ["F", "A"])])
    assert all([A == E for A, E in zip(sol[2], ["G", "B"])])
    assert all([A == E for A, E in zip(sol[3], ["H", "C"])])
    assert all([A == E for A, E in zip(sol[4], ["D"])])


def test_diag_anti_from_top():
    # given
    sol = long.anti_diagonal_top_bottom()

    # expected
    print(sol)
    assert all([A == E for A, E in zip(sol[0], ["A"])])
    assert all([A == E for A, E in zip(sol[1], ["B", "C"])])
    assert all([A == E for A, E in zip(sol[2], ["D", "E"])])
    assert all([A == E for A, E in zip(sol[3], ["F", "G"])])
    assert all([A == E for A, E in zip(sol[4], ["H"])])

    # given
    sol = wide.anti_diagonal_top_bottom()
    print(sol)
    # expected
    assert all([A == E for A, E in zip(sol[0], ["A"])])
    assert all([A == E for A, E in zip(sol[1], ["B", "E"])])
    assert all([A == E for A, E in zip(sol[2], ["C", "F"])])
    assert all([A == E for A, E in zip(sol[3], ["D", "G"])])
    assert all([A == E for A, E in zip(sol[4], ["H"])])


def test_diag_anti_from_bottom():
    # given
    sol = long.anti_diagonal_bottom_top()

    # expected
    print(sol)
    assert all([A == E for A, E in zip(sol[0], ["A"])])
    assert all([A == E for A, E in zip(sol[1], ["C", "B"])])
    assert all([A == E for A, E in zip(sol[2], ["E", "D"])])
    assert all([A == E for A, E in zip(sol[3], ["G", "F"])])
    assert all([A == E for A, E in zip(sol[4], ["H"])])

    # given
    sol = wide.anti_diagonal_bottom_top()
    print(sol)
    # expected
    assert all([A == E for A, E in zip(sol[0], ["A"])])
    assert all([A == E for A, E in zip(sol[1], ["E", "B"])])
    assert all([A == E for A, E in zip(sol[2], ["F", "C"])])
    assert all([A == E for A, E in zip(sol[3], ["G", "D"])])
    assert all([A == E for A, E in zip(sol[4], ["H"])])

