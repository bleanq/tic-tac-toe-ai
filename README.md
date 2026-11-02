# Tic-Tac-Toe AI

A console Tic-Tac-Toe game in Python where you play against the computer.
On the hard level the computer uses the **minimax** algorithm and never loses.

```
 X | 2 | O
---+---+---
 4 | X | 6
---+---+---
 7 | 8 | O
```

## Features

- Three difficulty levels:
  - **Easy**: random moves
  - **Medium**: best move half of the time
  - **Hard**: full minimax search, impossible to beat
- Play as X (first) or O (second)
- Score kept across rounds
- Input validation: wrong or occupied cells are rejected
- Unit tests, including a check of every possible game against the hard AI

## How to run

Requires Python 3.8+, no extra libraries.

```bash
python game.py
```

Run the tests:

```bash
python -m unittest -v
```

## How the AI works

Minimax tries every possible continuation of the game. The computer assumes
the opponent always plays their best move and picks the move with the best
guaranteed result. Faster wins score higher, so the AI finishes the game as
soon as it can.

## Tech

Python · unittest · algorithms (minimax, game tree search)
