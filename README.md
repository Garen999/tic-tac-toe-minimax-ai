# Noughts and Crosses AI — Minimax Algorithm

A Python-based, command-line Noughts and Crosses game featuring an AI opponent powered by the **Minimax algorithm**.

This independent programming project was developed to explore recursive algorithms, game-tree search and decision-making in adversarial games.

## Features

- Interactive, terminal-based Noughts and Crosses
- Human player (X) versus AI opponent (O)
- Recursive Minimax algorithm for evaluating possible moves
- AI decision-making based on optimal play
- Win and draw detection
- Implemented using standard Python without external libraries

## How Minimax Works

Minimax is a recursive decision-making algorithm used in two-player, turn-based games.

The algorithm explores possible future board states and assigns scores to terminal outcomes:

| Outcome | Score |
|---|---|
| AI (O) wins | +1 |
| Human (X) wins | -1 |
| Draw | 0 |

The AI aims to **maximise** the score, while the human opponent is assumed to **minimise** it.

By recursively evaluating possible moves, the AI selects the move with the best guaranteed outcome, assuming optimal play from both players.

## Implementation

The program separates the game logic and AI decision-making into several functions:

- `get_next_states()` — generates possible board states for the current player.
- `minimax()` — recursively evaluates board states and returns their optimal scores.
- `get_best_move()` — compares the scores of available AI moves and selects the highest-scoring move.
- `player_turn()` — handles human input and AI moves.

## Getting Started

**Requirements:** Python 3

1. Clone or download this repository.
2. Open the project directory in a terminal.
3. Run the main Python game file.
4. Follow the terminal prompts to play against the AI.

No additional dependencies are required.

## What I Learned

Through developing this project, I gained practical experience with:

- Recursion and recursive function calls
- Game trees and state-space exploration
- Minimax and adversarial decision-making
- Python dictionaries, lists and state management
- Debugging recursive algorithms
- Breaking a larger problem into smaller, reusable functions

## Development

This project was independently implemented in Python. Educational resources and AI-assisted explanations were used to understand Minimax, recursion and debugging, while the game's implementation was developed through my own programming and problem-solving.

## Possible Improvements

- Alpha-beta pruning to reduce unnecessary evaluations
- Depth-based scoring to prioritise faster wins
- Adjustable AI difficulty levels
- A graphical user interface