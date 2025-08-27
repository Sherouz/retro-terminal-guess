# main.py - Entry point for the Guess the Number game
# Python Script - Retro Terminal Guess Game Entry Point

"""
Purpose: Entry script for the "Retro Terminal Guess" game with retro ASCII art style,
high score tracking, and a more immersive UX.
"""

from src.core.ui import display_welcome, print_feedback
from src.core.game_logic import generate_number, check_guess
from src.core.utils import ask_play_again
from other.ascii_art.terminal_style import retro_boot_message

# Global variable for high score (lowest number of attempts)
HIGH_SCORE = None

def play_game(max_num: int) -> None:
    """
    Run the main game loop for Retro Terminal Guess game.

    Generates a random target number, tracks attempts, prompts user for guesses until correct or exit,
    and updates/displays high score at the end of each round.

    Args:
        max_num: Upper bound for the random number.   # if # if 

    Returns:
        None
    """
    global HIGH_SCORE

    target = generate_number(max_num)
    attempts = 0

    print(f"\n[ SYSTEM MESSAGE ] A secret number has been chosen between 1 and {max_num}...")

    while True:
        try:
            user_input = input(f"\n> Enter your guess (1-{max_num}) or press Enter to exit: ")

            if user_input == "":
                print("\n[ SYSTEM EXIT ] You chose to quit mid-game. See you next time!")
                return

            guess_num = int(user_input)
            if guess_num < 1:
                print("\n[ ERROR 0x01 ] Input value below minimum (1). >> Enter a valid number.")
                continue
            elif guess_num > max_num:
                print(f"\n[ ERROR 0x02 ] Input vaslue exceeds maximum ({max_num}). >> Enter a valid number.")
                continue
            else:
                attempts += 1

            result = check_guess(guess_num, target, max_num)
            print_feedback(result, target)

            if result == "correct":
                print(f"\n[ SUCCESS ] You guessed the number in {attempts} attempts! 🎯")

                if HIGH_SCORE is None or attempts < HIGH_SCORE:
                    HIGH_SCORE = attempts
                    print("[ NEW RECORD ] Congratulations! You set a new high score! 🏆")
                else:
                    print(f"[ HIGH SCORE ] Current record is {HIGH_SCORE} attempts. 🆕")

                break

        except ValueError:
            print("\n[ ERROR 0x04 ] Invalid input detected. Only numbers are allowed.")

def main() -> None:
    """Serve as the entry point for the Retro Terminal Guess game.

    Displays a retro ASCII art welcome message, runs the main guessing game loop,
    allows multiple rounds with high score tracking, and shows a retro exit message 
    when the user quits.

    Returns:
        None
    """
    
    if not display_welcome():
        return
    
    while True:
        play_game(max_num=50)

        if not ask_play_again():
            print("\n[ SYSTEM SHUTDOWN ] Thanks for playing. Game over.")
            if HIGH_SCORE is not None:
                print(f"[ FINAL HIGH SCORE ] Best performance: {HIGH_SCORE} attempts.")
            print("\n------- > Goodbye, retro warrior. < -------\n")
            break
        
if __name__ == "__main__":
    main()