import sys
import argparse

def word_count(file_paths=None, lines_flag=False, words_flag=False, characters_flag=False):
    total_lines = 0
    total_words = 0
    total_characters = 0

    for file_path in file_paths:
        try:
            with open(file_path, 'r') as file:
                content = file.read()
        except FileNotFoundError:
            print(f"Error: {file_path} not found.")
            sys.exit(1)

        lines = content.splitlines()
        words = content.split()
        characters = len(content)

        total_lines += len(lines)
        total_words += len(words)
        total_characters += characters

        if lines_flag:
            print(f"{len(lines):8}", end="")
        if words_flag:
            print(f"{len(words):8}", end="")
        if characters_flag:
            print(f"{characters:8}", end="")
        
        print(f" {file_path}")

    if len(file_paths) > 1:
        if lines_flag:
            print(f"{total_lines:8}", end="")
        if words_flag:
            print(f"{total_words:8}", end="")
        if characters_flag:
            print(f"{total_characters:8}", end="")
        
        print(" total")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Word count utility with extensions.')
    parser.add_argument('file_paths', nargs='*', help='List of file paths to count words.')
    parser.add_argument('-l', '--lines', action='store_true', help='Count only lines.')
    parser.add_argument('-w', '--words', action='store_true', help='Count only words.')
    parser.add_argument('-c', '--characters', action='store_true', help='Count only characters.')

    args = parser.parse_args()

    if not args.file_paths:
        content = sys.stdin.read()
        lines = content.splitlines()
        words = content.split()
        characters = len(content)

        if args.lines:
            print(f"{len(lines):8}", end="")
        if args.words:
            print(f"{len(words):8}", end="")
        if args.characters:
            print(f"{characters:8}", end="")
        
        print("")

    else:
        word_count(args.file_paths, args.lines, args.words, args.characters)
