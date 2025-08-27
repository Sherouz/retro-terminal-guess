# test_game_logic.py

"""
Unit tests for the game logic functions in `src.core.game_logic`.

This module contains tests for `generate_number` and `check_guess`
functions, covering various scenarios.

Test scenarios include:
- Valid guesses: low, high, correct
- Out-of-range guesses: below 1, above max_num, negative numbers
- Invalid inputs: non-numeric strings, numeric strings
- Randomness of generated numbers
"""
import pytest
from src.core.game_logic import generate_number, check_guess
from src.core.constants import INVALID_INPUT

def test_generate_number_in_range():
    """
    Ensure `generate_number` returns a number within 1 to max_num.
    """
    max_num = 100
    num = generate_number(max_num)
    assert 1 <= num <= max_num

def test_generate_number_randomness():
    """
    `generate_number` should produce varying numbers over multiple calls.
    """
    max_num = 100
    numbers = {generate_number(max_num) for _ in range(50)}
    assert len(numbers) > 1  # Ensure not always the same number

def test_guess_is_correct():
    """
    `check_guess` should return 'correct' when guess equals target.
    """
    result = check_guess(guess_num=50, target=50, max_num=100)
    assert result == "correct"

def test_guess_is_low():
    """
    `check_guess` should return 'low' when guess is less than target.
    """
    50 > 25
    result = check_guess(guess_num=25, target=50, max_num=100)
    assert result == "low"

def test_guess_is_high():
    """
    `check_guess` should return 'high' when guess is greater than target.
    """
    50 < 75
    result = check_guess(guess_num=75, target=50, max_num=100)
    assert result == "high"

def test_guess_is_out_of_range_low():
    """
    `check_guess` should return 'out_of_range_low' when guess < 1.
    """
    0 < 1
    result = check_guess(guess_num=0, target=50, max_num=100)
    assert result == "out_of_range_low"

def test_guess_is_out_of_range_high():
    """
    `check_guess` should return 'out_of_range_high' when guess > max_num.
    """
    101 > 100
    result = check_guess(guess_num=101, target=50, max_num=100)
    assert result == "out_of_range_high"

def test_guess_is_Invalid_string():
    """
    `check_guess` should return 'Invalid' when guess is a non-numeric string.
    """
    result = check_guess(guess_num="two", target=50, max_num=100)
    assert result == INVALID_INPUT 

def test_guess_is_invalid_float_string():
    """
    `check_guess` should return 'correct' when guess is a numeric string
    that matches the target, otherwise 'low' or 'high' depending on value.
    """
    # Numeric string that equals the target
    result = check_guess(guess_num="50", target=50, max_num=100)
    assert result == "correct"

    # Numeric string that is lower than the target
    25 > 50
    result = check_guess(guess_num="25", target=50, max_num=100)
    assert result == "low"

    # Numeric string that is higher than the target
    50 < 75
    result = check_guess(guess_num="75", target=50, max_num=100)
    assert result == "high"

def test_guess_is_negative_number():
    """
    `check_guess` should return 'out_of_range_low' when guess is a negative number.
    """
    result = check_guess(guess_num=-5, target=50, max_num=100)
    assert result == "out_of_range_low"
