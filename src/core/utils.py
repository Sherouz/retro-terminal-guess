# utils.py - Helper functions

from typing import Callable
from src.core.constants import YES_TOKENS, NO_TOKENS

# Prompt user to play again. Return True if yes, False if no.
def ask_play_again(inputing: Callable[[str], str] = input,
                   printing: Callable[[str], None] = print
                   ) -> bool:
    """
    Prompts the user in a retro terminal style to decide if they want to continue playing.
    
    Continuously asks the user for input until a valid response is provided (Y/N),
    and displays appropriate system messages in retro terminal style.
    
    Args:
        inputing: Callable to read user input. Defaults to the built-in input function.
            Can be replaced with a GUI input function or automated test input.
        printing: Callable to display messages. Defaults to print.
            Can be replaced with a logging function or GUI display function.
    
    Returns:
        bool: True if the user wants to play again, False otherwise.
    """

    while True:
        response = inputing("\n[ SYSTEM QUERY ] >> Initiate another round? (Y/N): ").lower().strip()
        
        if response in YES_TOKENS:
            printing("\n[ SYSTEM RESPONSE ] >> Protocol: CONTINUE\n")
            return True
        elif response in NO_TOKENS:
            printing("\n[ SYSTEM RESPONSE ] >> Protocol: TERMINATE\n")
            return False
        else:
            printing("\n[ ERROR 0x03 ] >> Invalid input detected. Acceptable tokens: Y / N\n")
