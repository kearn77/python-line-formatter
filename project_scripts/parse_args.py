import argparse

# Create an ArgumentParser that will evaluate arguments passed to main.py.
parser: argparse.ArgumentParser = argparse.ArgumentParser(
    prog = "line_formatter.py",
    description = (
        f"Enforce line breaks of an arbitrary length in a plain text file."
        ),
    epilog = (
        f"If neither -p nor -o are true, then non-enumerated output is "
        f"printed to the terminal.  "
        f"If the -ht optional switch is passed directly before the infile, then "
        f"pass a double dash between the two, e.g. -ht -- infile."
        ),
    add_help = True,
    )

# Add a required position argument named infile.
parser.add_argument(
    "infile",
    type = argparse.FileType('r', encoding="utf-8"),
    help = "The plain text file you would like to modify."
    )

# Add an optional keyword argument named length.
parser.add_argument(
    "-l",
    "--length",
    type = int,
    default = 80,
    required = False,
    help = "The desired line length for your modified file.  Defaults to 80.",
    metavar = ''
    )

# Add an optional argument that preview's the program's output in the terminal.
parser.add_argument(
    "-p",
    "--preview",
    action = "store_true",
    help = "Preview enumerated output in the terminal.",
)

# Redirect the program's output to a new file.
parser.add_argument(
    "-o",
    "--outfile",
    type = argparse.FileType('w', encoding="utf-8"),
    help = "Redirect output to a new file.",
    metavar = ''
)

# Add line breaks to the program's output.
parser.add_argument(
    "-b",
    "--breaktags",
    action = "store_true",
    help = "Add break tags to all lines that are not newline characters."
)

# Insert headers.
parser.add_argument(
    "-ht", 
    "--hashtags", 
    type = int, 
    nargs = "+", 
    help = "Insert headers at specified lines.",
    metavar = ''
)