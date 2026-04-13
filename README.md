# Morse Code Converter

A modular Python CLI that converts plain text (A–Z, 0–9) into Morse code.
Two builds: the original course submission and an OOP-refactored advanced version.

---

## 1. Quick Start

```bash
# From the repo root — shows the menu, pick a build, menu reappears on exit
python menu.py

# Or run a build directly
python original/main.py
python advanced/main.py
```

---

## 2. Builds Comparison

| Feature | Original | Advanced |
|---|---|---|
| Converts A–Z and 0–9 | ✓ | ✓ |
| Case-insensitive input | ✓ | ✓ |
| Word separator (`/`) | ✓ | ✓ |
| Unsupported-character warning | ✓ | ✓ |
| Startup command reference banner | — | ✓ |
| OOP design (`MorseConverter`, `Display`) | — | ✓ |
| Centralized config (zero magic strings) | — | ✓ |
| Type hints throughout | Partial | Full (Python 3.10+) |
| All I/O isolated to one class | — | ✓ |
| Launched from `menu.py` | ✓ | ✓ |

---

## 3. Commands

Both builds share the same prompt interface.

| Input | Result |
|---|---|
| Any text (letters, digits, spaces) | Prints the Morse code translation |
| `exit` | Prints "Goodbye." and quits |
| Empty / whitespace only | Prints "Please enter some text." |
| Text with unsupported chars | Converts supported chars, warns about the rest |

**Startup banner (advanced build):**

```
Morse Code Converter ready.
  Enter any text at the prompt to convert it to Morse code.
  Type 'exit' to quit.
```

---

## 4. App Flow

Step-by-step description of what happens during a session:

1. Run `menu.py` (or a build directly).
2. The advanced build prints the startup banner with command reference.
3. The `>>` prompt appears.
4. User types text and presses Enter.
   - Empty input → "Please enter some text." → prompt again.
   - `exit` → "Goodbye." → program ends.
   - Any other input → normalized (stripped + uppercased) → converted.
5. Morse output is printed, one line indented.
6. If any characters were skipped (e.g. `!`, `?`, `@`), a warning lists them.
7. The prompt reappears automatically. Repeat from step 4.

---

## 5. Features

**Both builds**

**Text-to-Morse conversion.** Accepts any mix of A–Z (upper or lower case) and 0–9.
Each character is mapped to its ITU Morse equivalent and the tokens are joined with spaces.

**Word separation.** A space in the input becomes a `/` in the output, matching the
standard Morse word-separator convention.

**Unsupported-character handling.** Characters outside A–Z and 0–9 are silently skipped
during conversion and then listed together in a warning message so the user knows exactly
what was ignored.

**Case normalization.** Input is uppercased before lookup, so `hello` and `HELLO` produce
identical output.

---

**Advanced build only**

**Startup command reference.** On launch the app prints a one-time banner listing every
valid input so the user never has to guess what to type.

**OOP design.** Logic lives in `MorseConverter`; all I/O lives in `Display`. The two classes
have no knowledge of each other — `main.py` wires them together.

**Centralized config.** Every constant (Morse dictionary, word separator, exit command,
prompt symbol, app title) is defined once in `config.py`. No string or value is repeated
anywhere else in the codebase.

**Full type hints.** All function and method signatures carry Python 3.10+ type annotations
(`X | Y` unions, `tuple[str, set[str]]` generics) for clarity and static-analysis support.

---

## 6. Navigation Flow

### Terminal menu tree

```
python menu.py
│
├── 1 ──→ subprocess: original/main.py   (blocks until user types 'exit')
│         └── returns to menu.py loop
│
├── 2 ──→ subprocess: advanced/main.py   (blocks until user types 'exit')
│         └── returns to menu.py loop
│
└── q ──→ breaks the while loop → menu.py exits
```

### In-app flow (both builds)

