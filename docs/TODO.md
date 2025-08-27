# Retro Terminal Guess - TODO

This file outlines tasks and planned improvements for the "Retro Terminal Guess" game.

---

## 1. Simple Enhancements (Learning & Practice)

- [ ] Add multiple levels: Introduce multiple difficulty levels; for harder levels, **hints will also be provided**.
- [ ] Attempt Limit: Set a maximum number of guesses per round (e.g., 7 attempts).
- [ ] Input Validation for Decimal Steps: In nightmare mode, guesses must be multiples of 0.25.
- [ ] Prompt Enhancements: Display the remaining number of attempts in the guess prompt (e.g., "3 attempts left").
- [ ] Skip Animations: Allow the player to press a key (e.g., Esc) to skip all ongoing animations instantly.

---

## 2. Fun & Visual Features

- [ ] Randomized Feedback Messages: Use a list of messages and pick one randomly instead of always "Too low"/"Too high".
- [ ] Colored Text: Use `colorama` or `rich` to color success, error, and info messages.
- [ ] Timer Display: Track how long it takes the player to guess the number and show it.
- [ ] ASCII Animations & Retro Effects:
  - [ ] Different loading bar variations
  - [ ] Character-by-character typing effect
  - [ ] Optional coin insert animation before START

---

## 3. Advanced Features (Challenge & Depth)

- [ ] Computer Guesses Mode: Reverse the game—player thinks of a number, computer guesses using binary search.
- [ ] High Score Persistence: Store best score in a file (`scores.txt` or `scores.json`) for session-to-session tracking.
- [ ] Nightmare Mode Enhancements:
  - [ ] Give subtle hints for decimal guesses (e.g., "number is smaller than 23.50").
  - [ ] Enforce step validation strictly so invalid decimal inputs are rejected.
- [ ] Difficulty Expansion:
  - [ ] `expert`: up to 200
  - [ ] `insane`: up to 500
  - [ ] Additional fun/fanatic modes with custom ranges and step sizes.
- [ ] Challenge Modes:
  - [ ] Timed rounds
  - [ ] Limited attempts with penalties
  - [ ] Randomized effects like swapping high/low messages

---

## 4. UX & Structural Improvements

- [ ] Refactor Main Loop: `main.py` should orchestrate game start, welcome screen, and replay loop.
- [ ] Enhanced ASCII Art Integration: Use all ASCII messages from `ascii_art/` with proper functions.
- [ ] Error & UX Handling:
  - [ ] Retro-style system logs for actions
- [ ] Unit Tests Coverage: Ensure `game_logic`, `ui`, and `utils` are fully tested.

---

## 5. Optional / Future Ideas

- [ ] Sound effects for correct/wrong guesses (beep or retro sounds).
- [ ] Online leaderboard or sharing scores.
- [ ] Special events / Easter eggs in the game.
- [ ] Colorful retro backgrounds or terminal themes.

---

> **Next Step Recommendation:**  
> I want to focus first on:
> 1. Limiting the number of attempts
> 2. Strict decimal validation in Nightmare mode
> 3. Modularizing the current functions
>
> Once the logic is solid, I want to move on to fun, visual, and advanced features.
