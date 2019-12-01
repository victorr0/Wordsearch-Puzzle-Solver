from solver.wordsearch import WordSolver


def main():

    solver = WordSolver("puzzle.txt")
    for i, sol in enumerate(solver.solve()):
        print(sol, end="\t\t")
        if i % 4 == 0:
            print()


main()
