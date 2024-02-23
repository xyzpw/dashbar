from . import _dashbarElements

global all_bars
all_bars = dict(_dashbarElements.all_bars)

def buildFromProgress(dash_type: str, progress: int, steps: int) -> str:
    dashElements = all_bars[dash_type]
    workingDash = dashElements["start"]
    workingDash += dashElements["trail"] * (progress-1) if progress >= 1 else ''
    workingDash += dashElements["head"] if progress >= 1 else ''
    workingDash += dashElements["filler"] * (steps-progress)
    workingDash += dashElements["finish"]
    return workingDash

def fixDashSteps(main_length: int, desc: str = None, percent: bool = False, spinner: bool = False):
    new_length = int(main_length)
    if bool(desc): new_length -= (len(desc) + 1)
    if bool(percent): new_length -= 5
    if bool(spinner): new_length -= 2
    return new_length
