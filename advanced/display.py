"""
display.py

Owns ALL print() and input() calls.
No business logic lives here.
"""

import os
import sys

from config import APP_TITLE, CMD_EXIT, PROMPT


def _read_line(prompt: str) -> str | None:
    """
    Read a line of input character by character in raw terminal mode.

    Returns:
        str   — the typed text (stripped) on Enter
        None  — if the user pressed the up arrow key (signal to return to menu)

    Raises KeyboardInterrupt on Ctrl+C.
    """
    sys.stdout.write(prompt)
    sys.stdout.flush()

    if os.name == "nt":
        # ── Windows ───────────────────────────────────────────────────────────
        import msvcrt
        chars: list[str] = []
        while True:
            ch = msvcrt.getwch()
            if ch in ("\x00", "\xe0"):          # special-key prefix
                ch2 = msvcrt.getwch()
                if ch2 == "H":                  # up arrow
                    sys.stdout.write("\n")
                    return None
            elif ch in ("\r", "\n"):            # Enter
                sys.stdout.write("\n")
                return "".join(chars).strip()
            elif ch == "\x08":                  # backspace
                if chars:
                    chars.pop()
                    sys.stdout.write("\b \b")
                    sys.stdout.flush()
            elif ch == "\x03":                  # Ctrl+C
                raise KeyboardInterrupt
            else:
                chars.append(ch)
                sys.stdout.write(ch)
                sys.stdout.flush()

    else:
        # ── macOS / Linux ─────────────────────────────────────────────────────
        import tty
        import termios
        fd = sys.stdin.fileno()
        if not sys.stdin.isatty():
            # Not an interactive terminal (pipe / redirect) — plain fallback
            line = sys.stdin.readline()
            sys.stdout.write("\n")
            return line.strip() if line else None
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            chars: list[str] = []
            while True:
                ch = sys.stdin.read(1)
                if ch == "\x1b":                # escape sequence
                    ch2 = sys.stdin.read(1)
                    if ch2 == "[":
                        ch3 = sys.stdin.read(1)
                        if ch3 == "A":          # up arrow
                            sys.stdout.write("\r\n")
                            sys.stdout.flush()
                            return None
                        # other arrow keys — ignore
                elif ch in ("\r", "\n"):        # Enter
                    sys.stdout.write("\r\n")
                    sys.stdout.flush()
                    return "".join(chars).strip()
                elif ch in ("\x7f", "\x08"):    # backspace / delete
                    if chars:
                        chars.pop()
                        sys.stdout.write("\b \b")
                        sys.stdout.flush()
                elif ch == "\x03":              # Ctrl+C
                    sys.stdout.write("\r\n")
                    sys.stdout.flush()
                    raise KeyboardInterrupt
                elif ch >= " ":                 # printable character
                    chars.append(ch)
                    sys.stdout.write(ch)
                    sys.stdout.flush()
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)


class Display:
    """Handles all terminal rendering and user interaction."""

    def show_startup(self) -> None:
        """Print the startup banner and command reference."""
        print(f"{APP_TITLE} ready.")
        print(f"  Enter any text at the prompt to convert it to Morse code.")
        print(f"  Press ↑ (up arrow) or type '{CMD_EXIT}' to return to menu.\n")

    def prompt_text(self) -> str | None:
        """
        Prompt the user for text to convert.

        Returns None if the user pressed the up arrow key.
        """
        return _read_line(f"{PROMPT} ")

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
