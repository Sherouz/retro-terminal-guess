# Retro Terminal Guess 🎮💾

A retro-inspired "Guess the Number" game for the terminal.  
Classic gameplay meets ASCII art, animated terminal effects, and high-score tracking.

---

## Table of Contents 📑

- [Retro Terminal Guess 🎮💾](#retro-terminal-guess-)
  - [Table of Contents 📑](#table-of-contents-)
  - [Features ✨](#features-)
  - [Installation ⚙️](#installation-️)
  - [Usage 🕹️](#usage-️)
  - [Roadmap 🚀](#roadmap-)
  - [Documentation 📂](#documentation-)
  - [Contributing 🤝🏽](#contributing-)
  - [License 📃](#license-)
  - [Donation 💸](#donation-)
  - [Acknowledgments 🙌🏽](#acknowledgments-)

---

## Features ✨

- **Gameplay**  
  - Random number generation (default range: 1–50)  
  - Feedback for each guess: LOW / HIGH / CORRECT  
  - Attempts counter per round  

- **Retro Terminal Effects**  
  - ASCII-art boot screen & startup simulation  
  - Animated loading bars  
  - Typewriter-style text  
  - Retro feedback/error messages  

- **High Score Tracking**  
  - Records lowest attempts across rounds  
  - Updates automatically  
  - Shown on exit  

- **Modular Python Architecture**  
  - `src/core/game_logic.py` – Core mechanics  
  - `src/core/ui.py` – Terminal effects and UI  
  - `src/core/utils.py` – Helpers  
  - `ascii_art/terminal_style.py` – ASCII boot messages  
  - `main.py` – Entry point & game loop  

---

## Installation ⚙️

```bash
# Clone the repository
git clone https://github.com/Sherouz/retro-terminal-guess.git

# Install dependencies
pip install -r requirements.txt

# Run the game
python main.py
````

---

## Usage 🕹️

1. Startup shows retro boot screen
2. Type `START` to begin
3. Enter a guess within the displayed range
4. Get retro-style feedback until correct
5. Play again (Y/N)
6. High score shown on exit

---

## Roadmap 🚀

Planned enhancements:

* Difficulty levels (larger ranges)
* Timer-based challenge mode
* Persistent high scores (saved to file)
* Sound effects for terminal actions
* Expanded ASCII art & animations

---

## Documentation 📂

Hack into the system’s core intel! The full directory layout lives in [docs/STRUCTURE.md](docs/STRUCTURE.md).

**Documentation Highlights**:

* **[CHANGELOG.md](docs/CHANGELOG.md)** – Track the game’s evolution with version updates and patch notes.
* **[OVERVIEW.md](docs/OVERVIEW.md)** – The big picture: project purpose and mission.
* **[STRUCTURE.md](docs/STRUCTURE.md)** – Full file & directory map.
* **[PLAN.md](docs/PLAN.md)** – Roadmap & upcoming features.
* **[TODO.md](docs/TODO.md)** – Task list & pipeline ideas.
* **[DONATE.md](docs/DONATE.md)** – Support the project and keep the neon vibes alive.

> *Pro Tip:* These docs are your cyber-terminal’s control hub – dive in to master the system! 🚀

---

## Contributing 🤝🏽

1. Fork the repo
2. Create a feature branch
3. Commit with clear messages
4. Submit a pull request with description

---

## License 📃

Distributed under the [MIT License](LICENSE).

---

## Donation 💸

Love the cyber-terminal vibes? Support the project:

* See [docs/DONATE.md](docs/DONATE.md) for ways to contribute.
* Every bit fuels new features and keeps the neon glowing. 💖

---

## Acknowledgments 🙌🏽

- Inspired by [Monster-Brawl](https://github.com/NazaNEYn/Monster-Brawl-Game) by [Naz Ashrafi](https://github.com/NazaNEYn).  
- Based on the "Guess the Number" project from [Kylie Ying](https://github.com/kying18)'s YouTube tutorial, with thanks to FreeCodeCamp.
- Inspired by vintage hacker terminals, text-based games, and cyberpunk aesthetics.
- Powered by the Python community and its stellar documentation.
- Shoutout to testers and contributors who keep the system running smoothly.
- A shoutout to the programming community for providing endless inspiration and support.

> For a personal note of thanks, check out [THANKS.md](THANKS.md) 💖
---

📅 **DATE: AUGUST 22, 2025**
👉 For the **full retro cyberpunk experience**, check out [docs/OVERVIEW.md](docs/OVERVIEW.md).

```

```
