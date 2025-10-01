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
