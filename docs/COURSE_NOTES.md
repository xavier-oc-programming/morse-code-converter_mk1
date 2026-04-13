# Assignment 1: Text to Morse Code Converter

## Project Overview

Build a **text-based Python program** that converts strings into Morse Code.

This is the first independent portfolio project in this section. The goal is not just to write
working code, but to design and implement a complete solution without step-by-step guidance.

---

## Objective

Create a Python program that:

- Accepts user input (a string of text)
- Converts each character into its Morse Code equivalent
- Outputs the translated Morse Code result

The program should operate entirely in the terminal (text-based).

---

## Core Requirements

### Input Handling

- Accept a string from the user.
- Handle uppercase and lowercase characters consistently.
- Consider how to handle spaces between words.

### Morse Code Mapping

- Create a dictionary that maps:
  - Letters (A–Z)
  - Numbers (0–9)
  - Optional punctuation
- Each key should correspond to its Morse Code representation.

Example structure:

- `"A"` → `".-"`
- `"B"` → `"-..."`
- `"1"` → `".----"`

---

## Expected Program Flow

### Step 1: Define the Morse Dictionary

Create a dictionary containing all required mappings.

### Step 2: Get User Input

Use `input()` to collect a string.

### Step 3: Normalize the Input

- Convert to uppercase.
- Optionally strip leading/trailing whitespace.

### Step 4: Convert Text to Morse

Loop through each character:

- If the character exists in the dictionary → append the Morse equivalent to a result list.
- If the character is a space → insert a separator (e.g. `/` or triple space).
- If unsupported → decide whether to ignore or handle gracefully.

### Step 5: Output the Result

Join the Morse elements with spaces and print the final translation.

---

## Learning Goals

This assignment reinforces:

- Dictionary usage
- Loops
- String manipulation
- Conditional logic
- Program structure design
- Independent problem-solving

More importantly, it begins training you to:

- Translate a written specification into working software
- Make design decisions independently
- Handle edge cases thoughtfully

---

## Portfolio Mindset

This is not just an exercise.

It is:

- A GitHub-worthy project
- A demonstration of problem-solving ability
- The beginning of independent project development

The goal is not perfection. The goal is ownership.
