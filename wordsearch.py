#!/usr/bin/python3

import json
import numpy as np

with open('dictionary.json','r',encoding='utf-8') as f:
    data = json.load(f)['words']

solutions = set([item.upper() for item in data])

def solve(file):
    """
    Solves a wordsearch puzzle
    """
    word_grid = open(file,'r').read().split('\n')[:-1]
    found_words = []
    line_lr = {}
    line_tb = {}
    directions = [line_lr, line_tb]

    for line in word_grid:
        line_lr[word_grid.index(line)] = line

    for i in range(len(word_grid)):
        line_tb[i] = [(line[i]) for line in word_grid]
        line = line_tb[i]
        line_tb[i] = (''.join(line))
    
    for direction in directions:
        for line in direction:
            for word in solutions:
                if word in direction[line]:
                    found_words.append(word)
         
    return found_words

def solve_advanced(file):

    word_grid = open(file,'r').read().split('\n')[:-1]
    found_words = []
    line_lr = {}
    line_tb = {}
    line_rl = {}
    line_bt = {}
    line_hd_t = {}
    line_hd_b = {}
    line_ad_t = {}
    line_ad_b = {}
    directions = [line_lr, line_tb, line_rl, line_bt, line_hd_t, line_hd_b, line_ad_t, line_ad_b]

    for i, line in enumerate(word_grid):
        line_lr[i] = line

    for i in range(len(word_grid)):
        line_tb[i] = [(line[i]) for line in word_grid]
        line = line_tb[i]
        line_tb[i] = (''.join(line))
        
    for i in line_lr:
        line_rl[i] = [i for i in reversed(line_lr[i])]
        line = line_rl[i]
        line_rl[i] = (''.join(line))
        
    for i in line_tb:
        line_bt[i] = [i for i in reversed(line_tb[i])]
        line = line_bt[i]
        line_bt[i] = (''.join(line))

    # current assumption is that the grid is square, this is easy to generalize (or pad)
    new_grid = np.array([[s for s in x] for x in word_grid])
    for i in range(-len(new_grid),len(new_grid)):
        line_hd_t[i + len(new_grid)] = new_grid.diagonal(i)
        line_hd_b[i + len(new_grid)] = reversed(new_grid.diagonal(i))

    
    new_grid = np.flip(np.array([[s for s in x] for x in word_grid]), axis=0)
    for i in range(-len(new_grid),len(new_grid)):
        line_ad_t[i + len(new_grid)] = new_grid.diagonal(i)
        line_ad_b[i + len(new_grid)] = reversed(new_grid.diagonal(i))

    for dic in [line_hd_t, line_hd_b, line_ad_t, line_ad_b]:
        for key in dic:
            dic[key] = "".join(dic[key])


    for direction in directions:
        for line in direction:
            for word in solutions:
                if word in direction[line]:
                    found_words.append(word)
    return set(list(filter(lambda x: len(x)>1,found_words)))
