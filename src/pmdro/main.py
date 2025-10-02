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


FOCUS_DEFAULT_DURATION = 25
BREAK_DEFAULT_DURATION = 5


@click.group()
def cli():
    pass


@cli.command("start")
@click.option(
    "-f",
    "--focus",
    "focus_duration",
    type=click.IntRange(1),
    help="Include focus timer. Requires integer argument to specify timer duration (in minutes).",
    default=None,
    is_flag=False,
    # flag_value=25,
)
@click.option(
    "-b",
    "--break",
    "break_duration",
    type=click.IntRange(1),
    help="Include break timer. Requires integer argument to specify timer duration (in minutes).",
    default=None,
    is_flag=False,
    # flag_value=5,
)
@click.option(
    "-a",
    "--auto-break",
    "auto_break",
    type=bool,
    default=False,
    help="Auto start break timer once focus timer is completed.",
    is_flag=True,
)
# @click.option("-s", "--split") # combines focus and break timer (syntax might look like 25/5)
def start(focus_duration, break_duration, auto_break):
    """
    Start new timer session

    By default, runs a 25 minute focus timer and a 5 minute break timer.
    Use -f and -b flags to customize the session.
    """

    # 'pmdro start' should run a session with a 25 min focus timer and a 5 min break timer.
    # 'pmdro start -f 45' should run a session with only a 45 min focus timer.
    # 'pmdro start -b 15' should run a session with only a 15 min break timer.
    # 'pmdro start -f 50 -b 10' should run a session with a 50 min focus timer and 10 min break timer.

    # Should there be a '-a' flag to auto start the break timer after the focus timer completes?

    click.echo(f"Focus duration: {focus_duration}")
    click.echo(f"Break duration: {break_duration}")
    click.echo("\nStarting new session...")

    if focus_duration is None and break_duration is None:
        focus_duration = FOCUS_DEFAULT_DURATION
        break_duration = BREAK_DEFAULT_DURATION

    if focus_duration is not None:
        click.echo(f"Starting {focus_duration} minute focus timer.")

    if break_duration is not None:
        if focus_duration is not None:
            if auto_break:
                click.echo("Focus timer complete! Auto starting break timer...")
                click.echo(f"Starting {break_duration} minute break timer.")
            else:
                if click.confirm(
                    f"Focus timer complete! Start {break_duration} minute break?",
                    default=True,
                ):
                    click.echo(f"Starting {break_duration} minute break timer.")
        else:
            click.echo(f"Starting {break_duration} minute break timer.")

        click.echo("Break timer complete!")
    else:
        click.echo("Focus timer complete!")

    # focus_seconds = focus_duration * 60

    # # App state load and save testing
    # state = load_state()
    # print(f"Timer state class: {state}")
    #
    # state.running = not state.running
    # print(f"Updated timer state class: {state}")
    #
    # save_state(state)
    #
    # # PID load and save testing
    # clear_pid()
    # pid = load_pid()
    # print(f"Current PID: {pid}\nShould be 'None'.")
    #
    # save_pid(4)
    # print("Look at '~/.config/pmdro/pmdro_pid' to see if value is 4.")
    #
    # pid = 98276
    # pid_is_running = is_process_running(pid)
    # print(f"\nProcess {pid} is running: {pid_is_running}")
    #
    # # Function arument testing
    # if focus_duration is not None:
    #     click.echo(f"Setting focus timer for {focus_duration} minutes.")
    #
    # # now = time.time()
    # # print(f"Current time: {now}")
    # # print(f"Data type of current time: {type(now)}")
    #
    # # with click.progressbar(range(focus_seconds)) as bar:
    # #     for _ in bar:
    # #         time.sleep(1)
    # #
    # if break_duration is not None:
    #     click.echo(f"Setting break timer for {break_duration} minutes.")
