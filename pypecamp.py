import json
import math
import sys
from typing import List

from PIL import Image


def usage():
    """Tell the user how the script works and exit."""
    raise SystemExit("USAGE: python3 pypecamp.py <GAME_JSON>")


def read_game_json(js: str):
    """Read a Hexapipes exported game file (JSON), return game dict."""
    try:
        with open(js, "r") as game_file:
            tiles = json.loads(game_file.read().strip())
            return tiles['tiles']
    except FileNotFoundError:
        raise SystemExit(f"File not found: {js}")
    except PermissionError:
        raise SystemExit(f"Permission denied for file {js}")
    except json.decoder.JSONDecodeError as jsde:
        raise SystemExit(f"Error decoding json for {js}:\n{jsde}")


def open_image_files():
    """Open the .png images that represent different tiles, return as dict."""
    images = {}
    for number in range(0, 15):
        n = str(number + 1).zfill(2)
        png = f'images/{n}.png'
        try:
            img = Image.open(png)
            images[number + 1] = img
        except OSError:
            raise SystemExit(f'Failed to open image {png}')

    return images


def render_grid(tiles: List[int], images: dict):
    """Given a list of tile integers and open Images, return image of game."""
    # Check for square grid, fail on non-square grid
    try:
        sqrt = math.sqrt(len(tiles))
        assert int(sqrt) == sqrt
    except AssertionError:
        raise SystemExit('Grid was not square, exiting.')

    # Ensure every .png is the same width and height (all squares)
    try:
        for k in images.keys():
            assert images[k].size[0] == 500
            assert images[k].size[1] == 500
        # assert all([im[i].size[0] == 500 for i, im in enumerate(images)])
        # assert all([im.size[1] == 500 for im in images])
    except AssertionError:
        raise SystemExit('Err: Not all .png files are same width and height.')

    # Set the image width and height for rendered grid
    grid_width = int(images[1].size[0] * sqrt)
    grid_height = int(images[1].size[1] * sqrt)
    col_width = int(images[1].size[0])
    # col_height = images[0].size[1]
    grid = Image.new("RGB", (grid_width, grid_height))

    for i, tile in enumerate(tiles[:5]):
        grid.paste(images[tile], (i * col_width, 0))

    return grid


def main():
    try:
        js = sys.argv[1]
    except IndexError:
        usage()

    tiles = read_game_json(js)
    print(tiles)

    images = open_image_files()
    print(images)

    grid = render_grid(tiles, images)
    grid.show()


if __name__ == "__main__":
    main()