```
┌──────────────────────┐
│  (startup banner)    │  ← advanced only
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│    >> prompt         │ ◄──────────────────────────────────────────┐
└──────────┬───────────┘                                            │
           │                                                        │
           ├─ empty / whitespace ──→ "Please enter some text."  ───┘
           │
           ├─ "exit"  ────────────→ "Goodbye."  ──→  program ends
           │
           └─ any text ──→ normalize ──→ convert
                                │
                                ├──→ print Morse result  ──────────┐
                                │                                  │
                                └──→ unsupported chars?            │
                                        yes → print warning  ──────┤
                                        no  ──────────────────────→┘
                                                                   │
                                                       back to >> prompt
```

---

## 7. Architecture

```
morse-code-converter_mk1/
│
├── menu.py              # Launcher: clears screen, shows menu, runs builds via subprocess
├── art.py               # LOGO constant — ASCII art printed by menu.py
├── requirements.txt     # No pip deps — stdlib only, Python 3.10+
├── .gitignore
├── README.md
│
├── docs/
│   └── COURSE_NOTES.md  # Original assignment brief from the course
│
├── original/            # Course submission — verbatim, no logic changes
│   ├── main.py          # Entry point + main loop (print/input here)
│   ├── converter.py     # text_to_morse() function
│   ├── morse_data.py    # MORSE_CODE_DICT data
│   └── utils.py         # normalize_text(), find_unsupported_characters()
│
└── advanced/            # OOP refactor
    ├── main.py          # Orchestrator — wires MorseConverter + Display, no logic
    ├── config.py        # All constants — MORSE_CODE_DICT, WORD_SEPARATOR, CMD_EXIT, …
    ├── converter.py     # class MorseConverter — pure logic, no I/O
    └── display.py       # class Display — all print() and input() calls
```

---

## 8. Module Reference

### `original/converter.py`

| Function | Returns | Description |
|---|---|---|
| `text_to_morse(text)` | `tuple[str, set]` | Normalizes input and converts to Morse; returns (morse_string, unsupported_set) |

### `original/utils.py`

| Function | Returns | Description |
|---|---|---|
| `normalize_text(text)` | `str` | Strips whitespace and uppercases the string |
| `find_unsupported_characters(text, valid_characters)` | `set` | Returns chars in text that are not in valid_characters (spaces excluded) |

### `advanced/converter.py` — `class MorseConverter`

| Method | Returns | Description |
|---|---|---|
| `__init__()` | `None` | Loads `MORSE_CODE_DICT` from config; builds valid-character set |
| `convert(text)` | `tuple[str, set[str]]` | Public entry point: normalizes, converts, returns (morse, unsupported) |
| `_normalize(text)` | `str` | Strips and uppercases input (private) |
| `_find_unsupported(normalized)` | `set[str]` | Returns chars not in the Morse dict, excluding spaces (private) |

### `advanced/display.py` — `class Display`

| Method | Returns | Description |
|---|---|---|
| `show_startup()` | `None` | Prints app title and one-line command reference |
| `prompt_text()` | `str` | Displays `>>` prompt and returns stripped user input |
| `show_result(morse)` | `None` | Prints the Morse code translation |
| `show_warning(chars)` | `None` | Lists unsupported characters that were ignored |
| `show_invalid()` | `None` | Tells user to enter non-empty text |
| `show_goodbye()` | `None` | Prints farewell message before exit |

---

## 9. Configuration Reference

All constants live in `advanced/config.py`.

| Constant | Default | Description |
|---|---|---|
| `WORD_SEPARATOR` | `"/"` | Token inserted between Morse words |
| `MORSE_CODE_DICT` | `{A: .-, B: -..., …}` | Full A–Z, 0–9 Morse mapping (36 entries) |
| `CMD_EXIT` | `"exit"` | Input string that ends the session |
| `PROMPT` | `">>"` | Symbol shown before every user input line |
| `APP_TITLE` | `"Morse Code Converter"` | Displayed in the startup banner |

---

## 10. Session Flow Diagram

Full prompt → outcome flow for a single session (advanced build):

