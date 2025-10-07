# PMDRO - CLI Pomodoro Timer

A simple pomodoro timer command line application written in Python. Intended for MacOS.

## Features

- Run full pomodoro sessions with focus and break timers
- Run focus timer only
- Run break timer only
- Customize timer durations
- Auto-start break timer (skip confirmation prompt)

## Installation

### Prerequisites

- Python 3.10 or higher
- [uv](https://github.com/astral-sh/uv)

### 1. Download repo

```
git clone https://github.com/sbrown3212/pmdro-py
cd pmdro-py
```

### 2a. Try it out (without installation)

To run pmdro without installing:

```
uv run pmdro start
```

Be sure to include `uv run` before all pmdro commands when it is not installed. `uv` will manage activating the virtual environment for you.

### 2b. Install it locally to use in a virtual environment (optional)

To install pmdro to be used within the project's virtual environment (and not need to include `uv run` before commands):

```
uv pip install --editable
```

Then activate the virtual environment:

```
source .venv/bin/activate
```

### 2c. Install it locally to use globally (optional)

To install pmdro on your own machine to be able run it from any directory:

```
uv tool install --editable
```

## Usage

When running a command without a local installation, it is necessary to add `uv run` before each of the following commands. Also, when using the `--focus` or `--break` options, it needs to be followed by an argument that needs to be an `int` greater than zero.

### Full Session (Focus + Break)

Run a complete session with both a focus and a break timer:

```
pmdro start
```

Customize the duration of each timer by including the focus and break options, each followed by their own duration in minutes:

```
pmdro start --focus 50 --break 10
```

By default, you'll be prompted to confirm before starting the break timer. To auto-start the break:

```
pomodoro start --focus 30 --break 15 --auto-start
```

### Focus Timer Only

Run only the focus timer:

```
pmdro start --focus 25
```

### Break Timer Only

Run only a break timer:

```
pmdro start --break 5
```

### Help

```
pmdro start --help
```

### Examples

```
# Standard session with 25 min focus timer and 5 min break timer with auto-start
pmdro start --auto-start
# or
pmdro start -a

# Quick 15 min focus session
pmdro start --focus 15
# or
pmdro start -f 15

# 3 minute break timer
pmdro start -b 3
# or
pmdro start -b 3

# Auto-start session with 50 min focus timer and 10 min break timer
pmdro start --focus 50 --break 10 --auto-start
# or
pmdro start -f 50 -b 10 -a
```

## Development

### Setup Development Environment

Clone the repo:

```
git clone https://github.com/sbrown3212/pmdro-py
cd pmdro-py
```

Create virtual environment and install dependencies:

```
uv sync
```

Install in editable mode (optional):

```
uv pip install -e
```

<!-- ### Running Tests -->

## Contributing

This is a personal project for [Boot.dev](https://boot.dev) (an awesome backend development course), but suggestions and feedback are welcome. Feel free to open an issue if you find a bug or have ideas for improvement.

## License

[MIT License](LICENSE) - feel free to use this project for learning purposes.

## Acknowledgments

- Built with [`click`](https://click.palletsprojects.com/en/stable/) for CLI the interface
- Project management with [`uv`](https://github.com/astral-sh/uv)
- Inspired by BashBunni's script. Check out her video [here](https://www.youtube.com/watch?v=GfQjJBtO-8Y). Check out the code [here](https://gist.github.com/bashbunni/f6b04fc4703903a71ce9f70c58345106).

<!-- ## Future improvements -->
<!---->
<!-- - [ ] Implement MacOS notifications -->
<!-- - [ ] Implement testing -->
<!-- - [ ] Version with threads (to allow for commands while timer is running) -->
<!-- - [ ] Implement `pause`, `resume`, and `stop` commands (requires threads) -->
<!-- - [ ] Version with processes (for persistent timer to run in the background) -->
<!-- - [ ] User config -->
