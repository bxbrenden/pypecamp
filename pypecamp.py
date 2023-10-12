import json
import sys

from PIL import Image


def usage():
    """Tell the user how the script works and exit."""
    raise SystemExit("USAGE: python3 pypecamp.py <GAME_JSON>")


def read_game_json(js):
    """Read a Hexapipes exported game file (JSON), return game dict."""
    try:
        with open(js, "r") as game_file:
            tiles = json.loads(game_file.read().strip())
            return tiles
    except FileNotFoundError:
        raise SystemExit(f"File not found: {js}")
    except PermissionError:
        raise SystemExit(f"Permission denied for file {js}")
    except json.decoder.JSONDecodeError as jsde:
        raise SystemExit(f"Error decoding json for {js}:\n{jsde}")


def main():
    try:
        js = sys.argv[1]
    except IndexError:
        usage()

    game_def = read_game_json(js)
    print(game_def)


if __name__ == "__main__":
    main()
