__all__ = [
    "DashbarError",
]

class DashbarError(Exception):
    """Dashbar exception."""
    def __init__(self, reason: str = ""):
        self.reason = reason