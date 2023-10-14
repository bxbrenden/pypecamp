# pypecamp

 <img src="https://github.com/bxbrenden/pypecamp/blob/main/images/solved_example.png" width=600px alt="Example rendered image of a solved Hexapipes puzzle">

A python-based image renderer for [Hexapipes](https://hexapipes.vercel.app/square/5) games.

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
It is also saved to a file with a long name like this:
```
9,6,12,5,12,10,9,13,3,11,13,1,10,10,8,14,9,5,14,9,4,1,2,8,4.png
```

The long name is simply a comma-separated list of the tiles' positions on the grid.
This naming scheme, though ugly, guarantees unique names for each output file.
