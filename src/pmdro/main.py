import click
import threading
import time


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
    focus_seconds = focus_duration * 60
    if focus_duration is not None:
        click.echo(f"Setting focus timer for {focus_duration} minutes.")

    with click.progressbar(range(focus_seconds)) as bar:
        for _ in bar:
            time.sleep(1)

    if break_duration is not None:
        click.echo(f"Setting break timer for {break_duration} minutes.")


# class Timer:
#     def __init__(self):
#         self.running = False
#         self.paused = False
#         self.thread = None
#         # self.start_time = None
#         # self.total_paused_duration = None # or 0
#         self.end_time = None
#
#     def start(self, duration_minutes):
#         """Start countdown timer"""
#         if self.running is True:
#             return False
#
#         self.running = True
#         self.paused = False
#         self.end_time = time.time() + (duration_minutes * 60)
#         self.thread = threading.Thread(target=self._countdown_loop)
#         self.thread.daemon = True
#         self.thread.start()
#         return True
#
#     def _countdown_loop(self):
#         """Internal countdown loop"""
#         while self.running:
#             if not self.paused:
#                 current_time = time.time()
#                 remaining = self.end_time - current_time
#
#                 if remaining <= 0:
#                     print("\nTime's up")
#                     self.running = False
#                     break
#
#                 min, sec = divmod(int(remaining), 60)
#                 print(f"\r{min:02d}:{sec:02d}", end="", flush=True)
#
#             time.sleep(0.1)
#
#     def stop(self):
#         """Terminate countown timer."""
#         self.running = False
#         if self.thread:
#             self.thread.join()
