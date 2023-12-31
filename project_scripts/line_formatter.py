# Standard library imports.
from sys import exit

# Local imports.
import exceptions as e
import linked_list as ll
import parse_args as pargs
from get_nodes import create_nodes
from get_nodes import model_lines

def add_breaks(text: str) -> str:
    """
    Adds a break tag - <br/> - to the end of a line.
    """
    input: list = text.split('\n')
    lines: list[str] = (
        [line + "<br/>" if line != '' else line
            for line in input]
        )
    output: str = '\n'.join(lines)

    return output

def add_headers(text: str, nums: list[int]) -> str:
    """
    Adds headers - # - at specified lines.
    """
    tags: tuple(str,int) = zip(["# "] + ["## "]*(len(nums)-1), nums)
    input: list = text.split('\n')
    for tag, num in tags:
        input[num] = tag + input[num]
        
    output: str = '\n'.join(input)

    return output

def preview(text: str) -> None:
    """
    Prints modified text to standard output.
    Output is enumerated to facilitate further editing.
    """
    input: list = text.split('\n')
    lines: list[(int,str)] = [(index,line) for index,line in enumerate(input)]
    for index, line in lines:
        print(index, line, sep=" => ")

def create_file(outfile: str, output: str) -> None:
    """
    Sends modified text to a new outfile.
    """
    with open(outfile,'w') as file_path:
        file_path.write(output)

def parse_lines(file_path: str):
    """
    Use open to read a file's contents, stripping whitespace while
    accounting for newlines and empty strings, which will be treated as
    newlines.
    """
    source: list[str] = []
    for line in open(file_path,'r'):
        if line == '\n':
            source.append(line)
        elif line.replace(' ','') == '\n':
            source.append('\n')
        else:
            source.append(line.rstrip())

    return source

def validate_file(file_path: str) -> None:
    """
    Validate the input file path passed to args.
    """
    try:
        if not file_path.endswith(".txt"):
            raise e.FileException("Input file must be in .txt format.")
    except e.FileException as err:
        print(err)
        exit(0)

def validate_length(length: int) -> None:
    """
    Validate the length passed to args.
    """
    try:
        if length < 1:
            raise e.LengthException(
                f"Please pass a natural number greater than zero to"
                f" the -l switch."
            )
    except e.LengthException as err:
        print(err)
        exit(0)

if __name__ == '__main__':
    # Get command line arguments.
    args = pargs.parser.parse_args()
    
    # Validate the input file format and length passed to args.
    validate_file(args.infile.name)
    validate_length(args.length)
    
    # Create a linked list of lines of the appropriate length.
    source = parse_lines(args.infile.name)
    node_dict = create_nodes(model_lines(source), source)
    head: ll.Node = node_dict[0]
    head.length = args.length
    node_links: ll.LinkedList = ll.LinkedList(head)

    # Generate output.  If breaktags is set to true, add breaktags
    # as necessary.
    if args.breaktags:
        raw_output = node_links.merge_nodes()
        output = add_breaks(raw_output)
    else:
        output = node_links.merge_nodes()

    #  Add headers if necessary.
    if args.hashtags:
        output = add_headers(output, args.hashtags)

    # Redirect output as specified by command line arguments.
    if args.preview:
        preview(output)

    if args.outfile:
        create_file(args.outfile.name, output)

    if not any([args.preview, args.outfile]):
        print(output)