"""
main.py

Orchestrator for the advanced Morse Code Converter.
Instantiates logic and display; contains no business logic itself.
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from config import CMD_EXIT
from converter import MorseConverter
from display import Display


def main() -> None:
    converter = MorseConverter()
    display = Display()
    display.show_startup()

    try:
        while True:
            user_input = display.prompt_text()

            if user_input is None:              # up arrow → return to menu
                display.show_goodbye()
                break

            if user_input.lower() == CMD_EXIT:
                display.show_goodbye()
                break

            if not user_input:
                display.show_invalid()
                continue

            morse, unsupported = converter.convert(user_input)
            display.show_result(morse)

            if unsupported:
                display.show_warning(unsupported)
    except KeyboardInterrupt:
        display.show_goodbye()


if __name__ == "__main__":
    main()
