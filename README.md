# PMDRO - CLI Pomodoro Timer

A simple pomodoro timer command line application written in Python.

## Features

- Run full pomodoro sessions with focus and break timers
- Run focus timer only
- Run break timer only
- Customize timer durations
- Auto-start break timer (skip confirmation prompt)

## Installation

### Prerequisites

- Python 3.8 or higher
- [uv](https://github.com/astral-sh/uv)

### 1. Download repo

```
git clone https://github.com/sbrown3212/pmdro-py
cd pmdro-py
```

### 2a. Try it out (without installation)

```
uv run pmdro start
```

### 2b. Install it locally (optional)

```
uv pip install -e
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

<!-- ## Development -->
<!---->
<!-- ### Setup Development Environment -->
<!---->
<!-- Clone the repo: -->
<!---->
<!-- ``` -->
<!-- git clone https://github.com/sbrown3212/pmdro-py -->
<!-- cd pmdro-py -->
<!-- ``` -->
<!---->
<!-- Create virtual environment and install dependencies: -->
<!---->
<!-- ``` -->
<!-- uv sync -->
<!-- ``` -->
<!---->
<!-- Install in editable mode (optional): -->
<!---->
<!-- ``` -->
<!-- uv pip install -e -->
<!-- ``` -->
<!---->
<!-- ### Running Tests -->
```
```

## Contributing

This is a personal project for a backend development course, but suggestions and feedback are welcome. Feel free to open an issue if you find a bug or have ideas for improvement.

<!-- ## License -->

## Acknowledgments

- Built with [`click`](https://click.palletsprojects.com/en/stable/) for CLI the interface
- Project management with [`uv`](https://github.com/astral-sh/uv)
- Inspired by BashBunni's script. Check out her video [here](https://www.youtube.com/watch?v=GfQjJBtO-8Y). Check out the code [here](https://gist.github.com/bashbunni/f6b04fc4703903a71ce9f70c58345106).

<!-- --- -->
<!---->
<!-- ### Start a timer -->
<!---->
<!-- #### To run the default timer -->
<!---->
<!-- ``` -->
<!-- pmdro start -->
<!-- ``` -->
<!---->
<!-- This will run a session with a focus timer of 25 minutes and a focus timer of 5 minutes. Once the focus timer is completed, the user will be prompted to confirm to start the break timer. -->
<!---->
<!-- #### To specify timer type and duration -->
<!---->
<!-- ``` -->
<!-- pmdro start --focus 50 --break 10 -->
<!-- ``` -->
<!---->
<!-- To specify the duration of each timer, include the option for the desired timer (`--focus` or `-f`, `--break` or `-b`) followed by the integer of the desired timer duration in minutes. Include both options (followed by their respective arguments) to include both timers in the session. To only include one of the timers in a session, only provide the respective option and argument. -->
<!---->
<!-- #### Auto start break timer -->
<!---->
<!-- By default, when a session includes both a focus and a default timer, the user will be prompted with a confirmation to start the break timer. To automatically begin the break timer without confirmation once the focus timer begins, include `-a` or `--auto-break` in the command. For example: -->
<!---->
<!-- ``` -->
<!-- pmdro start -a -->
<!---->
<!-- # or -->
<!---->
<!-- pmdro start -f 50 -b 10 --auto-break -->
<!-- ``` -->
<!---->
<!-- ## Difficulties/Learning experiences -->
<!---->
<!-- I ran into a quite a few road blocks with this project. -->
<!---->
<!-- ### Processes -->
<!---->
<!-- At first I wanted to have a timer that ran in the background, with the ability to check the status with a command, and upon the timer completing, a system and or terminal notification would be triggered. This would allow the terminal to continue to be used (or closed) without interrupting the timer. But this required state to be stored somehow, and so I began to try implement to implement a way to save state to a file. -->
<!---->
<!-- Then I realized that I would need to figure out how to manage processes, since all of this would be running in the background. I had never done anything like this before, and quickly became something bigger than would take in the amount of time that I was intended to spend for the Boot.dev personal project. -->
<!---->
<!-- ### Threads -->
<!---->
<!-- When trying to set more realistic expectations for this project, I decided to put application persistence on hold. Instead, I focused on setting up logic to be able to use other commands like `pause`, `resume`, and `stop`. This is where I quickly found my next road block. I tried to go about storing timer state in a class, but quickly found out that there would not be a way to have the different `click` commands use the same timer class instance. Which meant that I would need to implement a state file system like I had tried to do when using processes for persistence. -->
<!---->
<!-- ### Over-engineering/Scope creep -->
<!---->
<!-- By this point, I had already passed the amount of time recommended to spend on the project from the Boot.dev requirements. And, I still didn't have anything close to a working timer. Everything I had worked on so far was related to storing state (and even user config stuff to be able to set default timer length, etc.). So I decided to pivot and just see if I could get a basic `while` loop timer to run the way I liked. I eventually got there, but it was actually a lot more difficult than I was expecting. -->
<!---->
<!-- ### The wrong tool for the job -->
<!---->
<!-- It turns out, the `progresbar` utility from `click` is more intended for things that are to be iterated over, rather and a timer with continuous updates. I eventually made something that works, but it isn't ideal and has a lot of room for improvement. -->
<!---->
<!-- ### You don't know what you don't know -->
<!---->
<!-- There were a lot of things that I just wasn't familiar with. My understanding of when and how to use processes and threads is lacking. So, knowing when certain features would require the use of a background process or its own thread is a concept I am still trying to wrap my mind around. In future versions, I would like to explore using threads and processes, but for now, it was out of the scope of this project. -->
<!---->
<!-- Because I never got around to implementing threads or processes, I couldn't find a way to get other commands to work. So, unfortunately, there is no way to pause and resume the timer (for now). -->
<!---->
<!-- Another thing that caused me a lot of trouble was the `option`s for `click` commands. I was trying to use an option for the focus timer duration, and another for the break timer duration. I tried to implement a way to use the default duration for the respective timer while still allowing a way to either use the default duration or specify a custom duration. To do this, I tried to implement the following using `click` `option`s: -->
<!---->
<!-- - `-f` would only run a focus timer of the default focus timer duration. -->
<!-- - `-f 50` would only run a focus timer for the duration (in minutes) specified by the user. -->
<!-- - `-b` would only run a break timer of the default break timer duration. -->
<!-- - `-b 10` would only run a break timer for the duration specified by the user. -->
<!-- - `-f -b` would run both a focus and a break timer of their respective default durations. -->
<!-- - `-f 50 -b 10` would run both a focus and a break timer with a duration specified by the user. -->
<!---->
<!-- I was unable to figure out how to do this because in order to have the `option` behave as a flag (by setting `is_flag=True`), it no longer accepted an argument. And when setting `is_flag=False`, it expected an argument and would throw an error if there wasn't one. Because my exposure to CLI tools is currently lacking, I am not sure if this type of behaviour is frowned upon, or if this type of functionality just isn't built into `click`. Or maybe I just need to dive deeper into the docs. -->
<!---->
<!-- And finally, I wanted to implement system notifications, but without installing any other external dependencies. Because I use MacOS, this is what I prioritized. I tried doing this using `os.system` and `subprocess.run` that would run a `osascript` to display a notification, but I could never get it to work. For what its worth, I tried running the same `osascript` command on a friend's MacBook and it worked as expected. I spent hours searching through the options in the notifications settings to find what was wrong, but I was unsuccessful at finding the cause of the problem. So, I decided not to include system notifications in the current version as I would not be able to test it. -->

## Future improvements

- [ ] Implement MacOS notifications
- [ ] Implement testing
- [ ] Version with threads (to allow for commands while timer is running)
- [ ] Implement `pause`, `resume`, and `stop` commands (requires threads)
- [ ] Version with processes (for persistent timer to run in the background)
- [ ] User config
