class FileException(Exception):
    """
    An exception class for improperly formatted files.
    """
    def __init__(self, message):
        self.message = message

class LengthException(Exception):
    """
    An exception class for invalid input passed to the -l switch.
    """
    def __init__(self, message):
        self.message = message