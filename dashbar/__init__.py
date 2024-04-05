"""A progress-bar designed to be useful and easy to use."""

from . import _dashBuilder
from . import _dashbarElements
import shutil
from .exceptions import *

__all__ = [
    "customize",
    "log",
    "status",
    "dash",
    "autodash",
    "Dashbar",
]

__version__ = "2.0"
__description__ = "A progress-bar designed to be useful and easy to use."
__author__ = "xyzpw"
global all_bars
all_bars = dict(_dashbarElements.all_bars)

def customize(element: str, value: str) -> None:
    """Customizable dashbar is equivalent to 'classic' dashbar by default.

    Elements:
        start
        head
        trail
        filler
        finish"""
    global all_bars
    if not isinstance(element, str) or not isinstance(value, str):
        raise DashbarError("both parameters must type string")
    if element in all_bars["custom"]:
        if len(value) != 1:
            raise DashbarError("customizable element must be type char")
        all_bars["custom"][element] = value
        return
    raise DashbarError("customizable element does not exist")

spinner_parts = ['|', '/', '\u2013', '\\']

def log(text: str):
    global mydash
    try:
        print(f"\x1b[2K\r{text}\n{mydash}", end='', flush=True)
    except:
        return

def status(status_text: str = None):
    global mydash_status
    mydash_status = status_text

def dash(steps: int, dash_type: str = "classic", desc: str = None,
        percent: bool = False, spinner: bool = False, step_counter: bool = False):
    global mydash, mydash_status
    mydash_status = None
    progress = 0
    while progress < steps:
        yield progress
        progress += 1
        mydash = _dashBuilder.buildFromProgress(dash_type, progress, steps)
        if spinner and progress < steps-1:
            mydash += " " + str(spinner_parts[progress%4-1])
        if step_counter:
            mydash += f" {progress}/{steps}"
        if percent:
            mydash += " " + str(int(progress/steps*100)) + "%"
        if desc != None:
            textBeforeDash = desc
            if mydash_status != None:
                textBeforeDash += f": {mydash_status}"
            print(f"\x1b[2K\r{textBeforeDash} {mydash}", end='', flush=True)
        elif desc == None and mydash_status != None:
            print(f"\x1b[2K\r{mydash_status} {mydash}", end='', flush=True)
        else:
            print(f"\x1b[2K\r{mydash}", end='', flush=True)
        if progress == steps:
            del mydash_status
            print("\n", end='')
    del mydash

def autodash(count: int, dash_type: str = "classic", desc: str = None,
             percent: bool = False, spinner: bool = False,
             step_counter: bool = False):
    global mydash
    progress = 0
    while progress < count:
        yield progress
        progress += 1
        steps = shutil.get_terminal_size().columns-2
        steps = _dashBuilder.fixDashSteps(steps, desc, percent, spinner)
        if step_counter:
            steps -= len(str(count))*2+2
        equivalent_progress = int(progress / count * steps)
        mydash = _dashBuilder.buildFromProgress(dash_type, equivalent_progress, steps)
        if spinner and equivalent_progress < steps-1:
            mydash += " " + str(spinner_parts[progress%4-1])
        if step_counter:
            mydash += f" {progress}/{count}"
        if percent:
            mydash += " " + str(int(progress/count*100)) + "%"
        if bool(desc):
            print(f"\x1b[2K\r{desc} {mydash}", end='', flush=True)
        else:
            print(f"\x1b[2K\r{mydash}", end='', flush=True)
    del mydash

class Dashbar:
    def __init__(self, steps: int, dash_type: str = "classic",
                 desc: str = None, percent: bool = False, spinner: bool = False):
        self.steps = steps
        self.dash_type = dash_type
        self.desc = desc
        self.percent = percent
        self.spinner = spinner
        self.status = None
        self.progress = 0
        self.iscomplete = False
        self.build_dashbar()
    def build_dashbar(self):
        self.dashbar = _dashBuilder.buildFromProgress(self.dash_type, self.progress, self.steps)
        if self.spinner and self.progress <= self.steps-1:
            self.dashbar += " " + str(spinner_parts[self.progress%4-1])
        if self.percent:
            self.dashbar += " " + str(int(self.progress/self.steps*100)) + "%"
        if bool(self.desc):
            textBeforeDash = self.desc
            if bool(self.status):
                textBeforeDash += f": {self.status}"
            self.dashbar = f"{textBeforeDash} {self.dashbar}"
    def complete(self, display: bool = False):
        if self.iscomplete:
            return
        self.progress = self.steps
        self.build_dashbar()
        self.iscomplete = True
        if display:
            self.display()
    def update(self, count: int = 1, display: bool = False):
        if self.progress + count >= self.steps and not self.iscomplete:
            self.complete()
            if display:
                self.display()
            return
        elif self.iscomplete:
            raise DashbarError("dashbar is already complete")
        self.progress += count
        self.dashbar = _dashBuilder.buildFromProgress(self.dash_type, self.progress, self.steps)
        self.build_dashbar()
        if display:
            self.display()
    def display(self):
        print(f"\x1b[2K\r{self.dashbar}", end='', flush=True)
        if self.iscomplete:
            print("\n", end='', flush=True)
    def set_status(self, text: str = None) -> str:
        if self.iscomplete:
            raise DashbarError("dashbar is already complete")
        self.status = text
        self.build_dashbar()
    def log(self, text: str):
        print(f"\x1b[2K\r{text}\n{self.dashbar}", end='', flush=True)
