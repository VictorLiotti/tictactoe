# TicTacToe

![Project Banner](./assets/banner.png)

## Table of Contents

- [About](#about)
- [Demo](#demo)
- [Features](#features)
- [Tech & Concepts](#tech--concepts)
- [Repository structure](#repository-structure)
- [Quick start](#quick-start)
- [How to play](#how-to-play)
- [AI](#ai)
- [Running tests](#running-tests)
- [Roadmap / Ideas](#roadmap--ideas)
- [License](#license)
- [Author / Contact](#author--contact)

## About

TicTacToe is a clean, well-documented implementation of the classic 3×3 game written in Python.
I built this project to practice object-oriented programming (OOP) and to learn basic AI concepts — specifically the minimax algorithm.

## Demo
![Game demo](./assets/demo.gif)

## Features

- Game modes: Local PvP (Player vs Player) and PvC (Player vs Computer)
- "Computer" difficulty (Easy / Normal / Hard)
  - Hard uses Minimax (optimal play) with:
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

## Quick start

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

Each turn a player chooses an available position on the board to put its symbol there.

Positions marked with a symbol are no longer available.

The player that fills a whole row, column or diagonal with its symbol wins.

If there are no available positions left and nobody won, then its a draw.


### Playing

The game runs in the terminal (CLI).

Initially, you will be asked about game mode.

- If you choose PvP you are ready to go: PvP is local. Player 1 plays first and uses symbol X, Player 2 uses symbol O.
- If you choose PvC:
 - You will be asked about computer opponent difficulty: Easy, Normal or Hard.
  - Easy mode: computer plays randomly the whole game.
  - Normal mode: computer plays randomly untill it identify a trivial play: immenent victory or defeat. In that case it makes the optimum play.
  - Hard mode: computer uses minimax algorithm to decide the optimum plays all the time. It won't lose. You can read more about it in [AI](#ai) section.
 - You will have to choose which symbol you want to play with (X or O) and who plays first.

On each turn a player chooses an available position on the board and type the corresponding number to place its symbol (X or O) there. The board will be printed on the terminal.

When the game ends, you will can may choose replay for a playing it again.

## AI

Minimax is a recursive algorithm that simulate all possible moves ahead (until certain depth) and chooses the best play at the time.

Each move simulated creates a board state, also called node. If some moves still available, new nodes (of depth d+1) are formed from the previous one (depth d), making branches. The "tree" ends at the terminal states (end of game: victory/defeat/draw).

The algorithm assigns scores for the terminal states: 10 for victory, -10 for defeat and 0 for draw (these values were used in this program, but are arbitrary and should be chosen depend on case to case).

Starting at the deepest depth (D), the terminal scores are compared and passed to the previous node (depth D-1) depending on which player's turn that depth represent. The "player's turn" decides the logic: maximazing or minimazing the scores. Then all scores of depth D-1 are compared and passed, according to the inverse logic, to depth D-2. Each level the scores are passed above and the logic alternates (Min, Max, ...) until depth 0, where the position of maximum value is chosen as optimum move.

Let's assume a node is located at depth d and this depth corresponds to Computer turn. Computer wants to maximize its chance of winning: Computer is called MAX. Therefore the node will get the maximum value of its branches at depth d+1. Moving up, depth d-1 represents the user. User wants Computer to lose, it will minimize Computer's chances of winning: User is called MIN. Therefore, the score passed to node of depth d-1 is the mimimum of its branches at level d. The logic alternates. Thats were the name MINIMAX comes from.

The way Minimax was explained, it would have to analyse all nodes. But is possible to cut-off some branches, and therefore saving time and computational power, by using Alpha-Beta pruning.




