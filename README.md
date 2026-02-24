# Morse Code Converter

A modular Python CLI application that converts plain text into Morse code.

---

## Features

- Converts A–Z and 0–9 into Morse code
- Handles uppercase and lowercase automatically
- Separates words using "/"
- Warns about unsupported characters
- Clean modular structure

---

## Project Structure

```
morse-code-converter_mk1/
├── main.py            # CLI entry point (handles user interaction)
├── converter.py       # Core conversion logic (text → Morse)
├── morse_data.py      # Morse dictionary mapping (A–Z, 0–9)
├── utils.py           # Helper functions (normalization & validation)
├── requirements.txt   # Project dependencies
├── .gitignore         # Files ignored by Git
└── README.md          # Project documentation
```

---

## How to Run

From inside the `morse-code-converter_mk1` directory:

```bash
python main.py
```
