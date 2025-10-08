import click
import time

# import os
# import subprocess
# import threading

# from pmdro.state import (
#     TimerState,
#     load_state,
#     save_state,
#     # load_pid,
#     # save_pid,
#     # clear_pid,
#     # is_process_running,
# )


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
)
@click.option(
    "-b",
    "--break",
    "break_duration",
    type=click.IntRange(1),
    help="Include break timer. Requires integer argument to specify timer duration (in minutes).",
    default=None,
    is_flag=False,
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

    # CMD = """
    # on run argv
    #     display notification (item 2 of argv) with title (item 1 of argv)
    # end run
    # """

    # def notify(title, text):
    #     subprocess.call(["osascript", "-e", CMD, title, text])

    # def notify(title, text):
    #     os.system(
    #         """
    #               osascript -e 'display notification "{}" with title "{}"'
    #               """.format(text, title)
    #     )

    def run_timer(duration_seconds: int):
        start_time = time.time()

        mins, secs = divmod(duration_seconds, 60)
        initial_template = (
            f"%(label)s [%(bar)s] %(info)s- Remaining: {mins:02d}:{secs:02d}"
        )

        with click.progressbar(
            length=duration_seconds,
            show_eta=False,
            show_percent=False,
            bar_template=initial_template,
        ) as bar:
            last_update = 0

            while True:
                current_time = time.time()
                elapsed = int(current_time - start_time)
                remaining = max(0, duration_seconds - elapsed)

                mins, secs = divmod(remaining, 60)
                bar.bar_template = (
                    f"%(label)s [%(bar)s] %(info)s- Remaining: {mins:02d}:{secs:02d}"
                )

                if elapsed > last_update:
                    bar.update(elapsed - last_update)
                    last_update = elapsed

                if remaining <= 0:
                    bar.update(duration_seconds - last_update)
                    break

                time.sleep(0.1)

            click.echo("\nTimer complete.")

    # Calculate duration in seconds
    if focus_duration is None and break_duration is None:
        # If no arguments are provided, session runs with focus and break timer.
        focus_duration = FOCUS_DEFAULT_DURATION
        break_duration = BREAK_DEFAULT_DURATION
    # Use arguments as minutes. (comment out for testing)
    focus_seconds = focus_duration * 60 if focus_duration is not None else 0
    break_seconds = break_duration * 60 if break_duration is not None else 0

    # # Use arguments as seconds. (uncomment for testing)
    # focus_seconds = focus_duration if focus_duration is not None else 0
    # break_seconds = break_duration if break_duration is not None else 0

    # Not currently using state (not using threads)
    # # Initialize state
    # state = TimerState()
    # # TODO: set timer state for conditions below.

    click.echo("Starting new pmdro session.\n")

    if focus_duration is not None:
        click.echo(f"Starting {focus_duration} minute focus timer.")
        run_timer(focus_seconds)

    if break_duration is not None:
        if focus_duration is not None:
            # Handle break timer after focus timer completes.
            if auto_break:
                click.echo("\nAuto starting break timer...")
                click.echo(f"Starting {break_duration} minute break timer.")
                run_timer(break_seconds)
            else:
                if click.confirm(
                    f"\nStart {break_duration} minute break?",
                    default=True,
                ):
                    click.echo(f"Starting {break_duration} minute break timer.")
                    run_timer(break_seconds)
                else:
                    return
        else:
            # No focus timer, only break timer.
            click.echo(f"Starting {break_duration} minute break timer.")
            run_timer(break_seconds)

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
