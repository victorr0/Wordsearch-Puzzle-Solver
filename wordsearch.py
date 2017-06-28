#!/usr/bin/python3

# File name: wordsearch.py
# a module wordsearch with a function solve. The function takes
# the path to a text file with a word search puzzle, e.g. puzzle1.txt
# Assignment by Victor for the Advanced Programming course
# Date: 23-2-2016

from collections import defaultdict
import json

with open('words.json','r',encoding='utf-8') as f:
    data = json.load(f)['words']
solutions = set([item.upper() for item in data])

def solve(file):
    """
    Solves a wordsearch puzzle
    """
    word_grid = open(file,'r').read().split('\n')[:-1]
    found_words = []
    regel_lr = {}
    regel_tb = {}
    directions = [regel_lr, regel_tb]

    for line in word_grid:
        regel_lr[word_grid.index(line)] = line

    for i in range(len(word_grid)):
        regel_tb[i] = [(line[i]) for line in word_grid]
        regel = regel_tb[i]
        regel_tb[i] = (''.join(regel))
    
    for direction in directions:
        for line in direction:
            for word in solutions:
                if word in direction[line]:
                    found_words.append(word)
         
    return found_words

def solve_advanced(file):
    """
    Still working on this, solves a wordsearch puzzle more advanced
    """
    word_grid = open(file,'r').read().split('\n')[:-1]
    found_words = []
    regel_lr = {}
    regel_tb = {}
    regel_rl = {}
    regel_bt = {}
    directions = [regel_lr, regel_tb, regel_rl, regel_bt]

    for line in word_grid:
        regel_lr[word_grid.index(line)] = line

    for i in range(len(word_grid)):
        regel_tb[i] = [(line[i]) for line in word_grid]
        regel = regel_tb[i]
        regel_tb[i] = (''.join(regel))
        
    for i in regel_lr:
        regel_rl[i] = [i for i in reversed(regel_lr[i])]
        regel = regel_rl[i]
        regel_rl[i] = (''.join(regel))
        
    for i in regel_tb:
        regel_bt[i] = [i for i in reversed(regel_tb[i])]
        regel = regel_bt[i]
        regel_bt[i] = (''.join(regel))
    
    for direction in directions:
        for line in direction:
            for word in solutions:
                if word in direction[line]:
                    found_words.append(word)
    return found_words
