import json
import sys
import argparse

def convert_to_gron(data, base_object='json'):
    def traverse(obj, path):
        nonlocal output
        if isinstance(obj, dict):
            for key, value in obj.items():
                new_path = f"{path}.{key}"
                output += f"{new_path} = "
                if isinstance(value, dict):
                    output += "{{}}\n"
                    traverse(value, new_path)
                elif isinstance(value, list):
                    output += "[]\n"
                    for i, item in enumerate(value):
                        output += f"{new_path}[{i}] = "
                        if isinstance(item, dict):
                            output += "{}\n"
                            traverse(item, f"{new_path}[{i}]")
                        else:
                            output += json.dumps(item) + "\n"
                else:
                    output += json.dumps(value) + "\n"
        else:
            output += str(obj) + "\n"

    output = f"{base_object} = {{}}\n"
    traverse(data, base_object)
    return output

def main():
    parser = argparse.ArgumentParser(description='gron - JSON flattener')
    parser.add_argument('file', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
                        help='JSON file to process or use "-" for STDIN')
    parser.add_argument('--obj', type=str, default='json', help='Base object name (default: json)')
    args = parser.parse_args()

    try:
        json_content = json.load(args.file)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        sys.exit(1)

    flattened_json = convert_to_gron(json_content, args.obj)
    print(flattened_json)

if __name__ == "__main__":
    main()
