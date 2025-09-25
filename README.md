# TicTacToe

![Project Banner](./assets/banner.png)


## Table of Contents

- [About](#about)
- [Features](#features)
- [Tech & Concepts](#tech--concepts)
- [Repository structure](#repository-structure)
- [How to install](#how-to-install)
- [How to play](#how-to-play)
- [Demo](#demo)
- [AI](#ai)
- [Running tests](#running-tests)
- [Next steps](#next-steps)
- [License](#license)
- [Author / Contact](#author--contact)


## About

TicTacToe is a clean, well-documented implementation of the classic 3×3 game written in Python.
I built this project to practice object-oriented programming (OOP) and to learn basic AI concepts — specifically the minimax algorithm.


## Features

- Game modes: Local PvP (Player vs Player) and PvC (Player vs Computer)
- Computer difficulty (Easy / Normal / Hard)
  - **Hard** uses Minimax (optimal play) with:
    - Alpha–Beta pruning (search optimization)
    - Depth-weighted evaluation (prefer faster wins, delay defeats)
- Choice of symbol (X or O) and who plays first
- Win/draw detection and move validation
- Customizable victory/defeat/draw messages (from `messages.py`)
- Replay option
- Unit tests covering game logic


## Tech & Concepts

- Language: Python 3.13.6
- Libraries: `numpy`, `random`, `unittest`
- Keywords: Command-Line Interface (CLI), turn-based game, Minimax


## Repository structure
```
tictactoe/
├── tictactoe.py # main executable
├── messages.py # strings/messages used by the CLI
├── tests/
│ └── test_tictactoe.py
├── assets/
│ ├── demo.gif
│ └── banner.png
├── .gitignore
├── README.md
└── LICENSE
```


## How to install

1. Clone the repository
```bash
git clone git@github.com:VictorLiotti/tictactoe.git
cd tictactoe
```

2. Run the game
```
python tictactoe.py
```


## How to play

### Board

The board is a 3x3 grid numbered from 1 to 9

```
 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9
```


### Rules

- Each turn a player chooses an available position on the board to put its symbol there.
- Positions marked with a symbol are no longer available.
- The first player to fill a full row, column, or diagonal with their symbol wins.
- If all positions are filled with no winner, then its a draw.


### Playing

- The game runs in the terminal (CLI).
- Choose a game mode:
	- **PvP** — local two-player mode. Player 1 is X and plays first; Player 2 is O.
	- **PvC** — play against the computer:
		- Choose difficulty: Easy, Normal or Hard.
			- **Easy** mode: computer plays randomly.
			- **Normal** mode: computer plays randomly except when an imminent win or loss is detected; in that case it plays optimally.
			- **Hard** mode: computer uses Minimax (optimal play) with alpha–beta pruning and depth weighting — it will not lose. You can read more about it in [AI](#ai) section.
		- Choose your symbol (X or O) and who plays first.

- On each turn, the corresponded player type the number of the position where he wants to place his symbol. The board updates in the terminal.
- When the game ends, you will be offered the option to replay.


## Demo

<a href="./assets/demo.gif">
  <img src="./assets/demo.gif" alt="Game demo" width="480" />
</a>


## AI

The computer opponent uses the **minimax algorithm**, a recursive search method commonly applied in turn-based games. The idea is simple: simulate all possible moves ahead and pick the one that guarantees the best outcome assuming the opponent also plays optimally.

Each simulated move creates a new board state, also called a *node*. If moves are still available, new child nodes are generated, forming a game tree. The tree ends at *terminal states* (or leaves) — win, loss, or draw.

At the leaves, scores are assigned: in this project **+10 for a win, –10 for a loss, and 0 for a draw**. The raw scores are also **depth-weigthed** to differentiate between faster and slower outcomes:
- **Faster wins** (fewer moves) get higher scores, e.g. `10 – depth`.
- **Slower defeats** (more moves before losing) get less negative scores, e.g. `depth – 10`.
- Draws remain at 0.

These base values are arbitrary and can be tuned for different games, but the relative order must be preserved — ensuring that, even after depth weighting, **victory > draw > defeat** in all scenarios.

The algorithm then works backwards (backpropagation). Starting from the deepest depth:
- If it is the **computer’s turn (MAX)**, the node takes the *maximum* value of its children.
- If it is the **player’s turn (MIN)**, the node takes the *minimum* value of its children.

This alternation continues up the tree until depth 0, where the root node corresponds to the current board. The move leading to the best score at the root is chosen as the optimal play.

This max–min alternation explains the name **Minimax**.  
- **MAX (computer)** tries to maximize the score.  
- **MIN (player)** tries to minimize the score.

By default, minimax explores the entire tree. However, many branches can be ignored without changing the result by using **alpha–beta pruning**. Alpha (best already guaranteed for MAX) and beta (best already guaranteed for MIN) act as bounds. If a branch cannot possibly improve the outcome, it is cut off. This greatly reduces the number of nodes explored, making the algorithm faster and more efficient.


## Running tests

This project includes unit tests to validate the game logic.

Using unittest (built-in):
```
python -m unittest discover -v
```

## Next steps

> Not necessarily in priority order

- Add GUI
- Change difficulty by limiting search depth.
- Add remote online PvP
- Customizable symbols for players
- Separate completly the UI and game engine (break tictactoe.py into 2 scripts)

## License

This project is MIT licensed.


## Author / Contact

Víctor L. - [Github](https://github.com/VictorLiotti) - [Linkedin](https://www.linkedin.com/in/victor-liotti)