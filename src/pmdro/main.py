import click
import threading
import time

# from dataclasses import dataclass, field
# from typing import Optional
from pmdro.state import (
    TimerState,
    load_state,
    save_state,
    load_pid,
    save_pid,
    clear_pid,
    is_process_running,
)


@click.group()
def cli():
    pass


@cli.command("start")
@click.option(
    "-f",
    "--focus",
    "focus_duration",
    type=click.IntRange(1),
    help="Focus timer duration in minutes",
    default=25,
)
@click.option(
    "-b",
    "--break",
    "break_duration",
    type=click.IntRange(1),
    help="Break timer duration in minutes",
    default=5,
)
# @click.option("-s", "--split") # combines focus and break timer (syntax might look like 25/5)
def start(focus_duration, break_duration):
    # focus_seconds = focus_duration * 60

    state = load_state()
    print(f"Timer state class: {state}")

    state.running = not state.running
    print(f"Updated timer state class: {state}")

    save_state(state)

    clear_pid()
    pid = load_pid()
    print(f"Current PID: {pid}\nShould be 'None'.")

    save_pid(4)
    print("Look at '~/.config/pmdro/pmdro_pid' to see if value is 4.")

    pid = 98276
    pid_is_running = is_process_running(pid)
    print(f"\nProcess {pid} is running: {pid_is_running}")

    if focus_duration is not None:
        click.echo(f"Setting focus timer for {focus_duration} minutes.")

    # now = time.time()
    # print(f"Current time: {now}")
    # print(f"Data type of current time: {type(now)}")

    # with click.progressbar(range(focus_seconds)) as bar:
    #     for _ in bar:
    #         time.sleep(1)
    #
    if break_duration is not None:
        click.echo(f"Setting break timer for {break_duration} minutes.")
