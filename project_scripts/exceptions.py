class FileException(Exception):
    """
    An exception class for improperly formatted files.
    """

    def __init__(self, message):
        super().__init__(message)


class ParseArgs:
    """
    Parses the arguments passed to main.py.  Raises 
    exceptions as necessary.
    """
    def __init__(self, args: list):
        self.args = args
        self.length = None

    def parse_files(self):
        if len(self.args) == 1:
            raise FileException("Please pass a plain text file to main.py.")