"""
converter.py

Pure conversion logic — no print(), no input(), no UI imports.
"""

from config import MORSE_CODE_DICT, WORD_SEPARATOR


class MorseConverter:
    """Converts plain text to Morse code."""

    def __init__(self) -> None:
        self._codes: dict[str, str] = MORSE_CODE_DICT
        self._valid: set[str] = set(self._codes.keys())

    def convert(self, text: str) -> tuple[str, set[str]]:
        """
        Convert text to Morse code.

        Returns:
            tuple[str, set[str]]: (morse_string, unsupported_characters)
        """
        normalized = self._normalize(text)
        tokens: list[str] = []

        for char in normalized:
            if char == " ":
                tokens.append(WORD_SEPARATOR)
            elif char in self._codes:
                tokens.append(self._codes[char])

        morse = " ".join(tokens)
        unsupported = self._find_unsupported(normalized)
        return morse, unsupported

    def _normalize(self, text: str) -> str:
        """Strip whitespace and uppercase the input."""
        return text.strip().upper()

    def _find_unsupported(self, normalized: str) -> set[str]:
        """Return characters not in the Morse dictionary (spaces excluded)."""
        return {ch for ch in normalized if ch != " " and ch not in self._valid}
