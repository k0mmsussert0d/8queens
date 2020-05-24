# 8queens
Python solution for [eight queens puzzle](https://en.wikipedia.org/wiki/Eight_queens_puzzle) with graphical representation of found solution(s). It returns first found solution.

![Demo](test.gif)

## Usage
This repository consists of two packages:
- `eightqueens` - core of the algorithm, performing the search for right configuration
- `gui` - graphical interface, representing found solution on a board by listening for events sent by `eightqueens`

They both can run standalone, but it's best to run them in parallel in order to see human-friendly representation of found solution.

### Installation
In order to run the `gui` package, pygame library of version specified in `requirements.txt` is required. Install it inside environment of your choice by running:
```commandline
pip install -r requirements.txt
``` 

### Running
`demo.py` contains a wrapper function that allows to easily run the algorithm alongside with its GUI: `def eight_queens(n: int, visualize: bool = False)`, where `n` is the size of a chessboard and `visualize` determines whether visualization will be run.

In order to see a solution for classic, 8-fields-sized board, run:
```python
import demo.py
demo.eightqueens(8, True)
```
or run `demo.py` as a script using its `__main__` function:
```commandline
python demo.py
``` 

For running the algorithm without the visualization, run:
```python
import demo.py
demo.eightqueens(8, False)
```

In both cases, solution in form of `n` integers will be printed to stdout. Each represents the row (numbered from 1 to 8, bottom to top) of a single column, moving from the left to the right side of the board.