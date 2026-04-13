"""
converter.py

Core business logic for converting text into Morse code.
"""

from morse_data import MORSE_CODE_DICT
from utils import normalize_text, find_unsupported_characters


def text_to_morse(text: str) -> tuple[str, set]:
    """
    Convert plain text into Morse code.

    Parameters:
        text (str): The input string from the user.

    Returns:
        tuple[str, set]:
            - Morse code translation (str)
            - Set of unsupported characters (set)
    """

    normalized = normalize_text(text)

    morse_output = []
    valid_characters = set(MORSE_CODE_DICT.keys())

    for char in normalized:
        if char == " ":
            # Use "/" to separate words
            morse_output.append("/")
        elif char in MORSE_CODE_DICT:
            morse_output.append(MORSE_CODE_DICT[char])
        else:
            # Unsupported characters are handled separately
            continue

    unsupported = find_unsupported_characters(normalized, valid_characters)

    return " ".join(morse_output), unsupported
