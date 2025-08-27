# Project Structure - Retro Terminal Guess

This document outlines the **directory and file structure** of the Retro Terminal Guess project for clarity and maintainability.

---

## 1. Root Directory

```
retro-terminal-guess/
│
├── README.md               # Project introduction and quick start guide
├── LICENSE                 # Project license
├── requirements.txt        # Dependencies for Python environment
├── .gitignore              # Ignore files and folders like pycache, env, etc.
├── merged_guessing_game.py # Optional: Merged script for testing
├── python merge_guessing_game.py # Optional dev/test script
└── pytest.ini              # Pytest configuration
```

## 2. Documentation

```
docs/
├── CHANGELOG.md            # Project changelog
├── Donate.md               # Donation info or support
├── OVERVIEW.md             # Project overview and purpose
├── PLAN.md                 # Future plans and roadmap
└── STRUCTURE.md            # This file: directory structure documentation
```

## 3. Source Code

```
src/
├── __init__.py            # Marks src as a package
└── core/                  # Core game logic, UI, and helpers
   ├── __init__.py
   ├── game_logic.py      # Number generation and guess checking
   ├── main.py            # Entry point for the game
   ├── ui.py              # Terminal UI and animations
   └── utils.py           # Helper functions (play again, input validation)
```

## 4. ASCII Art

```
ascii_art/
└──terminal_style.py       # Retro ASCII messages and boot screens
```

## 5. Tests

```
tests/
├── __init__.py
├── test_game_logic.py      # Unit tests for game logic
├── test_main.py            # Tests for main game loop
├── test_ui.py              # Tests for UI functions
└── test_utils.py           # Tests for helper functions

```

## 6. Sandbox / Experimental Code

```
sandbox/
# Use for prototyping, experiments, or temporary scripts
```

## Notes

* Keep **core game logic, UI, and helpers** separate from ASCII/art assets.
* Tests should cover all core functionality and run independently.
* Sandbox is for development experiments and is optional for the public release.
* Use `docs/` to maintain all long-form documentation, flow diagrams, and project plans.
