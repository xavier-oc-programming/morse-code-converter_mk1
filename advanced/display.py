"""
display.py

Owns ALL print() and input() calls.
No business logic lives here.
"""

from config import APP_TITLE, CMD_EXIT, PROMPT


class Display:
    """Handles all terminal rendering and user interaction."""

    def show_startup(self) -> None:
        """Print the startup banner and command reference."""
        print(f"{APP_TITLE} ready.")
        print(f"  Enter any text at the prompt to convert it to Morse code.")
        print(f"  Type '{CMD_EXIT}' to quit.\n")

    def prompt_text(self) -> str:
        """Prompt the user for text to convert."""
        return input(f"{PROMPT} ").strip()

    def show_result(self, morse: str) -> None:
        """Display the Morse code result."""
        print(f"\nMorse Code:\n  {morse}\n")

    def show_warning(self, chars: set[str]) -> None:
        """Warn about unsupported characters that were ignored."""
        sorted_chars = ", ".join(sorted(chars))
        print(f"Warning: unsupported characters ignored: {sorted_chars}\n")

    def show_invalid(self) -> None:
        """Prompt user to enter actual text."""
        print("Please enter some text.\n")

    def show_goodbye(self) -> None:
        """Print exit message."""
        print("Goodbye.")
