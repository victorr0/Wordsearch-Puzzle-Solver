#!/usr/bin/python3

from wordsearch import solve
from wordsearch import solve_advanced


def main():

    file = 'puzzle.txt'
    sorted_solution = sorted(sorted(solve_advanced(file)), key=lambda x: len(x))
    for i, sol in enumerate(sorted_solution):
        print(sol, end="\t\t")
        if i % 4 == 0:
            print()

main()

