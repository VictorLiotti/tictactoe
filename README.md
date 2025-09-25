# TicTacToe

![Project Banner](./assets/banner.png)

## Table of Contents

- [About](#about)
- [Demo](#demo)
- [Features](#features)
- [Tech & Concepts](#tech--concepts)
- [Repository structure](#repository-structure)
- [Quick start](#quick-start)
- [Gameplay](#gameplay)
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
- Configurable computer opponent difficulty (Easy / Normal / Hard)
  - Hard uses Minimax (optimal play) with:
    - Alpha–Beta pruning (search optimization)
    - Depth-weighted evaluation (prefer faster wins, delay defeats)
- Choice of symbol (X or O) and who plays first
- Win/draw detection and move validation
- Customizable victory/defeat/draw messages (from `messages.py`)
- Replay support
- Unit tests covering core game logic

## Tech & Concepts

- Language: Python 3.13.6
- Libraries: `numpy`, `random`, `unittest`
- Keywords: Command-Line Interface (CLI), turn-based game, Minimax

## Repository structure

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


