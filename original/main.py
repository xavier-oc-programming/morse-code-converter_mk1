"""
main.py

Entry point for the Morse Code Converter CLI application.
"""

from converter import text_to_morse


def main():
    print("=== Morse Code Converter ===")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("Enter text to convert: ")

        if user_input.lower() == "exit":
            print("Goodbye.")
            break

        if not user_input.strip():
            print("Please enter some text.\n")
            continue

        morse_result, unsupported = text_to_morse(user_input)

        print("\nMorse Code:")
        print(morse_result)

        if unsupported:
            print("\nWarning: Unsupported characters ignored:", ", ".join(sorted(unsupported)))

        print()  # blank line for readability


if __name__ == "__main__":
    main()
