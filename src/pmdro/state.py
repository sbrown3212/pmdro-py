import json
import os
import signal
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


STATE_PATH = Path.home() / ".config" / "pmdro" / "pmdro_state.json"
PID_PATH = Path.home() / ".config" / "pmdro" / "pmdro_pid"


@dataclass
class TimerState:
    running: bool = field(default=False)
    paused: bool = field(default=False)
    total_seconds: int = field(default=0)
    remaining_seconds: int = field(default=0)
    start_time: Optional[float] = field(default=None)
    pause_time: Optional[float] = field(default=None)

    def to_dict(self):
        return {
            "running": self.running,
            "paused": self.paused,
            "total_seconds": self.total_seconds,
            "remaining_seconds": self.remaining_seconds,
            "start_time": self.start_time,
            "pause_time": self.pause_time,
        }

    @classmethod
    def from_dict(cls, data):
        state = cls()
        state.running = data.get("running", False)
        state.paused = data.get("paused", False)
        state.total_seconds = data.get("total_seconds", 0)
        state.remaining_seconds = data.get("remaining_seconds", 0)
        state.start_time = data.get("start_time", None)
        state.pause_time = data.get("pause_time", None)
        return state


# ************************* State functions *************************
# Use with thread implementation (to allow commands while timer is running).


def load_state():
    """Load timer state from file"""
    if not STATE_PATH.exists():
        return TimerState()

    try:
        with open(STATE_PATH, "r") as f:
            return TimerState.from_dict(json.load(f))
    except (json.JSONDecodeError, IOError):
        return TimerState()


def save_state(state: TimerState):
    """Save timer state to file"""
    with open(STATE_PATH, "w") as f:
        json.dump(state.to_dict(), f, indent=2)


# ************************* Process ID functions *************************
# Use with background process implementation


def load_pid():
    """Load background process id from file"""
    if not PID_PATH.exists():
        return None

    try:
        with open(PID_PATH, "r") as f:
            return int(f.read().strip())
    except (ValueError, IOError):
        # TODO: set up logging or return error.
        return None


def save_pid(pid: int):
    """Save background process id to file"""
    with open(PID_PATH, "w") as f:
        f.write(str(pid))


def clear_pid():
    """Remove PID file"""
    PID_PATH.unlink(missing_ok=True)


def is_process_running(pid: Optional[int]):
    """Check if a process with a given PID is currently running"""
    if pid is None:
        return False

    try:
        os.kill(pid, 0)  # does not kill proccess when `signal` is `0`.
        return True
    except ProcessLookupError:
        # TODO: set up logging or return error.
        return False
    # except PermissionError:


def timer_bg_process():
    """Background proccess that handles countdown timer"""
    # TODO: implement drift correction.

    def signal_handler(sig, frame):
        """Handle shutdown signals gracefully"""
        clear_pid()
        sys.exit(0)

    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)

    while True:
        state = load_state()

        if not state.running:
            clear_pid()
            break

        if state.paused:
            time.sleep(0.1)
            continue

        if state.remaining_seconds <= 0:
            state.running = False
            state.remaining_seconds = 0
            save_state(state)
            clear_pid()

            print("Timer finished!!!")
            break

        state.remaining_seconds -= 1
        save_state(state)
        time.sleep(1)
