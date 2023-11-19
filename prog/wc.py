import sys

def word_count(file_path=None):
    if file_path:
        try:
            with open(file_path, 'r') as file:
                content = file.read()
        except FileNotFoundError:
            print(f"Error: {file_path} not found.")
            sys.exit(1)
    else:
        content = sys.stdin.read()

    lines = content.splitlines()
    words = content.split()
    characters = len(content)

    print(f"\t{len(lines)}\t{len(words)}\t{characters}\t{file_path or ''}")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        word_count(sys.argv[1])
    elif len(sys.argv) == 1:
        word_count()
    else:
        print("Usage: python wc.py [file_path]")
        sys.exit(1)