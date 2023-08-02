class FileException(Exception):
    """
    An exception class for improperly formatted files.
    """

    def __init__(self, message):
        self.message = message