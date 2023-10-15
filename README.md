# pypecamp

 <img src="https://github.com/bxbrenden/pypecamp/blob/main/images/solved_example.png" width=600px alt="Example rendered image of a solved Hexapipes puzzle">

A python-based image renderer for [Hexapipes](https://hexapipes.vercel.app/square/5) games.

## Limitations
This project currently renders PNG images of square Hexapipes grids only.
No other grids such as Penrose, cube, etc. will work with this tool.

## Installation
This tool requires python `3.11` and uses [pipenv](https://pipenv.pypa.io/en/latest/) to manage dependencies.
You can install `pipenv` via pip:
```bash
python3 -m pip install --upgrade pipenv
```

Use pipenv to install the dependencies by running this command from the top-level directory of this repo:
```bash
pipenv install
```

Next, use pipenv to create a virtual environment for running the script:
```
pipenv shell
```

## Usage
`pypecamp` renders images of Hexapipes puzzles based on JSON files downloaded from the Hexapipes website.
The picture below shows how to download the JSON version of a puzzle:
<img src="https://github.com/bxbrenden/pypecamp/blob/main/images/download-json.png" alt="Example image demonstrating the download of a Hexapipes JSON puzzle" width=600px>

For example, to render an image of a puzzle called `puzzle.json`:
```bash
python3 pypecamp.py puzzle.json
```

The output will be rendered to your screen
It is also saved to a PNG file with a long name like this:
```
1-12-1-13-4-8-11-13-7-4-11-6-11-12-8-10-8-10-11-14-2-3-6-2-2.png
```

The long name is simply a hyphen-separated list of the tiles' positions on the grid.
This naming scheme, though ugly, guarantees unique names for each output file.

## pypecamp??
Since the tool renders Hexapipes images, I wanted a unique name that had "pipe" in it somewhere.
I named this project after my favorite episode of a Tim and Eric show called _Tom Goes to the Mayor_-- [Pipe Camp](https://www.imdb.com/title/tt0726060/).
The "py" at the beginning is a nod to the tool being written in python.
