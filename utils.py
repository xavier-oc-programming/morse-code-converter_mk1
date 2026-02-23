"""
utils.py

Utility helper functions for text normalization and validation.
"""

def normalize_text(text: str) -> str:
    """
    Normalize user input by:
    - Stripping leading/trailing whitespace
    - Converting to uppercase
    """
    return text.strip().upper()


def find_unsupported_characters(text: str, valid_characters: set) -> set:
    """
    Return a set of characters that are not supported
    by the Morse dictionary (excluding spaces).
    """
    unsupported = set()

    for char in text:
        if char != " " and char not in valid_characters:
            unsupported.add(char)

    return unsupported