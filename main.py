#!/usr/bin/python3

# File name: main.py
# Executes the wordsearch function.
# Assignment by Victor for the Advanced Programming course
# Date: 23-2-2016

from wordsearch import solve
from wordsearch import solve_advanced


def main():
    #Testing wordsearch's solve & solve_advanced
    file = 'puzzle1.txt'
    print(solve(file))
    print(solve_advanced(file))
    
    file = 'puzzle2.txt'
    print(solve(file))
    print(solve_advanced(file))

main()