```
 python advanced/main.py
         │
         ▼
 ┌───────────────────────────────────┐
 │  Morse Code Converter ready.      │
 │    Enter any text…                │
 │    Type 'exit' to quit.           │
 └───────────────────────────────────┘
         │
         ▼
 >> hello world
         │
         ▼
 ┌───────────────────────────────────┐
 │  Morse Code:                      │
 │    .... . .-.. .-.. --- / .-- --- │
 │    .-. .-.. -..                   │
 └───────────────────────────────────┘
         │
         ▼
 >> hi! there
         │
         ▼
 ┌───────────────────────────────────┐
 │  Morse Code:                      │
 │    .... .. / - .... . .-. .       │
 │                                   │
 │  Warning: unsupported characters  │
 │  ignored: !                       │
 └───────────────────────────────────┘
         │
         ▼
 >>
         │
         ▼
 Please enter some text.
         │
         ▼
 >> exit
         │
         ▼
 Goodbye.
```

---

## 11. Design Decisions

**`display.py` owns all I/O.**
Isolating every `print()` and `input()` call to one class means the logic modules
(`converter.py`) are trivially testable — pass in text, inspect the return value, done.
Swapping the CLI for a GUI later requires touching only `display.py`.

**`config.py` — zero magic numbers.**
Every constant (the `"/"` separator, the `"exit"` command, the `">>"` prompt) is defined
once. A future change — say, swapping `"/"` for `" | "` — is a one-line edit with no risk
of missing an occurrence buried in a print statement.

**`sys.path.insert` at the top of `advanced/main.py`.**
This ensures sibling imports (`from config import …`, `from converter import …`) resolve
correctly whether the script is launched by `menu.py` (which sets `cwd=advanced/`) or run
directly from the repo root with `python advanced/main.py`. No installed packages or
relative-import syntax needed.

**`subprocess.run()` + `cwd=` in `menu.py`.**
Passing `cwd=str(path.parent)` makes the subprocess's working directory match the build
folder. Inside `original/`, `from converter import …` resolves against `original/converter.py`
— not the root — without any path manipulation inside those files.

**`while True` in `menu.py` (not recursion).**
The menu reappears after a subprocess exits by looping back to the top of the `while True`.
A recursive call would grow the call stack with every build launch; the loop has constant
stack depth regardless of how many times the user switches builds.

**Console cleared before every menu render.**
`os.system("cls" if os.name == "nt" else "clear")` runs at the top of each loop iteration.
The user always sees a clean menu screen — no visual noise from the previous build's output.

**`MorseConverter._normalize` and `_find_unsupported` are private.**
The only public surface is `convert()`. Internal helpers are prefixed with `_` so callers
(i.e. `main.py`) are not tempted to bypass the intended interface.

---

## 12. Course Context

Built as **Day 82** of *100 Days of Code: The Complete Python Pro Bootcamp* by Dr. Angela Yu.

**Concepts covered in the original build:**
- Dictionary creation and lookup
- String normalization (`.strip()`, `.upper()`)
- `for` loops over strings
- List accumulation and `" ".join()`
- Separating data (`morse_data.py`), logic (`converter.py`), and utilities (`utils.py`)
- Conditional handling of edge cases (spaces, unsupported characters)

**The advanced build extends into:**
- Object-oriented programming — classes, instance attributes, public/private methods
- Separation of concerns — logic vs I/O via dedicated `Display` class
- Centralized configuration — `config.py` as single source of truth
- Type hints (Python 3.10+ syntax: `tuple[str, set[str]]`, `dict[str, str]`)
- Subprocess orchestration and working-directory management

See [docs/COURSE_NOTES.md](docs/COURSE_NOTES.md) for the full original assignment brief.

---

## 13. Dependencies

| Module | Used in | Purpose |
|---|---|---|
| `os` | `menu.py` | `os.system()` to clear the console |
| `sys` | `menu.py`, `advanced/main.py` | `sys.executable` for subprocess; `sys.path.insert` for imports |
| `subprocess` | `menu.py` | Launches each build as a child process |
| `pathlib.Path` | `menu.py`, `advanced/main.py` | Resolve file paths relative to each script's location |
