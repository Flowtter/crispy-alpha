class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class WrongPath(Error):
    """Exception raised when no readers are plug to the computer.
    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message