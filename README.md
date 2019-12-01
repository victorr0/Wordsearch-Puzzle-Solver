## ![badge](https://github.com/ArnoCo/word_search_dictionary_solver/workflows/Lint%20and%20Test/badge.svg)  word_search_dictionary_solver 
Solves word search puzzles in Python using a provided dictionary. The provided one is a JSON file containing Dutch words, replace this one if you're looking for another language.

#### Forked from https://github.com/victorr0/Wordsearch-Puzzle-Solver ##
- Diagonal lines supported
- Extended the provided dutch dictionary
- Restructured solver so certain checks can be enabled/disabled easily

#### Installation

```
pip install -r requirements.txt
```

#### Running the code

Solve the `puzzle.txt` file by running:
```
python3 -m solver.main
```
