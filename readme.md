## Line Formatter:  A CLI Application for Plain Text Files<br/>

line_formatter.py is a command line application with a simple  purpose:<br/>
enforce user-defined line breaks in a plain text file.  Not only do<br/>
line breaks make plain text files more readable, they also allow plain<br/>
text  to serve as an intermediary to other file formats, such as<br/>
markdown and markup.  This application facilitates that process.<br/>

In addition to its core line break functionality, line_formatter.py<br/>
provides some markdown specific features, like the ability to end lines<br/>
with break-tags and designate whether a line is a header.  This has<br/>
expedited my ability to write clean, concise markdown.  I’m sure<br/>
plenty of alternatives exist.  On the off chance that I am mistaken,<br/>
however, my modest application is made available here.<br/>

Broadly speaking, the application slices a text file’s lines into<br/>
keep and send components.  These components are used to create nodes in<br/>
a linked list.  Once all of the nodes have been linked, the node’s<br/>
contents are merged into a string, which is returned to the user.<br/>

## Table of Contents<br/>

### [format_fns.py](./project_scripts/format_fns.py)<br/>

This module contains four functions: get_attrs, split_at, keep_line,<br/>
and send_line.  Collectively, they are used to create the nodes that<br/>
compose a linked list.  The eval_node method - a member function of the<br/>
Node class - calls this group of functions to format a node’s line<br/>
value.<br/>

### [linked_list.py](./project_scripts/linked_list.py)<br/>

A linked list is a memory efficient data structure that is well suited<br/>
for insert and delete operations. It is composed of nodes, objects that<br/>
contain some data and a pointer to another node.  This pointer allows<br/>
the list to be stored non-sequentially in memory.  Moreover, in the<br/>
event that a value must be inserted or deleted, no shifting takes<br/>
place.  Rather, the pointers for the affected nodes are amended to<br/>
reflect the updated structure.  The linked list is instantiated with a<br/>
node designated as the head, which serves as the entry point to the<br/>
other nodes in the list.<br/>

The linked_list module implements this data structure.  The Node class<br/>
has three attributes: line, length, and next.  Line is a string taken<br/>
from the input file.  This attribute is accessed by the eval_node<br/>
method, which calls keep_line and send_line to create keep and send<br/>
components.  Line is set equal to the keep component, while the send<br/>
component is pushed to the next node and concatenated with that<br/>
node’s line value.  Length is the user provided number of characters<br/>
in a line.  Note that, in the event that the user does not provide a<br/>
line length, it defaults to eighty.  Effectively, all nodes inherit the<br/>
head node’s length value.<br/>

The LinkedList class has two methods: eval_recursive and merge_nodes.<br/>
Taking a linked list as an argument, the former uses recursion to<br/>
create new nodes to accommodate the changing structure of the input.<br/>
The latter merges the list’s line values into a single string.<br/>

### [get_nodes.py](./project_scripts/get_nodes.py)<br/>

The get_nodes module contains two functions that create the initial<br/>
linked list passed to eval_recursive.   Model lines, a helper function,<br/>
returns a list of two-tuples that index whether any given line is<br/>
followed by a non-empty line.  create_nodes takes this list as an<br/>
argument and returns a dictionary of node values, where the head node<br/>
is accessed by the key 0.<br/>

### [parse_args.py](./project_scripts/parse_args.py)<br/>

Utilizing python’s argparse library, parse_args.py instantiates an<br/>
ArgumentParser object named ‘parser,’  which creates the command<br/>
line interface the user interacts with to run the program.<br/>

### [exceptions.py](./project_scripts/exceptions.py)<br/>

Raises an error if the file passed to the command line interface does<br/>
not end in ‘.txt’.<br/>

### [line_formatter.py](./project_scripts/line_formatter.py)<br/>

This module serves as the entry point to the command line application.<br/>
It contains four functions - add_breaks, add_headers, preview, and<br/>
create_file - that are responsible for modifying the output returned by<br/>
the merge_nodes method.<br/>

## Example Usage<br/>

To demonstrate the module’s usage, we will create a markdown file out<br/>
of this readme’s introduction and table of contents.  This repository<br/>
contains directories named ‘input’ and ‘output.’  A plain text<br/>
file containing the readme text has been placed within the input<br/>
directory.  We will use line_formatter.py to create a corresponding<br/>
markdown file in the output directory.<br/>

Passing the -h switch to the command line displays all of the options<br/>
available to the user.  A quick survey of these options reveals that<br/>
the ‘-p’ switch will provide an enumerated preview of the<br/>
program’s output.  For example:<br/>

```
usage: line_formatter.py [-h] [-l] [-p] [-o] [-b] [-ht  [...]] infile

Enforce line breaks of an arbitrary length in a plain text file.

positional arguments:
  infile                The plain text file you would like to modify.

optional arguments:
  -h, --help            show this help message and exit
  -l , --length         The desired line length for your modified file.
                        Defaults to 80.
  -p, --preview         Preview enumerated output in the terminal.
  -o , --outfile        Redirect output to a new file.
  -b, --breaktags       Add break tags to all lines that are not newline
                        characters.
  -ht  [ ...], --hashtags  [ ...]
                        Insert headers at specified lines.

If neither -p nor -o are true, then non-enumerated output is printed to the
terminal. If the -ht optional switch is passed directly before the infile,
then pass a double dash between the two, e.g. -ht -- infile.
```

After experimenting with several line lengths, we determine that we<br/>
would like the lines in our markdown files to be no longer than<br/>
seventy-two characters, with headers placed at lines  zero and twenty.<br/>

To accomplish this, we must pass four switches to the interface: the<br/>
length switch, ‘-l’; the break-tag switch, ‘-b’; the hashtag<br/>
switch, ‘-ht’; and the outfile switch, ‘-o’.  The following<br/>
command creates a markdown file in the desired folder.<br/>

```
python .\project_scripts\line_formatter.py .\input_files\revised_introduction.txt -ht 0 20 -b -l 72 -o introduction.md
```

## Potential Improvements<br/>

There is no reason to limit this application to .txt input.  Hopefully,<br/>
I can expand processing to popular file formats.  After all, the<br/>
grammar and spell checking provided by modern word  processors is a<br/>
difficult thing to forfeit.<br/>

Adding more markdown specific features will greatly improve the<br/>
application, such as the ability to recognize code blocks and escape<br/>
special markdown characters.<br/>

From an aesthetic standpoint, splitting a line  may not make sense.<br/>
Exploring stylistic considerations in determining line breaks will<br/>
almost certainly improve the program.<br/>

Although the application in its current state is far from perfect, I<br/>
hope it can serve as a point of reference for programmers solving<br/>
similar problems.  Thanks for reading!<br/>