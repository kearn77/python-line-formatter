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


if __name__ == '__main__':
    # Get command line arguments.
    args = pargs.parser.parse_args()
    
    # Raise a FileException error if a text file is not passed via the cli.
    if args.infile.name[-4:] != ".txt":
        try:
            raise e.FileException(f"Please pass a .txt file to main.")
        except e.FileException as error:
            print(error)
            exit(0)
    
    # Create a linked list of lines of the appropriate length.
    source = (
        [line.rstrip() if line != "\n" else line 
            for line in open(args.infile.name)]
        )
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