# game_logic.py - Core game mechanics

import random
from .constants import GUESS_RESULTS
from src.core.constants import INVALID_INPUT

def generate_number(max_num: int) -> int:
    """
    Generates a random integer between 1 and max_num (inclusive).

    Args:
        max_num: The upper bound for the random number.

    Returns:
        A randomly generated integer between 1 and max_num.
    """
    return random.randint(1, max_num)

def check_guess(guess_num: any, target: int, max_num: int) -> str:
    """
    Compare the user's guess with the target number and validate range.

    Args:
        guess_num: The number guessed by the user.
        target: The target number to be guessed.
        max_num: The upper bound for valid guesses.

    Returns:
        A string indicating the result:
            - "low" if guess_num < target but within range
            - "high" if guess_num > target but within range
            - "correct" if guess_num == target
            - "out_of_range_low" if guess_num < 1
            - "out_of_range_high" if guess_num > max_num
            - "Invalid" if guess_num cannot be converted to an integer
    """

    try:

        guess_num = int(guess_num)
    except ValueError:
        return INVALID_INPUT

    if guess_num < 1:
        return GUESS_RESULTS["OUT_OF_RANGE_LOW"]
    if guess_num > max_num:
        return GUESS_RESULTS["OUT_OF_RANGE_HIGH"]
    if guess_num < target:
        return GUESS_RESULTS["LOW"]
    elif guess_num > target:
        return GUESS_RESULTS["HIGH"]
    return GUESS_RESULTS["CORRECT"]