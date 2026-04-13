"""
config.py

All configuration constants for the advanced Morse Code Converter.
Zero magic numbers or magic strings anywhere else in the codebase.
"""

# ── Conversion ────────────────────────────────────────────────────────────────

WORD_SEPARATOR = "/"        # token inserted between words in Morse output

MORSE_CODE_DICT: dict[str, str] = {
    "A": ".-",   "B": "-...", "C": "-.-.", "D": "-..",
    "E": ".",    "F": "..-.", "G": "--.",  "H": "....",
    "I": "..",   "J": ".---", "K": "-.-",  "L": ".-..",
    "M": "--",   "N": "-.",   "O": "---",  "P": ".--.",
    "Q": "--.-", "R": ".-.",  "S": "...",  "T": "-",
    "U": "..-",  "V": "...-", "W": ".--",  "X": "-..-",
    "Y": "-.--", "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---",
    "3": "...--", "4": "....-", "5": ".....",
    "6": "-....", "7": "--...", "8": "---..",
    "9": "----.",
}

# ── Commands ──────────────────────────────────────────────────────────────────

CMD_EXIT = "exit"           # user types this to quit

# ── Display / formatting ──────────────────────────────────────────────────────

PROMPT = ">>"               # input prompt symbol
APP_TITLE = "Morse Code Converter"
