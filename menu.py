"""
menu.py

Launcher for the Morse Code Converter.
Clears the console and shows the menu before each prompt.
Uses subprocess.run() + cwd= so sibling imports inside each build
resolve correctly without installed packages or relative imports.
"""

import os
import sys
import subprocess
from pathlib import Path

from art import LOGO

ROOT = Path(__file__).parent


def main() -> None:
    try:
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            print(LOGO)
            print("Select a build:")
            print("  1 → Original  (course submission)")
            print("  2 → Advanced  (OOP refactor)")
            print("  q → Quit\n")

            choice = input(">> ").strip().lower()

            if choice == "1":
                path = ROOT / "original" / "main.py"
                subprocess.run([sys.executable, str(path)], cwd=str(path.parent))
            elif choice == "2":
                path = ROOT / "advanced" / "main.py"
                subprocess.run([sys.executable, str(path)], cwd=str(path.parent))
            elif choice == "q":
                break
            else:
                print("Invalid choice. Try again.")
    except KeyboardInterrupt:
        print("\nGoodbye.")


if __name__ == "__main__":
    main()
