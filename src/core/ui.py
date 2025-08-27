# ui.py - User interaction layer & User Interface functions for the game

import sys
import time

from typing import Callable
from other.ascii_art.terminal_style import retro_boot_message
from src.core.constants import COMMAND_START, COMMAND_EXIT, INVALID_INPUT
from .constants import GUESS_RESULTS

def type_out(text, 
             speed=0.02,
             printing: Callable[[str], None] = sys.stdout.write
            ):
    """
    Prints text character-by-character to simulate an old terminal feel.

    This function outputs the given text one character at a time, with a small delay
    between each character to create a retro terminal typing effect.

    Args:
        text: The text string to display on the terminal.
        speed: Delay (in seconds) between each character. Defaults to 0.02 seconds.
        printing: A callable used to output each character. Defaults to sys.stdout.write,
            but can be replaced with any function that takes a string, such as print,
            a logging function, or a custom GUI text display function.

    Returns:
        None
    """

    for char in text:
        printing(char)
        sys.stdout.flush()  # Required for immediate display of changes
        time.sleep(speed)   # Delay for animation effect
    print()

def animated_loading_bar(total=25, 
                         speed=0.1, 
                         printing: Callable[[str], None] = sys.stdout.write
                        ) -> None:
    """
    Renders a retro-style animated loading bar in the terminal.

    This function displays a loading bar that fills segment by segment, simulating
    a classic terminal loading animation. Each segment is displayed with a small
    delay to give the retro feel.

    Args:
        total: Number of segments in the loading bar, determining the total bar length.
            Defaults to 25.
        speed: Delay (in seconds) between filling each segment. Defaults to 0.1 seconds.
        printing: A callable used to output each segment. Defaults to sys.stdout.write,
            but can be replaced with any function that takes a string, such as print,
            a logging function, or a GUI element for custom display.

    Returns:
        None
    """

    bar = ["░"] * total # List filled with empty blocks for displaying the bar
    for i in range(total):
        bar[i] = "█"
        printing("\r[ " + "".join(bar) + " ]")
        sys.stdout.flush() 
        time.sleep(speed)
    print()

def display_welcome(delay: float = 0.05, inputing: Callable[[str], None] = input) -> bool:
    """
    Displays the retro boot-up welcome message and waits for the user to type 'START'.

    This function prints the ASCII-art retro boot screen line by line with a character
    delay to simulate old-school terminal output, shows an animated loading bar,
    and then waits for user input to continue the program.

    Args:
        delay: Delay (in seconds) between characters when printing the welcome screen.
            Defaults to 0.05 seconds.
        inputing: A callable used to read input from the user. Defaults to the built-in
            input function. This allows redirecting input from other sources, such as
            a GUI prompt or automated test input.

    Returns:
        bool: True if the user types 'START' to proceed, False otherwise.
    """

    # Print initial messages one by one with typing effect
    for line in retro_boot_message.strip().splitlines():
        type_out(line, delay, printing=sys.stdout.write)
        if "CHECKING INPUT DEVICES... DONE" in line:
            animated_loading_bar(printing=sys.stdout.write)
            
    # Wait for user to type START or exit
    while True:
        command = inputing(">>> ").strip().upper()
        if command == COMMAND_START:
            type_out(r"""
[ SYSTEM MESSAGE ]
>>> GAME STARTED! GOOD LUCK!
""", 0.03, printing=sys.stdout.write)
            return True
        elif command in [COMMAND_EXIT, ""]: 
            type_out(r"""
[ SYSTEM SHUTDOWN ]
>>> USER CHOSE TO ABORT LAUNCH. EXITING GAME...
""", 0.03, printing=sys.stdout.write)
            return False
        else:
            type_out(r"""
[ ERROR ]
>>> INVALID COMMAND. TYPE 'START' TO BEGIN OR TYPE 'EXIT' / PRESS 'ENTER' TO LEAVE.
""", 0.03, printing=sys.stdout.write)

# Print feedback message depending on guess result
def print_feedback(result: str,
                   target: int = None,
                   printing: Callable[[str], None] = print
                   ) -> None:
    """
    Print retro terminal-style feedback based on the guess result.

    This function provides feedback messages in a retro terminal style depending
    on the player's guess outcome. The messages inform the player whether their
    guess is too low, too high, correct, or out of the allowed range.

    Args:
        result: The outcome of the player's guess. Expected values:
            - "low": The guess is below the target number.
            - "high": The guess is above the target number.
            - "correct": The guess matches the target number.
            - "out_of_range_low": The guess is less than 1.
            - "out_of_range_high": The guess is greater than max_num.
        target: The target number (used only if result is "correct"). Defaults to None.
        printing: A callable used to output the feedback messages. Defaults to
            the built-in print function. This allows redirecting messages to
            a different output stream, such as a log file or a GUI element.

    Returns:
        None
    """

    if result == GUESS_RESULTS["LOW"]:
        printing("[ ACCESS DENIED ] Input value too LOW. >> Retry sequence.")
    elif result == GUESS_RESULTS["HIGH"]:
        printing("[ ACCESS DENIED ] Input value too HIGH. >> Retry sequence.")
    elif result == GUESS_RESULTS["CORRECT"]:
        printing(f"[ SYSTEM OVERRIDE GRANTED ] Code {target} ACCEPTED. >> Access unlocked.")
    elif result == GUESS_RESULTS["OUT_OF_RANGE_LOW"]:
        printing("[ ERROR 0x01 ] Input value below minimum (1). >> Enter a valid number.")
    elif result == GUESS_RESULTS["OUT_OF_RANGE_HIGH"]:
        printing("[ ERROR 0x02 ] Input value exceeds maximum. >> Enter a valid number.")
    elif result == INVALID_INPUT:
        printing("[ ERROR ] Invalid input detected. >> Enter a number.")
